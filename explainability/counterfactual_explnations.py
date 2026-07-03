import pandas as pd
import numpy as np


class CounterfactualGenerator:

    def __init__(
        self,
        model,
        feature_names
    ):

        self.model = model
        self.feature_names = feature_names

    def generate(
        self,
        instance,
        target_class=1,
        step_size=0.05
    ):

        original_prediction = (
            self.model.predict(
                [instance]
            )[0]
        )

        modified = instance.copy()

        for idx in range(
            len(instance)
        ):

            temp = modified.copy()

            temp[idx] += step_size

            prediction = (
                self.model.predict(
                    [temp]
                )[0]
            )

            if prediction == target_class:

                return {
                    "original_prediction":
                        original_prediction,
                    "counterfactual":
                        temp,
                    "changed_feature":
                        self.feature_names[
                            idx
                        ]
                }

        return None

    def compare(
        self,
        original,
        counterfactual
    ):

        return pd.DataFrame({

            "Feature":
                self.feature_names,

            "Original":
                original,

            "Counterfactual":
                counterfactual
        })