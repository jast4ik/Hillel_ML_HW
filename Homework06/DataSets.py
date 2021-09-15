import struct
from os.path import isfile
import pandas as pd
import gc
import re
import numpy as np
import scipy.stats
from scipy.stats import zscore
import matplotlib.pyplot as plt
import seaborn as sns
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pickle


def get_src_df(regenerate=False, strip_str=True, encode_labels=False):
    src_df = pd.DataFrame()

    if isfile("./data/src_df.pkl") and not regenerate:
        src_df = pd.read_pickle(filepath_or_buffer="./data/src_df.pkl", compression='zip')
        print("\nSource dataframe loaded.")
    else:
        src_df = pd.read_csv('./data/true_car_listings_prepeared.csv')
        src_df.drop('Vin', inplace=True, axis=1)

        src_df.drop_duplicates(inplace=True)

        if strip_str:
            src_df['Model'] = src_df['Model'].map(
                lambda x: "".join(re.findall("[a-zA-Z0-9]+", x)) if type(x) is str else np.NaN
            )
            src_df['Model'] = src_df['Model'].map(
                lambda x: str.upper(x) if type(x) is str else np.NaN
            )

            src_df['Make'] = src_df['Make'].map(
                lambda x: "".join(re.findall("[a-zA-Z]+", x)) if type(x) is str else np.NaN
            )
            src_df['Make'] = src_df['Make'].map(
                lambda x: str.upper(x) if type(x) is str else np.NaN
            )

            src_df['City'] = src_df['City'].map(
                lambda x: "".join(re.findall("[a-zA-Z]+", x)) if type(x) is str else np.NaN
            )
            src_df['City'] = src_df['City'].map(
                lambda x: str.upper(x) if type(x) is str else np.NaN
            )

            src_df['State'] = src_df['State'].map(
                lambda x: "".join(re.findall("[a-zA-Z]+", x)) if type(x) is str else np.NaN
            )
            src_df['State'] = src_df['State'].map(
                lambda x: str.upper(x) if type(x) is str else np.NaN
            )

        if encode_labels:
            temp_df = src_df[['Model', 'Make', 'City', 'State']].astype('category').apply(lambda x: x.cat.codes)
            temp_df = temp_df.where(~src_df.isna(), src_df)

            src_df['Model'] = temp_df['Model']
            src_df['Make'] = temp_df['Make']
            src_df['City'] = temp_df['City']
            src_df['State'] = temp_df['State']

            del temp_df
            gc.collect()

        src_df.to_pickle(path="./data/src_df.pkl", compression='zip')
        print("\nSource dataframe created.")

    return src_df


def get_clear_df(regenerate=False):
    clear_df = pd.DataFrame()

    if isfile("./data/clear_df.pkl") and not regenerate:
        clear_df = pd.read_pickle(filepath_or_buffer="./data/clear_df.pkl", compression='zip')
        print("\nClear dataframe loaded.")
    else:
        src_df = get_src_df()

        clear_df = src_df.loc[
            (src_df['Price'] > 0) &
            (~src_df['Mileage'].isna()) &
            (src_df['Mileage'] > 0) &
            (~src_df['Model'].isna())
        ]

        clear_df.to_pickle(path="./data/clear_df.pkl", compression='zip')
        print("\nClear dataframe created.")

        del src_df
        gc.collect()

    return clear_df


def get_label_encoded_clear_df(regenerate=False):
    result_df = pd.DataFrame()

    if isfile("./data/clear_label_encoded_df.pkl") and not regenerate:
        result_df = pd.read_pickle(filepath_or_buffer="./data/clear_label_encoded_df.pkl", compression='zip')
        print("\nLabel encoded dataframe loaded.")
    else:
        result_df = get_clear_df()

        result_df['Model'] = result_df['Model'].astype('category').cat.codes
        result_df['Make'] = result_df['Make'].astype('category').cat.codes
        result_df['City'] = result_df['City'].astype('category').cat.codes
        result_df['State'] = result_df['State'].astype('category').cat.codes

        result_df.to_pickle(path="./data/clear_label_encoded_df.pkl", compression='zip')
        print("\nLabel encoded dataframe created.")

    return result_df


def impute_mileage(regenerate=False):
    result_df = get_src_df()

    max_year = result_df.Year.max()

    for index in result_df.index:
        if result_df.loc[index, 'Year'] == max_year and \
                (result_df.loc[index, 'Mileage'] < 5 or np.isnan(result_df.loc[index, 'Mileage'])):
            result_df.loc[index, 'Mileage'] = 5

    xgb_model = xgb.XGBRegressor()

    if isfile("./data/models/mileage_imputation_model.pkl") and not regenerate:
        with open("./data/models/mileage_imputation_model.pkl", "rb") as m_file:
            xgb_model = pickle.load(m_file)
    else:
        clear_e_df = get_src_df().dropna(axis=0)

        max_limit = clear_e_df['Mileage'].quantile(0.995)
        min_limit = clear_e_df['Mileage'].quantile(0.005)

        clear_e_df = clear_e_df[(clear_e_df['Mileage'] < max_limit) & (clear_e_df['Mileage'] > min_limit)]

        X = clear_e_df[['Year', 'Make', 'State', 'City', 'Price', 'Model']]
        y = clear_e_df['Mileage']

        print(X.dtypes)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

        dmatrix_train = xgb.DMatrix(data=X_train, label=y_train)
        dmatrix_test = xgb.DMatrix(data=X_test, label=y_test)

        xgb_model = xgb.train(params={'objective': 'reg:squarederror'},
                              dtrain=dmatrix_train,
                              evals=[(dmatrix_train, "train"), (dmatrix_test, "validation")],
                              num_boost_round=10000,
                              verbose_eval=20,
                              early_stopping_rounds=25
                              )

        del clear_e_df
        del X
        del y
        del X_test
        del y_test
        del X_train
        del y_train
        del dmatrix_test
        del dmatrix_train
        gc.collect()

        with open("./data/models/mileage_imputation_model.pkl", "wb") as m_file:
            pickle.dump(xgb_model, m_file)

    to_predict_df = result_df.loc[
        (result_df['Mileage'].isna()) &
        (result_df['Price'] != 0) &
        (~result_df['Model'].isna())
        ]

    to_predict_df = to_predict_df[['Year', 'Make', 'State', 'City', 'Price', 'Model']]

    dmatrix_predict = xgb.DMatrix(to_predict_df)
    xgb_preds = xgb_model.predict(dmatrix_predict)
    print(xgb_preds)
    print(to_predict_df.head)

    return result_df


if __name__ == "__main__":
    src_df = get_src_df(regenerate=True, strip_str=True, encode_labels=True)
    print(src_df.isna().sum())
    print(src_df.head)
    mi_df = impute_mileage(regenerate=True)
    print(mi_df.isna().sum())
    exit()

    src_df = get_src_df(regenerate=False)
    clear_df = get_clear_df(regenerate=False)
    #enc_df = get_label_encoded_clear_df(regenerate=True)

    max_limit = src_df['Mileage'].quantile(0.995)
    min_limit = src_df['Mileage'].quantile(0.005)

    print(src_df.shape)

    src_df = src_df[(src_df['Mileage'] < max_limit) & (src_df['Mileage'] > min_limit)]

    print(src_df.shape)

    sns.pairplot(src_df)
    plt.show()

    src_df['Price_Z'] = src_df[['Price']].apply(scipy.stats.zscore)
    src_df['Mileage_Z'] = src_df[['Price']].apply(scipy.stats.zscore)
    z_limit = 3.5
    src_df = src_df.loc[
        (src_df['Price_Z'] < z_limit) &
        (src_df['Price_Z'] > -1 * z_limit) &
        (src_df['Mileage_Z'] < z_limit) &
        (src_df['Mileage_Z'] > -1 * z_limit)
    ]

    #src_df.drop(['Price_Z'], axis=1, inplace=True)
    #src_df.drop(['Mileage_Z'], axis=1, inplace=True)
    print(src_df.head)

    #sns.pairplot(src_df)
    #sns.displot(src_df['Mileage'])
    #plt.show()

    print(src_df['Mileage'].max())