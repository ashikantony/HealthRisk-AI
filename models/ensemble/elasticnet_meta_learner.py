from sklearn.linear_model import (
    ElasticNet
)


class ElasticNetMetaLearner:

    def __init__(
        self,
        alpha=1.0,
        l1_ratio=0.50
    ):

        self.model = ElasticNet(
            alpha=alpha,
            l1_ratio=l1_ratio,
            random_state=42
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