import numpy as np


class InferenceEngine:

    def __init__(
        self,
        models
    ):
        self.models = models

    def predict(
        self,
        X
    ):

        predictions = {}

        for name, model in (
            self.models.items()
        ):

            predictions[name] = (
                model.predict(X)
            )

        return predictions

    def ensemble_prediction(
        self,
        X,
        weights=None
    ):

        outputs = self.predict(X)

        predictions = list(
            outputs.values()
        )

        predictions = np.array(
            predictions
        )

        if weights is None:

            weights = (
                np.ones(
                    predictions.shape[0]
                )
                /
                predictions.shape[0]
            )

        final_prediction = (
            np.average(
                predictions,
                axis=0,
                weights=weights
            )
        )

        return final_prediction