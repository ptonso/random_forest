import pandas as pd

def threshold_mapping(df, quantile=0.2, y_index=0, less_than=True):
    '''
    receive df, return df
    in y_column, return 1 if value is less than quantile, else 0
    if less_than = False, return values greater than quantile
    '''
    y_column = df.columns[y_index]
    quant_value = df[y_column].quantile(quantile)
    
    if less_than:
        df[y_column] = (df[y_column] < quant_value).astype(int)
    else:
        df[y_column] = (df[y_column] > quant_value).astype(int)
    return df