from sklearn.linear_model import (
    LogisticRegression,
    LinearRegression
)


class LogisticRegressionModel:

    def __init__(
        self,
        task="classification"
    ):

        self.task = task

        if task == "classification":

            self.model = (
                LogisticRegression(
                    max_iter=500,
                    random_state=42
                )
            )

        else:

            self.model = (
                LinearRegression()
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

    def predict_proba(
        self,
        X
    ):
        if (
            self.task
            ==
            "classification"
        ):
            return (
                self.model
                .predict_proba(X)
            )

        raise ValueError(
            "Regression model "
            "does not support "
            "predict_proba()."
        )

    def coefficients(self):

        if hasattr(
            self.model,
            "coef_"
        ):
            return self.model.coef_

        return None