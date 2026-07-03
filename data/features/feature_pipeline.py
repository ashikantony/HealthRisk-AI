from .demographic_features import (
    DemographicFeatures
)
from .insurance_features import (
    InsuranceFeatures
)
from .hospital_features import (
    HospitalFeatures
)
from .pharmaceutical_features import (
    PharmaceuticalFeatures
)
from .esg_features import (
    ESGFeatures
)


class FeatureEngineeringPipeline:

    def run(self, df):

        print(
            "Starting Feature Engineering..."
        )

        if "age" in df.columns:
            df = (
                DemographicFeatures
                .age_group(df)
            )

        if (
            "claims_paid" in df.columns
            and
            "premium_collected"
            in df.columns
        ):
            df = (
                InsuranceFeatures
                .claim_ratio(df)
            )

        if (
            "revenue" in df.columns
            and
            "expense" in df.columns
        ):
            df = (
                HospitalFeatures
                .operating_margin(df)
            )

        if (
            "phase1_success"
            in df.columns
        ):
            df = (
                PharmaceuticalFeatures
                .pipeline_success_score(df)
            )

        if (
            "carbon_emission"
            in df.columns
        ):
            df = (
                ESGFeatures
                .environmental_score(df)
            )

        print(
            "Feature Engineering Completed."
        )

        return df