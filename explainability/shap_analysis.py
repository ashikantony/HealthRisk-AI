import shap
import pandas as pd
import matplotlib.pyplot as plt


class SHAPAnalyzer:

    def __init__(self, model):

        self.model = model
        self.explainer = None
        self.shap_values = None

    def fit(self, X):

        self.explainer = shap.Explainer(
            self.model.predict,
            X
        )

        self.shap_values = self.explainer(X)

        return self.shap_values

    def summary_plot(self):

        shap.summary_plot(
            self.shap_values,
            show=False
        )

        plt.tight_layout()

        return plt.gcf()

    def waterfall_plot(
        self,
        sample_index=0
    ):

        shap.plots.waterfall(
            self.shap_values[
                sample_index
            ],
            show=False
        )

        return plt.gcf()

    def force_plot(
        self,
        sample_index=0
    ):

        return shap.force_plot(
            self.explainer.expected_value,
            self.shap_values[
                sample_index
            ]
        )

    def get_feature_impacts(self):

        return pd.DataFrame({
            "feature":
                self.shap_values.feature_names,
            "importance":
                abs(
                    self.shap_values.values
                ).mean(axis=0)
        }).sort_values(
            "importance",
            ascending=False
        )