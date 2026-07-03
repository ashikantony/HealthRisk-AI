import joblib

from sklearn.model_selection import (
    train_test_split
)

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


class TabularTrainer:

    def __init__(
        self,
        model,
        task="classification"
    ):
        self.model = model
        self.task = task

    def split_data(
        self,
        X,
        y,
        test_size=0.20
    ):

        return train_test_split(
            X,
            y,
            test_size=test_size,
            random_state=42,
            stratify=y
            if self.task ==
            "classification"
            else None
        )

    def train(
        self,
        X_train,
        y_train
    ):

        self.model.fit(
            X_train,
            y_train
        )

    def evaluate(
        self,
        X_test,
        y_test
    ):

        predictions = (
            self.model.predict(
                X_test
            )
        )

        if (
            self.task
            ==
            "classification"
        ):

            results = {
                "accuracy":
                    accuracy_score(
                        y_test,
                        predictions
                    ),
                "precision":
                    precision_score(
                        y_test,
                        predictions,
                        average="weighted",
                        zero_division=0
                    ),
                "recall":
                    recall_score(
                        y_test,
                        predictions,
                        average="weighted",
                        zero_division=0
                    ),
                "f1":
                    f1_score(
                        y_test,
                        predictions,
                        average="weighted",
                        zero_division=0
                    )
            }

            try:

                probabilities = (
                    self.model
                    .predict_proba(
                        X_test
                    )
                )[:, 1]

                results[
                    "roc_auc"
                ] = (
                    roc_auc_score(
                        y_test,
                        probabilities
                    )
                )

            except Exception:
                pass

            return results

        else:

            return {
                "mae":
                    mean_absolute_error(
                        y_test,
                        predictions
                    ),
                "mse":
                    mean_squared_error(
                        y_test,
                        predictions
                    ),
                "rmse":
                    mean_squared_error(
                        y_test,
                        predictions,
                        squared=False
                    ),
                "r2":
                    r2_score(
                        y_test,
                        predictions
                    )
            }

    def save_model(
        self,
        filepath
    ):
        joblib.dump(
            self.model,
            filepath
        )

    @staticmethod
    def load_model(
        filepath
    ):
        return joblib.load(
            filepath
        )