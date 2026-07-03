import pandas as pd
from sklearn.preprocessing import (
    LabelEncoder,
    OneHotEncoder
)


class DataEncoder:

    def __init__(self):

        self.label_encoders = {}

    def label_encode(
        self,
        df,
        columns
    ):

        for column in columns:

            encoder = LabelEncoder()

            df[column] = encoder.fit_transform(
                df[column].astype(str)
            )

            self.label_encoders[
                column
            ] = encoder

        return df

    def one_hot_encode(
        self,
        df,
        columns
    ):

        return pd.get_dummies(
            df,
            columns=columns,
            drop_first=True
        )