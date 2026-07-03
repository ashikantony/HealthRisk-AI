import numpy as np


class WeightedEnsemble:

    def __init__(
        self,
        weights=None
    ):
        self.weights = weights

    def predict(
        self,
        predictions
    ):

        predictions = np.array(
            predictions
        )

        if self.weights is None:

            self.weights = (
                np.ones(
                    predictions.shape[0]
                )
                /
                predictions.shape[0]
            )

        ensemble_prediction = (
            np.average(
                predictions,
                axis=0,
                weights=self.weights
            )
        )

        return ensemble_prediction