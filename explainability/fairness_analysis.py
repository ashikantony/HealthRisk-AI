import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix


class FairnessAnalyzer:

    def demographic_parity(
        self,
        predictions,
        sensitive_attribute
    ):

        groups = np.unique(
            sensitive_attribute
        )

        results = {}

        for group in groups:

            mask = (
                sensitive_attribute
                == group
            )

            results[group] = (
                predictions[
                    mask
                ].mean()
            )

        return results

    def equal_opportunity(
        self,
        y_true,
        y_pred,
        sensitive_attribute
    ):

        groups = np.unique(
            sensitive_attribute
        )

        results = {}

        for group in groups:

            mask = (
                sensitive_attribute
                == group
            )

            tn, fp, fn, tp = (
                confusion_matrix(
                    y_true[mask],
                    y_pred[mask]
                ).ravel()
            )

            tpr = tp / (
                tp + fn + 1e-8
            )

            results[group] = tpr

        return results

    def fairness_report(
        self,
        y_true,
        y_pred,
        sensitive_attribute
    ):

        return {

            "demographic_parity":
                self.demographic_parity(
                    y_pred,
                    sensitive_attribute
                ),

            "equal_opportunity":
                self.equal_opportunity(
                    y_true,
                    y_pred,
                    sensitive_attribute
                )
        }