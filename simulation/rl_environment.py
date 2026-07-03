import gym
from gym import spaces
import numpy as np


class HealthRiskEnvironment(
    gym.Env
):

    def __init__(self):

        super().__init__()

        self.action_space = (
            spaces.Discrete(3)
        )

        self.observation_space = (
            spaces.Box(
                low=-1,
                high=1,
                shape=(5,),
                dtype=np.float32
            )
        )

        self.state = np.zeros(
            5,
            dtype=np.float32
        )

        self.steps = 0

    def reset(self):

        self.steps = 0

        self.state = np.zeros(
            5,
            dtype=np.float32
        )

        return self.state

    def step(
        self,
        action
    ):

        reward = (
            np.random.normal(
                0,
                1
            )
        )

        self.state = (
            np.random.uniform(
                -1,
                1,
                5
            )
        )

        self.steps += 1

        done = (
            self.steps >= 100
        )

        return (
            self.state,
            reward,
            done,
            {}
        )

    def render(
        self,
        mode="human"
    ):

        print(
            f"State: {self.state}"
        )