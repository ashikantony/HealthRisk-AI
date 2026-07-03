class RewardSystem:

    def __init__(self):

        self.score = 0

    def calculate_reward(
        self,
        previous_value,
        current_value
    ):

        profit = (
            current_value
            -
            previous_value
        )

        reward = (
            profit / 1000
        )

        self.score += reward

        return reward

    def total_score(self):

        return self.score