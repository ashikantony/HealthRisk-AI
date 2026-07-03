from lime.lime_tabular import (
    LimeTabularExplainer
)

import pandas as pd


class LIMEAnalyzer:

    def __init__(
        self,
        model,
        training_data,
        feature_names
    ):

        self.model = model

        self.explainer = (
            LimeTabularExplainer(
                training_data,
                feature_names=feature_names,
                mode="classification"
            )
        )

    def explain_instance(
        self,
        instance
    ):

        explanation = (
            self.explainer
            .explain_instance(
                instance,
                self.model.predict_proba
            )
        )

        return explanation

    def as_dataframe(
        self,
        explanation
    ):

        return pd.DataFrame(
            explanation.as_list(),
            columns=[
                "Feature",
                "Contribution"
            ]
        )