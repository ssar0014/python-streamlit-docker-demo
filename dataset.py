import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn import datasets

if __name__ == "__main__":
    data = datasets.fetch_california_housing()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    target_label = data.target_names[0]
    target_vals = data.target
    df[target_label] = target_vals

    train_df, test_df = train_test_split(df, test_size=0.3, shuffle=True, random_state=42)
    train_df, val_df = train_test_split(train_df, test_size=0.2, shuffle=True, random_state=42)
    
    train_df.to_csv("./train.csv", index=False)
    test_df.to_csv("./test.csv", index=False)
    val_df.to_csv("./validation.csv", index=False)
    