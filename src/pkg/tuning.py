import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_rf(X_train:pd.DataFrame, y_train:pd.Series, random_state=123, max_depth=10):
    
    accuracy=None
    rf = RandomForestClassifier(max_depth=max_depth, random_state=random_state)
    rf.fit(X_train, y_train)
    
    if X_test and y_test:
        y_hat = rf.predict(X_test)
        accuracy = accuracy_score(y_test, y_hat)
        print("Accuracy:", accuracy)

    if accuracy:
        return rf, accuracy
    return rf


def k_fold(k=int, df, random_state=123):
    '''
    k is number of partitions
    '''
    seed = RandomState(random_state)
    n = df.shape[0]
    partitions_df = partition_df(k, df)

    for i, partition in enumerate(partitions_df):
        p = k/n
        msk = seed.rand(n) < p
    
        test = df[msk]
        train = df[~msk]

        
    return train, test

def find_gamma(df, min=20, max=100):
    
    opt_gamma = 0
    gammas_acc = []

    for gamma in range(min, max):

        gammas.append(gamma)
        accuracy = acc_test_gamma(df, gamma:int, min=min, max=max)
        gamma_acc.append([accuracy])

    gamma_index = gamma_acc.index(max(gamma_acc))

    return gamma[gamma_index]


def binning():
    return binned_df


def acc_test_gamma(df, gamma:int, min=20, max=100):

    binned_df = binning(df, gamma)
    X_train, X_test, y_train, y_test = split(df)
    rf, accuracy = tuning.train_rf(X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test, 
                                    max_depth=trees_max_depth, random_state=seed)
    
    return accuracy    
