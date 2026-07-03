from .portfolio_manager import (
    PortfolioManager
)
from .insurance_engine import (
    InsuranceEngine
)
from .shock_generator import (
    ShockGenerator
)
from .scenario_simulator import (
    ScenarioSimulator
)
from .reward_system import (
    RewardSystem
)
from .leaderboard import (
    Leaderboard
)


class SimulationEngine:

    def __init__(self):

        self.portfolio = (
            PortfolioManager()
        )

        self.insurance = (
            InsuranceEngine()
        )

        self.shocks = (
            ShockGenerator()
        )

        self.rewards = (
            RewardSystem()
        )

        self.leaderboard = (
            Leaderboard()
        )

        self.scenario = (
            ScenarioSimulator(
                self.portfolio,
                self.shocks
            )
        )

    def play_round(
        self,
        market_prices,
        player_name
    ):

        previous_value = (
            self.portfolio
            .portfolio_value(
                market_prices
            )
        )

        results = (
            self.scenario
            .simulate(
                market_prices
            )
        )

        current_value = (
            results[
                "portfolio_value"
            ]
        )

        reward = (
            self.rewards
            .calculate_reward(
                previous_value,
                current_value
            )
        )

        total_score = (
            self.rewards
            .total_score()
        )

        self.leaderboard.update(
            player_name,
            total_score
        )

        results[
            "reward"
        ] = reward

        results[
            "score"
        ] = total_score

        return results