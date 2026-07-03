from sklearn.datasets import (
    make_classification
)

from sklearn.ensemble import (
    RandomForestClassifier
)

from explainability.feature_importance import (
    FeatureImportanceAnalyzer
)


def test_feature_importance():

    X, y = make_classification(
        n_samples=100,
        n_features=10,
        random_state=42
    )

    model = (
        RandomForestClassifier()
    )

    model.fit(X, y)

    analyzer = (
        FeatureImportanceAnalyzer(
            model,
            [f"f{i}" for i in range(10)]
        )
    )

    importance = (
        analyzer.get_importance()
    )

    assert (
        len(importance)
        == 10
    )