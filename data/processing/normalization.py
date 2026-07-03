from sklearn.preprocessing import (
    StandardScaler,
    MinMaxScaler
)


class DataNormalizer:

    def __init__(self):

        self.standard_scaler = (
            StandardScaler()
        )

        self.minmax_scaler = (
            MinMaxScaler()
        )

    def standardize(
        self,
        df,
        columns
    ):

        df[columns] = (
            self.standard_scaler
            .fit_transform(df[columns])
        )

        return df

    def minmax_scale(
        self,
        df,
        columns
    ):

        df[columns] = (
            self.minmax_scaler
            .fit_transform(df[columns])
        )

        return df