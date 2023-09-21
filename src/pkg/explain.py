from sklearn.tree import _tree
import pandas as pd

def find_rules(tree, features):
    dt = tree.tree_
    rules = []
    def visitor(node, depth, rule):
        if dt.feature[node] != _tree.TREE_UNDEFINED:

            rule.append((features[node], dt.threshold[node]))
            visitor(dt.children_left[node], depth + 1, rule.copy())
            rule.pop()
            rule.append(('not ' + features[node], dt.threshold[node]))
            visitor(dt.children_right[node], depth + 1, rule.copy())
            rule.pop()
        else:
            rules.append(rule.copy())
    visitor(0, 1, [])
    return rules


def binning_serie(feature, bins=10):
    key = feature.name
    values = []
    q = 1/bins

    for b in range(1,bins+1):
        value = feature.quantile(b*q)
        values.append(value)

    return key, values


def binning_df(X, bins=10):
    bin_dict = {}
    
    for column in X:
        key, values = binning_serie(X[column],bins=bins)
        bin_dict[key] = values
    
    bin_df = pd.DataFrame.from_dict(bin_dict)

    return bin_df