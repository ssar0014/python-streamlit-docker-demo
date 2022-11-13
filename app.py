import pandas as pd
import sklearn
from sklearn.metrics import r2_score
import json
import os
import streamlit as st
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score

train_df = pd.read_csv(os.path.join("./train.csv"))
test_df = pd.read_csv(os.path.join("./test.csv"))
val_df = pd.read_csv(os.path.join("./validation.csv"))

# TODO : implement a customizable train test split instead of reading in static files

st.write(f"# California Housing Classifier")
st.write(f"### Training Dataset: \n")
st.dataframe(train_df)

# load the model from disk
loaded_model = pickle.load(open(os.path.join("./model.pkl"), 'rb'))

# choose df
df_type = st.radio("Choose dataset to score metrics: ", ("Train", "test", "validation"))
if df_type == "Train":
    df = train_df
elif df_type == "test":
    df = test_df
else:
    df = val_df

x_values = df.iloc[:, :-1].values
y_values = df.iloc[:,-1].values

# scaler is trained on train_df
x_train = train_df.iloc[:, :-1].values
scaler = StandardScaler()
scaler.fit(x_train)

# normalize or not
normalize = st.checkbox('Normalize?')
if normalize:
    st.write(f'Metrics on Normalized {df_type} dataset:\n')
    x_scaled = scaler.transform(x_values)
    loaded_model = pickle.load(open(os.path.join("./model.pkl"), 'rb'))
    preds = loaded_model.predict(x_scaled)
    r2 = r2_score(y_values, preds)
    st.write(f"R2 score on Normalized {df_type}: {r2}")
else:
    st.write(f'Metrics on non-normalized {df_type} dataset:\n')
    loaded_model = pickle.load(open(os.path.join("./model.pkl"), 'rb'))
    preds = loaded_model.predict(x_values)
    r2 = r2_score(y_values, preds)
    st.write(f"R2 score on Normalized {df_type}: {r2}")


