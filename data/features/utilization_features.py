class UtilizationFeatures:

    @staticmethod
    def hospital_visit_count(
        df,
        visit_columns
    ):

        df["hospital_visit_count"] = (
            df[visit_columns]
            .sum(axis=1)
        )

        return df

    @staticmethod
    def high_utilizer_flag(df):

        df["high_utilizer"] = (
            df["hospital_visit_count"] >= 3
        ).astype(int)

        return df