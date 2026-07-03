from sklearn.datasets import (
    make_classification
)

from sklearn.ensemble import (
    RandomForestClassifier
)


def test_pharma_prediction():

    X, y = make_classification(
        n_samples=300,
        n_features=15,
        random_state=42
    )

    model = (
        RandomForestClassifier()
    )

    model.fit(X, y)

    predictions = model.predict(
        X
    )

    assert len(
        predictions
    ) == 300