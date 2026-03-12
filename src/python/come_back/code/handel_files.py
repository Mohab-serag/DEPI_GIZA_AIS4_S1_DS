import pandas as pd

def handel_dtype(df , cols):
    df[cols] = df[cols].astype('category')
    return pd.DataFrame(df.dtypes).T