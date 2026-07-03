import torch
import torch.nn as nn
import torch.nn.functional as F


class DynamicDeepHit(nn.Module):

    def __init__(
        self,
        input_dim,
        hidden_dim=128,
        lstm_layers=2,
        num_time_bins=50
    ):
        super().__init__()

        self.lstm = nn.LSTM(
            input_dim,
            hidden_dim,
            lstm_layers,
            batch_first=True,
            dropout=0.30
        )

        self.output_layer = nn.Linear(
            hidden_dim,
            num_time_bins
        )

    def forward(self, x):

        outputs, _ = self.lstm(x)

        final_state = outputs[:, -1, :]

        probabilities = F.softmax(
            self.output_layer(
                final_state
            ),
            dim=1
        )

        return probabilities