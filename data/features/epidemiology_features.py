class EpidemiologyFeatures:

    @staticmethod
    def growth_rate(
        df,
        cases_column="cases"
    ):

        df["growth_rate"] = (
            df[cases_column]
            .pct_change()
        )

        return df

    @staticmethod
    def moving_average(
        df,
        cases_column="cases",
        window=7
    ):

        df["cases_ma"] = (
            df[cases_column]
            .rolling(window)
            .mean()
        )

        return df