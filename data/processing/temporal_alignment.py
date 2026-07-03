import pandas as pd


class TemporalAligner:

    @staticmethod
    def convert_to_datetime(
        df,
        column
    ):

        df[column] = pd.to_datetime(
            df[column]
        )

        return df

    @staticmethod
    def sort_by_time(
        df,
        column
    ):

        return (
            df.sort_values(column)
            .reset_index(drop=True)
        )

    @staticmethod
    def resample_monthly(
        df,
        date_column
    ):

        df[date_column] = (
            pd.to_datetime(
                df[date_column]
            )
        )

        return (
            df
            .set_index(date_column)
            .resample("M")
            .mean(numeric_only=True)
            .reset_index()
        )