from sklearn.tree import export_graphviz
from sklearn import tree

import os

from IPython.display import Image
import graphviz
import matplotlib.pyplot as plt


def plot_tree(tree, feature_names, max_depth=5):
    '''
    receives nth tree inside model: estimators_[n]
    and feature names: X_train.columns
    display graph of this tree 
    '''
    dot_data = export_graphviz(tree, feature_names=feature_names, filled=True, max_depth=5, impurity=False, proportion=True)
    graph = graphviz.Source(dot_data)
    display(graph)


def plot_trees(rf, feature_names, nrows=2, ncols=3, savename=False):

    if nrows<2:
        print("nrows must be at least 2")
        nrows = 2

    figsize = (ncols*4, nrows*2)

    dpi = min(3000, ncols*nrows*300)

    fig,axes=plt.subplots(nrows=nrows,ncols=ncols,figsize=figsize,dpi=dpi)


    for row in range(nrows):
        for column in range(ncols):
            i = column+(ncols*row)

            tree.plot_tree(rf.estimators_[i], feature_names=feature_names, filled=True, ax=axes[row,column])
            axes[row,column].set_title('Estimator: ' + str(i), fontsize = 11)

    if savename :
        parent_abs = os.path.abspath(os.path.join(os.getcwd(),os.pardir))
        relative_path = r'reports'

        if not savename.endswith(".png"):
            savename += '.png'

        path = os.path.join(parent_abs, relative_path, savename)
        fig.savefig(path)

    plt.show()   