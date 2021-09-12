import gc

import pandas as pd
import numpy as np
from os.path import isfile
import sys
#from sklearn.model_selection import GridSearchCV
# import matplotlib.pyplot as plt
from xgboost.sklearn import XGBRegressor
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
# import seaborn as sns
from sklearn.model_selection import KFold
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
import sklearn


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



    max_year = src_df['Year'].max()



    #xgb_model = XGBRegressor(
    #    max_depth=6,
    #    n_estimators=100,
    #    n_jobs=8,
    #    booster='gbtree',
    #    random_state=42,
    #    learning_rate=0.05
    #)

    X = numeric_df[['Year', 'Price']].astype(np.float64)
    y = numeric_df['Price'].astype(np.float64)

    make_cat = pd.DataFrame()
    model_cat = pd.DataFrame()
    make_cat['Make_cat'] = src_df['Make'].astype('category').cat.codes
    model_cat['Model_cat'] = src_df['Model'].astype('category').cat.codes

    X = X.join(model_cat)
    X = X.join(make_cat)

    del numeric_df
    del src_df
    gc.collect()

    #sns.pairplot(X.join(y), x_vars=['Model_cat', 'Make_cat', 'Year', 'Price'], y_vars='Mileage', height=7, aspect=0.7, kind='reg')

    #X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

    #xgb_model.fit(X_train, y_train)
    #xgb_pred = xgb_model.predict(X_test)

    #print(r2_score(y_test, xgb_pred))

    #xgb.plot_importance(xgb_model)
    #plt.show()

    #k_fold = KFold(n_splits=20, shuffle=True, random_state=42)
    #k_fold.get_n_splits(X)

    #xgb_best_model = XGBRegressor()
    #xgb_best_score = 0.0

    #for train_index, test_index in k_fold.split(X):
    #    X_train = X.iloc[train_index][['Make_cat', 'Year', 'Price']]
    #    X_test = X.iloc[test_index][['Make_cat', 'Year', 'Price']]
    #    y_train = y.iloc[train_index]
    #    y_test = y.iloc[test_index]

    #    model = XGBRegressor(max_depth=6,
    #                         n_estimators=100,
    #                         n_jobs=8,
    #                         booster='gbtree',
    #                         random_state=42,
    #                         learning_rate=0.05)
    #    model.fit(X_train, y_train)
    #    preds = model.predict(X_test)

    #    r2 = r2_score(y_test, preds)
    #    if r2 > xgb_best_score:
    #        xgb_best_model = model
    #        xgb_best_score = r2
    #        print("Best r2: ", r2)

    X_ = X.sample(frac=0.01, random_state=42)
    y_ = y.sample(frac=0.01, random_state=42)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

    #dmatrix = xgb.DMatrix(data=X, label=y)

    params = {'max_depth': [10, 11, 12, 13, 14],
              'learning_rate': [0.005, 0.0045, 0.004, 0.003, 0.0035, 0.002, 0.0025, 0.0055, 0.006],
              'subsample': np.arange(0.5, 1.0, 0.1),
              'colsample_bytree': np.arange(0.8, 1.0, 0.05),
              'colsample_bylevel': np.arange(0.2, 0.6, 0.05),
              'n_estimators': [800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200],
              }

    #print(sorted(sklearn.metrics.SCORERS.keys()))

    xgbr = xgb.XGBRegressor(seed=20, objective='reg:squarederror')

    clf = RandomizedSearchCV(estimator=xgbr,
                             param_distributions=params,
                             scoring='r2',
                             verbose=1,
                             n_iter=20)

    clf.fit(X, y)

    preds = clf.predict(X_test)

    r2 = r2_score(y_test, preds)

    print("Best parameters:", clf.best_params_)
    print("Best RMSE: ", clf.best_score_)
    print("Best r2: ", r2)
