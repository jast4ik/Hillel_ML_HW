import gc

import pandas as pd
import numpy as np
from os.path import isfile
import sys
import matplotlib.pyplot as plt
from xgboost import XGBRegressor
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import seaborn as sns


# region Functions to show memory used by pandas
def obj_size_fmt(num):
    if num < 10 ** 3:
        return "{:.2f}{}".format(num, "B")
    elif (num >= 10 ** 3) & (num < 10 ** 6):
        return "{:.2f}{}".format(num / (1.024 * 10 ** 3), "KB")
    elif (num >= 10 ** 6) & (num < 10 ** 9):
        return "{:.2f}{}".format(num / (1.024 * 10 ** 6), "MB")
    else:
        return "{:.2f}{}".format(num / (1.024 * 10 ** 9), "GB")


def memory_usage():
    memory_usage_by_variable = pd.DataFrame({k: sys.getsizeof(v) for (k, v) in globals().items()}, index=['Size'])
    memory_usage_by_variable = memory_usage_by_variable.T
    memory_usage_by_variable = memory_usage_by_variable.sort_values(by='Size', ascending=False).head(10)
    memory_usage_by_variable['Size'] = memory_usage_by_variable['Size'].apply(lambda x: obj_size_fmt(x))
    return memory_usage_by_variable


# endregion


if __name__ == "__main__":

    src_df = pd.DataFrame()
    clear_df = pd.DataFrame()
    numeric_df = pd.DataFrame()

    if isfile("./data/src_df.pkl"):
        print("src_df:\tloading...")
        src_df = pd.read_pickle(filepath_or_buffer="./data/src_df.pkl", compression='zip')
        print("src_df:\tdone")
    else:
        print("src_df:\tprocessing...")
        src_df = pd.read_csv('./data/true_car_listings_prepeared.csv')
        src_df.drop(['Vin'], axis=1, inplace=True)
        #src_df.drop(['City'], axis=1, inplace=True)
        src_df.to_pickle(path="./data/src_df.pkl", compression='zip')
        print("src_df:\tdone")

    max_year = src_df['Year'].max()

    if isfile("./data/num_df.pkl"):
        print("num_df:\tloading...")
        numeric_df = pd.read_pickle(filepath_or_buffer="./data/num_df.pkl", compression='zip')
        print("num_df:\tdone")
    else:
        print("num_df:\tprocessing...")
        numeric_df = src_df.loc[
            (src_df['Price'] != 0) &
            (~src_df['Mileage'].isna()) &
            (~src_df['Model'].isna())
        ].select_dtypes(include=['int64', 'float64'])
        numeric_df.to_pickle(path="./data/num_df.pkl", compression='zip')
        print("num_df:\tdone")

    xgb_model = XGBRegressor(
        max_depth=6, n_estimators=100, n_jobs=8, booster='gbtree', random_state=42, learning_rate=0.05
    )

    X = numeric_df[['Year', 'Price']].astype(np.float64)
    y = numeric_df['Mileage'].astype(np.float64)

    make_cat = pd.DataFrame()
    model_cat = pd.DataFrame()
    state_cat = pd.DataFrame()
    city_cat = pd.DataFrame()
    make_cat['Make_cat'] = src_df['Make'].astype('category').cat.codes
    #model_cat['Model_cat'] = src_df['Model'].astype('category').cat.codes
    #state_cat['State_cat'] = src_df['State'].astype('category').cat.codes
    #city_cat['City_cat'] = src_df['City'].astype('category').cat.codes
    #make_cat = pd.get_dummies(src_df['Make'], prefix="model")
    model_cat = pd.get_dummies(src_df['Model'], prefix="make")

    X = X.join(model_cat)
    X = X.join(make_cat)
    #X = X.join(state_cat)
    #X = X.join(city_cat)
    #X['YP'] = X['Price'] * X['Make_cat'] * X['Model_cat']

    #for key in X:
    #    X[key] = (X[key] - X[key].mean()) / X[key].std()

    #print(X.head)
    #sns.heatmap(X.corr(), annot=True)

    del numeric_df
    del src_df
    gc.collect()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    xgb_model.fit(X_train, y_train)
    xgb_pred = xgb_model.predict(X_test)

    print(r2_score(y_test, xgb_pred))

    #xgb.plot_importance(xgb_model)

    #plt.show()

