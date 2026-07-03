import torch

from models.survival.deepsurv import (
    DeepSurv
)


def test_deepsurv():

    model = DeepSurv(
        input_dim=20
    )

    x = torch.rand(
        32,
        20
    )

    output = model(x)

    assert output.shape == (
        32,
        1
    )