import random


class ShockGenerator:

    SHOCKS = [
        "pandemic",
        "drug_failure",
        "hospital_default",
        "insurance_claim_spike",
        "regulatory_change",
        "supply_chain_disruption"
    ]

    def generate_shock(self):

        return random.choice(
            self.SHOCKS
        )

    def shock_impact(
        self,
        shock
    ):

        impacts = {

            "pandemic": -0.25,
            "drug_failure": -0.15,
            "hospital_default": -0.20,
            "insurance_claim_spike": -0.18,
            "regulatory_change": -0.10,
            "supply_chain_disruption": -0.12
        }

        return impacts.get(
            shock,
            0
        )