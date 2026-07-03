class DiagnosisFeatures:

    @staticmethod
    def diagnosis_count(
        df,
        diagnosis_columns
    ):

        df["diagnosis_count"] = (
            df[diagnosis_columns]
            .notna()
            .sum(axis=1)
        )

        return df

    @staticmethod
    def chronic_risk_score(
        df,
        chronic_columns
    ):

        df["chronic_risk_score"] = (
            df[chronic_columns]
            .sum(axis=1)
        )

        return df