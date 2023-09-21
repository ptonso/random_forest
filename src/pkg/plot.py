import os

import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d
import graphviz
from IPython.display import Image


from sklearn.tree import export_graphviz
from sklearn import tree as sktree
from sklearn import decomposition
from sklearn.manifold import TSNE

# Util

plt.style.use('ggplot')

def save(savename, saving_function):
    parent_abs = os.path.abspath(os.path.join(os.getcwd(),os.pardir))
    parent = 'reports'
    path = os.path.join(parent_abs, parent, savename)
    
    saving_function(path)
    
    print('figure saved on ', path)
# 
# _____________________________
# 
# Feature visualization


def pca_2d(X, savename=False):
    '''
    receives X features
    return plot of 2 components pca
    '''
    fig = plt.figure(figsize=(10,10))

    pca = decomposition.PCA(n_components=3)
    view = pca.fit_transform(X)

    plt.scatter(view[:,0], view[:,1], c=view[:,2])
    plt.xlabel('PCA-1')
    plt.ylabel('PCA-2')

    if savename :
        save(savename, fig.savefig)

    plt.show()


def pca_3d(X, multiple_graph=False, savename=False):
    '''
    plot a 3 components pca
    if multiple_graph: more 3 2d combinations        
    '''

    pca = decomposition.PCA(n_components=4)
    view = pca.fit_transform(X)

    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(221, projection='3d')
    alpha = 0.4

    if not multiple_graph:

        ax.scatter(view[:,0], view[:,1], view[:,2], c=view[:,3], alpha=alpha)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')

        plt.show()

    if multiple_graph:

        ax.scatter(view[:,0], view[:,1], view[:,2], c=view[:,3], alpha=alpha)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')

        ax = fig.add_subplot(222)
        ax.scatter(view[:,0], view[:,1], c=view[:,2], alpha=alpha)
        ax.set_xlabel('y')
        ax.set_ylabel('z')

        ax = fig.add_subplot(223)
        ax.scatter(view[:,0], view[:,2], c=view[:,1], alpha=alpha)
        ax.set_xlabel('x')
        ax.set_ylabel('z')

        ax = fig.add_subplot(224)
        ax.scatter(view[:,1], view[:,2], c=view[:,3], alpha=alpha)
        ax.set_xlabel('x')
        ax.set_ylabel('y')

    if savename :
        save(savename, fig.savefig)

    plt.show()


def t_sne(X, savename=False):
    '''
    plot two component t_SNE
    '''
    view = TSNE(n_components=2, random_state=123).fit_transform(X)
    fig = plt.figure(figsize=(10,10))
    plt.scatter(view[:,0], view[:,1], alpha=0.5)
    plt.xlabel('t-SNE-1')
    plt.ylabel('t-SNE-2')

    if savename :
        save(savename, fig.savefig)

    plt.show()

# 
# _____________________________
# 
# Model visualization

## Decision Tree

def tree(tree, feature_names, max_depth=5, savename=False):
    '''
    receives nth tree inside model: estimators_[n]
    and feature names: X_train.columns
    display graph of this tree 
    '''
    dot_data = export_graphviz(tree, feature_names=feature_names, filled=True, max_depth=5, impurity=False, proportion=True)
    graph = graphviz.Source(dot_data, format='png')
    display(graph)

    if savename :
        save(savename, graph.render)

# Multiple trees
def trees(rf, feature_names, nrows=2, ncols=3, savename=False):
    '''
    Decide size of output nrows x ncols = m
    plot first m decision trees inside rf
    in different subplots    
    '''

    if nrows<2:
        print("nrows must be at least 2")
        pass

    figsize = (ncols*4, nrows*2)

    dpi = min(1200, ncols*nrows*300)
    
    fig,axes=plt.subplots(nrows=nrows,ncols=ncols,figsize=figsize,dpi=dpi)


    for row in range(nrows):
        for column in range(ncols):
            

            i = column+(ncols*row) # Conferido
            dt = rf.estimators_[i]
            feature_names = [f'Feature {i}' for i in range(len(dt.feature_importances_))]

            sktree.plot_tree(dt, feature_names=feature_names, filled=True, ax=axes[row,column])
            axes[row,column].set_title('Estimator: ' + str(i), fontsize = 11)

    if savename :
        save(savename, fig.savefig)

    plt.show()