import torch
import torch.nn as nn
import torch.nn.functional as F


class DeepHit(nn.Module):

    def __init__(
        self,
        input_dim,
        num_time_bins=50,
        hidden_dim=128
    ):
        super().__init__()

        self.shared = nn.Sequential(
            nn.Linear(
                input_dim,
                hidden_dim
            ),
            nn.ReLU(),
            nn.Dropout(0.30)
        )

        self.output_layer = nn.Linear(
            hidden_dim,
            num_time_bins
        )

    def forward(self, x):

        x = self.shared(x)

        probabilities = F.softmax(
            self.output_layer(x),
            dim=1
        )

        return probabilities