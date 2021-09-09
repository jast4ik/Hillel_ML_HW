import xgboost as xgb
import pickle
from sklearn.metrics import r2_score
import pandas as pd
import numpy as np
from os.path import isfile
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

if __name__ == "__main__":
    if isfile("./data/src_df.pkl"):
        print("src_df:\tloading...")
        src_df = pd.read_pickle(filepath_or_buffer="./data/src_df.pkl", compression='zip')
        print("src_df:\tdone")
    else:
        exit(-2)

    if isfile("./data/num_df.pkl"):
        print("num_df:\tloading...")
        numeric_df = pd.read_pickle(filepath_or_buffer="./data/num_df.pkl", compression='zip')
        print("num_df:\tdone")
    else:
        exit(-2)

    X = numeric_df[['Year', 'Mileage']].astype(np.float64)
    y = numeric_df['Price'].astype(np.float64)

    make_cat = pd.DataFrame()
    model_cat = pd.DataFrame()
    make_cat['Make_cat'] = src_df['Make'].astype('category').cat.codes
    model_cat['Model_cat'] = src_df['Model'].astype('category').cat.codes

    X = X.join(model_cat)
    X = X.join(make_cat)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=42)

    dmatrix_train = xgb.DMatrix(data=X_train, label=y_train)
    dmatrix_test = xgb.DMatrix(data=X_test, label=y_test)

    xgb_params = {
        'max_depth': 6,
        'learning_rate': 0.05,
        'subsample': 0.975,
        'colsample_bytree': 0.65,
        'colsample_bylevel': 0.65,
        'n_estimators': 950,
        'reg_alpha': 0.053,
    }

    xgb_model = xgb.XGBRegressor(validate_parameters=xgb_params, objective='reg:squarederror')

    if isfile("./data/models/xgb_model.model"):
        print("XGB model:\tload...")
        # xgb_model.load_model("./data/models/xgb_model.model")
        xgb_model = pickle.load(open("./data/models/xgb_model.model", "rb"))
        print("XGB model:\tdone")
    else:
        xgb_model = xgb.train(params=xgb_params,
                              dtrain=dmatrix_train,
                              evals=[(dmatrix_train, "train"), (dmatrix_test, "validation")],
                              num_boost_round=50000
                              #early_stopping_rounds=20)
                              )

        # xgb_model.save_model("./data/models/xgb_model.model")
        pickle.dump(xgb_model, open("./data/models/xgb_model.model", "wb"))

    xgb_preds = xgb_model.predict(dmatrix_test)
    r2 = r2_score(y_test, xgb_preds)

    print("Best r2: ", r2)
