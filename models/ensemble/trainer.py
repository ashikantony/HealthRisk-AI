import joblib
import numpy as np
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    mean_squared_error,
    r2_score
)


class EnsembleTrainer:

    def __init__(
        self,
        ensemble,
        task="classification"
    ):

        self.ensemble = ensemble
        self.task = task

    def train(
        self,
        X_train,
        y_train
    ):

        self.ensemble.fit(
            X_train,
            y_train
        )

    def evaluate(
        self,
        X_test,
        y_test
    ):

        predictions = (
            self.ensemble.predict(
                X_test
            )
        )

        if (
            self.task
            ==
            "classification"
        ):

            return {
                "accuracy":
                    accuracy_score(
                        y_test,
                        predictions
                    ),
                "f1_score":
                    f1_score(
                        y_test,
                        predictions,
                        average="weighted"
                    )
            }

        return {
            "mse":
                mean_squared_error(
                    y_test,
                    predictions
                ),
            "r2":
                r2_score(
                    y_test,
                    predictions
                )
        }

    def save(
        self,
        filepath
    ):
        joblib.dump(
            self.ensemble,
            filepath
        )

    @staticmethod
    def load(
        filepath
    ):
        return joblib.load(
            filepath
        )