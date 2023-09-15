import os
import pickle

def get_parents():
    abs_path = os.path.dirname(os.getcwd())
    return abs_path

def save_df(df, filename):
    abs_path = get_parents()
    rel_path = "\\data\\" + filename
    
    path = abs_path + rel_path
    df.to_csv(path)
    print("csv file saved on: ", path)


def save_model(model, filename):
    abs_path = get_parents()
    rel_path = "\\models\\" + filename

    path = abs_path + rel_path
    pickle.dump(model, open(path, 'wb'))
    print("model saved created on: ", path)