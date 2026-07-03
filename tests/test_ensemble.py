import numpy as np

from models.ensemble.weighted_ensemble import (
    WeightedEnsemble
)


def test_weighted_ensemble():

    predictions = [
        np.array([1, 0, 1]),
        np.array([1, 1, 0]),
        np.array([1, 0, 0])
    ]

    ensemble = (
        WeightedEnsemble()
    )

    result = ensemble.predict(
        predictions
    )

    assert len(result) == 3