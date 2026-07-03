class ESGFeatures:

    @staticmethod
    def environmental_score(df):

        df["environment_score"] = (
            100
            -
            df["carbon_emission"]
        )

        return df

    @staticmethod
    def social_score(df):

        df["social_score"] = (
            df["community_benefit"]
            +
            df["patient_satisfaction"]
        ) / 2

        return df

    @staticmethod
    def governance_score(df):

        df["governance_score"] = (
            df["board_independence"]
            +
            df["compliance_score"]
        ) / 2

        return df

    @staticmethod
    def esg_score(df):

        df["esg_score"] = (
            df[
                [
                    "environment_score",
                    "social_score",
                    "governance_score"
                ]
            ]
            .mean(axis=1)
        )

        return df