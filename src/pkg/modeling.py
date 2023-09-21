
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def test_sup_model(X, y, model, seed=123):
    
    X_test, X_train, y_test, y_train = train_test_split(X, y, test_size=0.2, random_state=seed)

    model.fit(X_train, y_train)

    y_hat = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_hat)
    print(model.__class__.__name__, " - accuracy : ", accuracy)
    return accuracy

    # Other metrics:
    # ROC_AUC
    # Bal accuracy