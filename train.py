import sklearn
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import StandardScaler
import os
import pandas as pd
import pickle

train_df = pd.read_csv(os.path.join("./train.csv"))
test_df = pd.read_csv(os.path.join("./test.csv"))
val_df = pd.read_csv(os.path.join("./validation.csv"))

x_train = train_df.iloc[:, :-1].values
y_train = train_df.iloc[:,-1].values

x_val = val_df.iloc[:, :-1].values
y_val = val_df.iloc[:,-1].values

x_test = test_df.iloc[:, :-1].values
y_test = test_df.iloc[:,-1].values

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_val_scaled = scaler.transform(x_val)
x_test_scaled = scaler.transform(x_test)

clf = DecisionTreeRegressor()
clf.fit(x_train_scaled, y_train)

filename = 'model.pkl'
pickle.dump(clf, open(filename, 'wb'))