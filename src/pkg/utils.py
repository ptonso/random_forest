import os
import pickle

def get_parents():
    abs_path = os.path.dirname(os.getcwd())
    return abs_path

def get_path(parent, filename):
    path = os.path.join(get_parents(),parent,filename)
    return path

def save_df(df, filename):
    path = get_path('data', filename)
    df.to_csv(path)
    print("csv file saved on: ", path)

def read_model(filename):
    path = get_path('models', filename)
    # t = open(path,'wb')
    
    model = pickle.load(open(path, 'rb'))
    return model


def save_model(model, filename):
    '''
    e.g. inputs
    model = rf # RandomForestClassifier
    filename = "v01.pkl"
    '''
    path = get_path('models', filename)

    if os.path.exists(path):
        open(path, 'x')

    with open(path, 'wb') as f:
        pickle.dump(model, f)
    print("model saved on: ", path)