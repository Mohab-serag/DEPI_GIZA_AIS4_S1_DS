import pandas as pd

def chk_types(df):
    dtype = df.dtypes
    n_uniq = df.nunique()
    
    return pd.DataFrame({
        "Dtypes": dtype,
        "Num_unique": n_uniq
    }).T