import pandas as pd

def threshold_mapping(y, quantile=0.2, less_than=True):
    '''
    y continuous series, return y bool series
    in y_column, return 1 if value is less than quantile, else 0
    if less_than = False, return values greater than quantile
    '''
    quant_value = y.quantile(quantile)
    
    if less_than:
        y = (y < quant_value).astype(int)
    else:
        y = (y > quant_value).astype(int)
    return y


