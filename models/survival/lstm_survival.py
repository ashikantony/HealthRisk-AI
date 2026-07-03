import torch
import torch.nn as nn


class LSTMSurvival(nn.Module):

    def __init__(
        self,
        input_dim,
        hidden_dim=128,
        layers=2
    ):
        super().__init__()

        self.lstm = nn.LSTM(
            input_dim,
            hidden_dim,
            layers,
            batch_first=True,
            dropout=0.30
        )

        self.output_layer = nn.Linear(
            hidden_dim,
            1
        )

    def forward(self, x):

        outputs, _ = self.lstm(x)

        final_output = outputs[:, -1, :]

        risk_score = self.output_layer(
            final_output
        )

        return risk_score