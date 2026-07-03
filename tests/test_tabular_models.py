from sklearn.datasets import (
    make_classification
)

from models.tabular.random_forest import (
    RandomForestModel
)


def test_random_forest():

    X, y = make_classification(
        n_samples=100,
        n_features=10,
        random_state=42
    )

    model = RandomForestModel()

    model.fit(X, y)

    predictions = model.predict(
        X
    )

    assert len(
        predictions
    ) == len(y)