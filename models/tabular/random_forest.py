from sklearn.ensemble import (
    RandomForestClassifier,
    RandomForestRegressor
)


class RandomForestModel:

    def __init__(
        self,
        task="classification",
        **kwargs
    ):

        self.task = task

        if task == "classification":

            self.model = (
                RandomForestClassifier(
                    n_estimators=300,
                    max_depth=15,
                    random_state=42,
                    n_jobs=-1,
                    **kwargs
                )
            )

        else:

            self.model = (
                RandomForestRegressor(
                    n_estimators=300,
                    max_depth=15,
                    random_state=42,
                    n_jobs=-1,
                    **kwargs
                )
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
        if self.task == "classification":
            return self.model.predict_proba(X)

        raise ValueError(
            "Regression models "
            "do not support "
            "predict_proba()."
        )

    def feature_importance(self):
        return self.model.feature_importances_