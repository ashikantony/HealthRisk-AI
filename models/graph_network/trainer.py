import torch
import torch.nn.functional as F
from sklearn.metrics import (
    accuracy_score,
    f1_score
)


class GNNTrainer:

    def __init__(
        self,
        model,
        learning_rate=0.001,
        epochs=100
    ):

        self.model = model
        self.epochs = epochs

        self.optimizer = (
            torch.optim.Adam(
                model.parameters(),
                lr=learning_rate
            )
        )

    def train(
        self,
        data
    ):

        self.model.train()

        for epoch in range(
            self.epochs
        ):

            self.optimizer.zero_grad()

            logits = self.model(
                data.x,
                data.edge_index
            )

            loss = (
                F.cross_entropy(
                    logits[data.train_mask],
                    data.y[
                        data.train_mask
                    ]
                )
            )

            loss.backward()

            self.optimizer.step()

            if (
                epoch + 1
            ) % 10 == 0:

                print(
                    f"Epoch "
                    f"{epoch + 1}/"
                    f"{self.epochs}"
                    f" | Loss: "
                    f"{loss.item():.4f}"
                )

    def evaluate(
        self,
        data
    ):

        self.model.eval()

        with torch.no_grad():

            logits = self.model(
                data.x,
                data.edge_index
            )

        predictions = (
            logits.argmax(
                dim=1
            )
        )

        y_true = (
            data.y[
                data.test_mask
            ]
            .cpu()
            .numpy()
        )

        y_pred = (
            predictions[
                data.test_mask
            ]
            .cpu()
            .numpy()
        )

        accuracy = (
            accuracy_score(
                y_true,
                y_pred
            )
        )

        f1 = f1_score(
            y_true,
            y_pred,
            average="weighted"
        )

        return {
            "accuracy":
                accuracy,
            "f1_score":
                f1
        }