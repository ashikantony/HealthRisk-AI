class InsuranceFeatures:

    @staticmethod
    def claim_ratio(df):

        df["claim_ratio"] = (
            df["claims_paid"] /
            df["premium_collected"]
        )

        return df

    @staticmethod
    def high_claimant(df):

        df["high_claimant"] = (
            df["claim_ratio"] > 0.80
        ).astype(int)

        return df