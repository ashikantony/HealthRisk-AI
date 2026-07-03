from simulation.insurance_engine import (
    InsuranceEngine
)


def test_policy_creation():

    engine = InsuranceEngine()

    engine.add_policy(
        "P001",
        premium=500,
        expected_claim=200
    )

    assert (
        len(engine.policies)
        == 1
    )


def test_risk_ratio():

    engine = InsuranceEngine()

    engine.add_policy(
        "P001",
        1000,
        500
    )

    ratio = (
        engine.risk_ratio()
    )

    assert ratio == 0.5