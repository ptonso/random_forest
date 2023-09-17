import numpy as np
import pandas as pd

def extract_first_n_groups(input_string:str, n:int):
    '''
    take string separed with "|"
    return first n elements
    '''

    groups = input_string.split("|")
    
    result = "|".join(groups[:n])

    return result


def group_columns_startswith(old_df,new_columns):

    index = old_df.index
    new_dict = {index.name:index}

    for new_column in new_columns:
        column_names = [i for i in old_df.columns if i.startswith(new_column)]
        new_dict[new_column] = list(old_df[column_names].sum(axis=1))

    new_df = pd.DataFrame.from_dict(new_dict)
    new_df = new_df.set_index(index.name)
    return new_df