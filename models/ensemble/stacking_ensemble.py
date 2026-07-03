import numpy as np
from sklearn.model_selection import KFold


class StackingEnsemble:

    def __init__(
        self,
        base_models,
        meta_model,
        n_folds=5
    ):
        self.base_models = base_models
        self.meta_model = meta_model
        self.n_folds = n_folds

    def fit(
        self,
        X,
        y
    ):

        kf = KFold(
            n_splits=self.n_folds,
            shuffle=True,
            random_state=42
        )

        meta_features = np.zeros(
            (
                X.shape[0],
                len(self.base_models)
            )
        )

        for index, model in enumerate(
            self.base_models
        ):

            fold_predictions = np.zeros(
                X.shape[0]
            )

            for train_idx, val_idx in kf.split(X):

                X_train = X.iloc[
                    train_idx
                ]

                y_train = y.iloc[
                    train_idx
                ]

                X_val = X.iloc[
                    val_idx
                ]

                model.fit(
                    X_train,
                    y_train
                )

                predictions = (
                    model.predict(
                        X_val
                    )
                )

                fold_predictions[
                    val_idx
                ] = predictions

            meta_features[:, index] = (
                fold_predictions
            )

        self.meta_model.fit(
            meta_features,
            y
        )

    def predict(self, X):

        meta_features = np.column_stack([
            model.predict(X)
            for model in self.base_models
        ])

        return self.meta_model.predict(
            meta_features
        )