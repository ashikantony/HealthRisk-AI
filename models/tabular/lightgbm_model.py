from lightgbm import (
    LGBMClassifier,
    LGBMRegressor
)


class LightGBMModel:

    def __init__(
        self,
        task="classification",
        **kwargs
    ):

        self.task = task

        if task == "classification":

            self.model = LGBMClassifier(
                n_estimators=500,
                learning_rate=0.05,
                max_depth=10,
                num_leaves=64,
                random_state=42,
                **kwargs
            )

        else:

            self.model = LGBMRegressor(
                n_estimators=500,
                learning_rate=0.05,
                max_depth=10,
                num_leaves=64,
                random_state=42,
                **kwargs
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