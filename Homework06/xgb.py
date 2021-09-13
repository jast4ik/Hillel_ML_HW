import pandas as pd
import xgboost as xgb
from sklearn.metrics import r2_score
import numpy as np
from sklearn.model_selection import train_test_split
import DataSets as ds
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

if __name__ == "__main__":
    #encoded_df = ds.get_lable_encoded_clear_df()

    #upper_limit = encoded_df['Price'].quantile(0.995)
    #bottom_limit = encoded_df['Price'].quantile(0.005)

    #print(upper_limit, bottom_limit)

    #encoded_df = encoded_df[encoded_df['Price'].between(bottom_limit, upper_limit)]

    #upper_limit = encoded_df['Mileage'].quantile(0.995)
    #bottom_limit = encoded_df['Mileage'].quantile(0.005)

    #print(upper_limit, bottom_limit)

    #encoded_df = encoded_df[encoded_df['Mileage'].between(bottom_limit, upper_limit)]

    #print(encoded_df.head)
    src_df = ds.get_clear_df()#ds.get_src_df(regenerate=True, proceed_str=True)

    src_df['Model'] = src_df['Model'].astype('category').cat.codes
    src_df['Make'] = src_df['Make'].astype('category').cat.codes
    src_df['City'] = src_df['City'].astype('category').cat.codes
    src_df['State'] = src_df['State'].astype('category').cat.codes
    #src_df['Year'] = src_df['Year'].astype('float')
    src_df.drop('Vin', inplace=True, axis=1)

    X = src_df[['Year', 'Mileage', 'Make', 'Model', 'State', 'City']]
    y = src_df['Price']



    print(src_df.dtypes)


    sns.heatmap(src_df.corr(), annot=True)
    plt.show()

    #X = X.apply(scipy.stats.zscore)
    #y = y.apply(np.log)
    #X['Mileage'] = X['Mileage'].map(np.log)
    #print(X.head)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=2)

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

    xgb.plot_importance(xgb_model, title="Clear data after string processing.")




