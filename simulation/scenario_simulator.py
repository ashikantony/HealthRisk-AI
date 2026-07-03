class ScenarioSimulator:

    def __init__(
        self,
        portfolio_manager,
        shock_generator
    ):

        self.portfolio = (
            portfolio_manager
        )

        self.shocks = (
            shock_generator
        )

    def simulate(
        self,
        market_prices
    ):

        shock = (
            self.shocks
            .generate_shock()
        )

        impact = (
            self.shocks
            .shock_impact(
                shock
            )
        )

        adjusted_prices = {}

        for asset, price in (
            market_prices.items()
        ):

            adjusted_prices[
                asset
            ] = (
                price
                *
                (
                    1
                    +
                    impact
                )
            )

        value = (
            self.portfolio
            .portfolio_value(
                adjusted_prices
            )
        )

        return {
            "shock":
                shock,
            "impact":
                impact,
            "portfolio_value":
                value
        }