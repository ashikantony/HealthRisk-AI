import pandas as pd


class DataCleaner:

    @staticmethod
    def clean_column_names(df):

        df.columns = (
            df.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
        )

        return df

    @staticmethod
    def remove_whitespace(df):

        object_columns = df.select_dtypes(
            include="object"
        ).columns

        for column in object_columns:
            df[column] = (
                df[column]
                .astype(str)
                .str.strip()
            )

        return df

    @staticmethod
    def convert_dtypes(df):

        return df.convert_dtypes()

    @staticmethod
    def drop_empty_rows(df):

        return df.dropna(how="all")

    @staticmethod
    def clean(df):

        df = DataCleaner.clean_column_names(df)
        df = DataCleaner.remove_whitespace(df)
        df = DataCleaner.convert_dtypes(df)
        df = DataCleaner.drop_empty_rows(df)

        return df