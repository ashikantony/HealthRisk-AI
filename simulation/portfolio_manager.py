class PortfolioManager:

    def __init__(self):

        self.cash = 1_000_000
        self.positions = {}

    def buy(
        self,
        asset,
        price,
        quantity
    ):

        cost = price * quantity

        if cost > self.cash:
            raise ValueError(
                "Insufficient funds."
            )

        self.cash -= cost

        self.positions[asset] = (
            self.positions.get(
                asset,
                0
            )
            + quantity
        )

    def sell(
        self,
        asset,
        price,
        quantity
    ):

        current = (
            self.positions.get(
                asset,
                0
            )
        )

        if quantity > current:
            raise ValueError(
                "Insufficient holdings."
            )

        self.positions[asset] -= quantity
        self.cash += (
            price * quantity
        )

    def portfolio_value(
        self,
        prices
    ):

        total = self.cash

        for asset, quantity in (
            self.positions.items()
        ):

            total += (
                quantity
                *
                prices.get(
                    asset,
                    0
                )
            )

        return total