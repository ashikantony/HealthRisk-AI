import pandas as pd


class MissingValueHandler:

    @staticmethod
    def mean_imputation(df):

        numeric_columns = df.select_dtypes(
            include="number"
        ).columns

        for column in numeric_columns:
            df[column] = (
                df[column]
                .fillna(df[column].mean())
            )

        return df

    @staticmethod
    def median_imputation(df):

        numeric_columns = df.select_dtypes(
            include="number"
        ).columns

        for column in numeric_columns:
            df[column] = (
                df[column]
                .fillna(df[column].median())
            )

        return df

    @staticmethod
    def mode_imputation(df):

        categorical_columns = (
            df.select_dtypes(
                include="object"
            ).columns
        )

        for column in categorical_columns:
            mode = df[column].mode()

            if len(mode) > 0:
                df[column] = (
                    df[column]
                    .fillna(mode[0])
                )

        return df