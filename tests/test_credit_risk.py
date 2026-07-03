from sklearn.datasets import (
    make_classification
)

from lightgbm import (
    LGBMClassifier
)


def test_credit_model():

    X, y = make_classification(
        n_samples=200,
        n_features=12,
        random_state=42
    )

    model = LGBMClassifier()

    model.fit(X, y)

    score = model.score(
        X,
        y
    )

    assert score > 0.70