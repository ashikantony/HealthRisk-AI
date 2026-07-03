import torch
from models.graph_network.gnn_model import (
    HealthcareGNN
)


def test_gnn_forward():

    model = HealthcareGNN(
        input_dim=16,
        hidden_dim=32,
        output_dim=2
    )

    x = torch.rand(
        10,
        16
    )

    edge_index = torch.tensor([
        [0, 1, 2, 3],
        [1, 2, 3, 4]
    ])

    output = model(
        x,
        edge_index
    )

    assert output.shape == (
        10,
        2
    )