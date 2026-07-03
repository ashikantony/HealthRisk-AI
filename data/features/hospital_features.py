class HospitalFeatures:

    @staticmethod
    def operating_margin(df):

        df["operating_margin"] = (
            (
                df["revenue"]
                -
                df["expense"]
            )
            /
            df["revenue"]
        )

        return df

    @staticmethod
    def occupancy_rate(df):

        df["occupancy_rate"] = (
            df["occupied_beds"]
            /
            df["total_beds"]
        )

        return df