import struct
from os.path import isfile
import pandas as pd
import gc
import re
import numpy as np
from scipy.stats import zscore


def get_src_df(regenerate=False, proceed_str=True):
    src_df = pd.DataFrame()

    if isfile("./data/src_df.pkl") and not regenerate:
        src_df = pd.read_pickle(filepath_or_buffer="./data/src_df.pkl", compression='zip')
        print("\nSource dataframe loaded.")
    else:
        src_df = pd.read_csv('./data/true_car_listings_prepeared.csv')

        if proceed_str:
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
            (src_df['Price'] != 0) &
            (~src_df['Mileage'].isna()) &
            (src_df['Mileage'] != 0) &
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
        clear_df = get_clear_df()

        make_cat = pd.DataFrame()
        model_cat = pd.DataFrame()
        make_model_cat = pd.DataFrame()
        state_cat = pd.DataFrame()
        city_cat = pd.DataFrame()
        #make_cat['Make_cat'] = clear_df['Make'].astype('category').cat.codes
        #model_cat['Model_cat'] = clear_df['Model'].astype('category').cat.codes
        state_cat['City_cat'] = clear_df['City'].astype('category').cat.codes
        city_cat['State_cat'] = clear_df['State'].astype('category').cat.codes

        result_df = clear_df.select_dtypes(include=['int64', 'float64'])
        #result_df = result_df.join(model_cat)
        #result_df = result_df.join(make_cat)
        make_model_cat['Make_Model'] = clear_df['Make'] + clear_df['Model']
        make_model_cat['Make_Model'] = make_model_cat['Make_Model'].astype('category').cat.codes
        result_df = result_df.join(city_cat)
        result_df = result_df.join(state_cat)
        result_df = result_df.join(make_model_cat)

        del clear_df
        del make_cat
        del model_cat
        gc.collect()

        result_df.to_pickle(path="./data/clear_label_encoded_df.pkl", compression='zip')
        print("\nLabel encoded dataframe created.")

    return result_df


if __name__ == "__main__":
    pass
    src_df = get_src_df(regenerate=True, proceed_str=True)
    #print(len(src_df['Make'].unique()))
    #print(src_df.isna().sum())
    print(src_df.head)
    clear_df = get_clear_df(regenerate=True)
    print(clear_df.shape, src_df.shape)
