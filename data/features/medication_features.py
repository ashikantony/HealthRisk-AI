class MedicationFeatures:

    @staticmethod
    def medication_count(
        df,
        medication_columns
    ):

        df["medication_count"] = (
            df[medication_columns]
            .notna()
            .sum(axis=1)
        )

        return df

    @staticmethod
    def polypharmacy_flag(df):

        df["polypharmacy"] = (
            df["medication_count"] >= 5
        ).astype(int)

        return df