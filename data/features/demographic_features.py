import pandas as pd


class DemographicFeatures:

    @staticmethod
    def age_group(df, age_column="age"):

        bins = [0, 18, 35, 50, 65, 120]
        labels = [
            "child",
            "young_adult",
            "adult",
            "middle_age",
            "senior"
        ]

        df["age_group"] = pd.cut(
            df[age_column],
            bins=bins,
            labels=labels
        )

        return df

    @staticmethod
    def encode_gender(
        df,
        gender_column="gender"
    ):

        mapping = {
            "M": 1,
            "F": 0
        }

        df["gender_encoded"] = (
            df[gender_column]
            .map(mapping)
        )

        return df