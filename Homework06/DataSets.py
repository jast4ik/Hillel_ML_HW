from os.path import isfile
import pandas as pd
import gc
import numpy as np
from scipy.stats import zscore


def get_src_df():
    src_df = pd.DataFrame()

    if isfile("./data/src_df.pkl"):
        src_df = pd.read_pickle(filepath_or_buffer="./data/src_df.pkl", compression='zip')
        print("\nSource dataframe loaded.")
    else:
        src_df = pd.read_csv('./data/true_car_listings_prepeared.csv')
        src_df.drop(['Vin'], axis=1, inplace=True)
        src_df.to_pickle(path="./data/src_df.pkl", compression='zip')
        print("\nSource dataframe created.")

    return src_df


def get_clear_df():
    clear_df = pd.DataFrame()

    if isfile("./data/clear_df.pkl"):
        clear_df = pd.read_pickle(filepath_or_buffer="./data/clear_df.pkl", compression='zip')
        print("\nClear dataframe loaded.")
    else:
        src_df = get_src_df()

        clear_df = src_df.loc[
            (src_df['Price'] != 0) &
            (~src_df['Mileage'].isna()) &
            (~src_df['Model'].isna())
        ]

        clear_df.to_pickle(path="./data/num_df.pkl", compression='zip')
        print("\nClear dataframe created.")

        del src_df
        gc.collect()

    return clear_df


def get_lable_encoded_clear_df():
    result_df = pd.DataFrame()

    if isfile("./data/clear_label_encoded_df.pkl"):
        result_df = pd.read_pickle(filepath_or_buffer="./data/clear_label_encoded_df.pkl", compression='zip')
        print("\nLabel encoded dataframe loaded.")
    else:
        clear_df = get_clear_df()

        make_cat = pd.DataFrame()
        model_cat = pd.DataFrame()
        state_cat = pd.DataFrame()
        city_cat = pd.DataFrame()
        make_cat['Make_cat'] = clear_df['Make'].astype('category').cat.codes
        model_cat['Model_cat'] = clear_df['Model'].astype('category').cat.codes
        state_cat['City_cat'] = clear_df['City'].astype('category').cat.codes
        city_cat['State_cat'] = clear_df['State'].astype('category').cat.codes

        result_df = clear_df.select_dtypes(include=['int64', 'float64'])
        result_df = result_df.join(model_cat)
        result_df = result_df.join(make_cat)
        result_df = result_df.join(city_cat)
        result_df = result_df.join(state_cat)


        del clear_df
        del make_cat
        del model_cat
        gc.collect()

        result_df.to_pickle(path="./data/clear_label_encoded_df.pkl", compression='zip')
        print("\nLabel encoded dataframe created.")

    return result_df


if __name__ == "__main__":
    pass
    src_df = get_lable_encoded_clear_df()
    print(src_df.head)