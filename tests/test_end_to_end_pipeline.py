from sklearn.datasets import (
    make_classification
)

from models.tabular.xgboost_model import (
    XGBoostModel
)

from explainability.feature_importance import (
    FeatureImportanceAnalyzer
)


def test_end_to_end_pipeline():

    X, y = make_classification(
        n_samples=500,
        n_features=20,
        random_state=42
    )

    model = XGBoostModel()

    model.fit(X, y)

    predictions = model.predict(X)

    assert (
        len(predictions)
        == len(y)
    )

    analyzer = (
        FeatureImportanceAnalyzer(
            model.model,
            [f"f{i}" for i in range(20)]
        )
    )

    importance = (
        analyzer.get_importance()
    )

    assert (
        len(importance)
        == 20
    )