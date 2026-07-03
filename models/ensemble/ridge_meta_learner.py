from sklearn.linear_model import (
    Ridge
)


class RidgeMetaLearner:

    def __init__(
        self,
        alpha=1.0
    ):

        self.model = Ridge(
            alpha=alpha
        )

    def fit(
        self,
        X,
        y
    ):
        self.model.fit(X, y)

    def predict(
        self,
        X
    ):
        return self.model.predict(X)

    def coefficients(self):
        return self.model.coef_