import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d

from sklearn import decomposition
from sklearn.manifold import TSNE


def pca_2d(df, y):

    pca = decomposition.PCA(n_components=2)
    view = pca.fit_transform(df)

    plt.scatter(view[:,0], view[:,1],c=y)
    plt.xlabel('PCA-1')
    plt.ylabel('PCA-2')

    plt.show()


def pca_3d(df, y, multiple_graph=False):

    pca = decomposition.PCA(n_components=3)
    view = pca.fit_transform(df)

    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(221, projection='3d')
    alpha = 0.4

    if not multiple_graph:

        ax.scatter(view[:,0], view[:,1], view[:,2],c=y, alpha=alpha)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')

        plt.show()

    if multiple_graph:

        ax.scatter(view[:,0], view[:,1], view[:,2],c=y, alpha=alpha)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')

        ax = fig.add_subplot(222)
        ax.scatter(view[:,0], view[:,1],c=y, alpha=alpha)
        ax.set_xlabel('y')
        ax.set_ylabel('z')

        ax = fig.add_subplot(223)
        ax.scatter(view[:,0], view[:,2],c=y, alpha=alpha)
        ax.set_xlabel('x')
        ax.set_ylabel('z')

        ax = fig.add_subplot(224)
        ax.scatter(view[:,1], view[:,2],c=y, alpha=alpha)
        ax.set_xlabel('x')
        ax.set_ylabel('y')


def t_sne(df):
    view = TSNE(n_components=2, random_state=123).fit_transform(df)
    plt.figure(figsize=(20,10))
    plt.scatter(view[:,0], view[:,1], alpha=0.5)
    plt.xlabel('t-SNE-1')
    plt.ylabel('t-SNE-2')

    plt.show()