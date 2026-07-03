class LaboratoryFeatures:

    @staticmethod
    def laboratory_risk_score(
        df,
        laboratory_columns
    ):

        df["laboratory_risk_score"] = (
            df[laboratory_columns]
            .sum(axis=1)
        )

        return df

    @staticmethod
    def abnormal_lab_count(
        df,
        abnormal_columns
    ):

        df["abnormal_lab_count"] = (
            df[abnormal_columns]
            .sum(axis=1)
        )

        return df