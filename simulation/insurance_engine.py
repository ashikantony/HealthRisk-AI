class InsuranceEngine:

    def __init__(self):

        self.policies = []

    def add_policy(
        self,
        policy_id,
        premium,
        expected_claim
    ):

        self.policies.append({
            "policy_id":
                policy_id,
            "premium":
                premium,
            "expected_claim":
                expected_claim
        })

    def total_premium(self):

        return sum(
            p["premium"]
            for p in self.policies
        )

    def expected_liability(self):

        return sum(
            p["expected_claim"]
            for p in self.policies
        )

    def risk_ratio(self):

        premium = (
            self.total_premium()
        )

        if premium == 0:
            return 0

        return (
            self.expected_liability()
            /
            premium
        )