import scipy.stats
import xgboost as xgb
import pickle
from sklearn.metrics import r2_score
import pandas as pd
import numpy as np
from os.path import isfile
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import DataSets as ds

if __name__ == "__main__":
    encoded_df = ds.get_lable_encoded_clear_df()

    X = encoded_df[['Year', 'Mileage', 'Model_cat', 'Make_cat']]
    y = encoded_df['Price']

    X = X.apply(scipy.stats.zscore)
    y = y.apply(np.log)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=42)

    dmatrix_train = xgb.DMatrix(data=X_train, label=y_train)
    dmatrix_test = xgb.DMatrix(data=X_test, label=y_test)

    xgb_model = xgb.train(params={'objective': 'reg:squarederror'},
                          dtrain=dmatrix_train,
                          evals=[(dmatrix_train, "train"), (dmatrix_test, "validation")],
                          num_boost_round=10000,
                          verbose_eval=20,
                          early_stopping_rounds=25
                          )

    xgb_preds = xgb_model.predict(dmatrix_test)
    r2 = r2_score(y_test, xgb_preds)

    print("Best r2: ", r2)
