from xgboost import (
    XGBClassifier,
    XGBRegressor
)


class XGBoostModel:

    def __init__(
        self,
        task="classification",
        **kwargs
    ):
        self.task = task

        if task == "classification":
            self.model = XGBClassifier(
                n_estimators=500,
                max_depth=8,
                learning_rate=0.05,
                subsample=0.80,
                colsample_bytree=0.80,
                random_state=42,
                **kwargs
            )

        else:
            self.model = XGBRegressor(
                n_estimators=500,
                max_depth=8,
                learning_rate=0.05,
                subsample=0.80,
                colsample_bytree=0.80,
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
            "Probability prediction "
            "available only for "
            "classification."
        )

    def feature_importance(self):
        return self.model.feature_importances_