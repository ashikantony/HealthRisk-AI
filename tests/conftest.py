import pytest
import pandas as pd
import numpy as np


@pytest.fixture
def sample_dataframe():

    return pd.DataFrame({
        "age": [25, 40, 55, 60],
        "income": [50000, 70000, 80000, 100000],
        "claim_amount": [1000, 2000, 5000, 7000],
        "target": [0, 0, 1, 1]
    })


@pytest.fixture
def sample_features():

    return np.random.rand(
        100,
        10
    )


@pytest.fixture
def sample_labels():

    return np.random.randint(
        0,
        2,
        size=100
    )