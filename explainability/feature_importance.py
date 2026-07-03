import pandas as pd
import numpy as np


class FeatureImportanceAnalyzer:

    def __init__(
        self,
        model,
        feature_names
    ):

        self.model = model
        self.feature_names = feature_names

    def get_importance(self):

        if hasattr(
            self.model,
            "feature_importances_"
        ):

            scores = (
                self.model
                .feature_importances_
            )

        elif hasattr(
            self.model,
            "coef_"
        ):

            scores = np.abs(
                self.model.coef_
            ).flatten()

        else:

            raise ValueError(
                "Model does not support "
                "feature importance."
            )

        return pd.DataFrame({
            "feature":
                self.feature_names,
            "importance":
                scores
        }).sort_values(
            "importance",
            ascending=False
        )

    def top_features(
        self,
        top_n=20
    ):

        return (
            self.get_importance()
            .head(top_n)
        )