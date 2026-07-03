import torch
import torch.nn as nn
import torch.nn.functional as F


class DeepSurv(nn.Module):

    def __init__(
        self,
        input_dim,
        hidden_dims=[128, 64],
        dropout=0.30
    ):
        super().__init__()

        layers = []
        previous_dim = input_dim

        for hidden_dim in hidden_dims:

            layers.extend([
                nn.Linear(
                    previous_dim,
                    hidden_dim
                ),
                nn.ReLU(),
                nn.BatchNorm1d(
                    hidden_dim
                ),
                nn.Dropout(
                    dropout
                )
            ])

            previous_dim = hidden_dim

        self.network = nn.Sequential(
            *layers
        )

        self.risk_layer = nn.Linear(
            previous_dim,
            1
        )

    def forward(self, x):

        x = self.network(x)
        risk = self.risk_layer(x)

        return risk