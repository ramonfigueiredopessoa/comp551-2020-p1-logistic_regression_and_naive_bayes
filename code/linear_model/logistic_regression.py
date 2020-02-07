import numpy as np


# TODO: Add regularization
class LogisticRegression:
    def __init__(self, lr=.01, eps=1e-2):
        self.lr = lr
        self.eps = eps
        self.w = np.zeros(0)

    # Logistic function (sigmoid)
    def logistic(self, z):
        return 1 / (1 + np.exp(-z))

    # Calculates de gradient over the whole dataset (full-batch)
    def gradient(self, X, y):
        yh = self.logistic(np.dot(X, self.w))
        grad = np.dot(X.T, yh - y)
        return grad

    # Uses full-batch gradient descent to fit the model to the data provided
    def fit(self, X, y):
        N, D = X.shape
        self.w = np.zeros(D)
        g = np.inf
        while np.linalg.norm(g) > self.eps:
            g = self.gradient(X, y)
            self.w = self.w - self.lr * g

    # Returns the model prediction over a set of data points
    def predict(self, x_test):
        return self.logistic(np.dot(x_test, self.w))

    def cost(self, X, y):
        z = np.dot(X, self.w)
        J = np.mean(y * np.log1p(np.exp(-z)) + (1 - y) * np.log1p(np.exp(z)))
        return J
