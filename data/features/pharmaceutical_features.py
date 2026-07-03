class PharmaceuticalFeatures:

    @staticmethod
    def pipeline_success_score(df):

        df["pipeline_success_score"] = (
            (
                df["phase1_success"]
                +
                df["phase2_success"]
                +
                df["phase3_success"]
            )
            / 3
        )

        return df

    @staticmethod
    def adverse_event_rate(df):

        df["adverse_event_rate"] = (
            df["adverse_events"]
            /
            df["patients"]
        )

        return df