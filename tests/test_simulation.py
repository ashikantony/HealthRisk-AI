from simulation.simulation_engine import (
    SimulationEngine
)


def test_simulation_round():

    engine = (
        SimulationEngine()
    )

    prices = {
        "Pfizer": 100,
        "Moderna": 120
    }

    result = (
        engine.play_round(
            prices,
            "player1"
        )
    )

    assert (
        "reward"
        in result
    )

    assert (
        "score"
        in result
    )