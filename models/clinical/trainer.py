import torch
import torch.nn as nn
from torch.utils.data import (
    DataLoader,
    TensorDataset
)
from sklearn.metrics import (
    accuracy_score,
    f1_score
)


class ClinicalNLPTrainer:

    def __init__(
        self,
        model,
        learning_rate=2e-5,
        epochs=5,
        batch_size=8
    ):

        self.model = model
        self.epochs = epochs
        self.batch_size = batch_size

        self.optimizer = (
            torch.optim.AdamW(
                model.parameters(),
                lr=learning_rate
            )
        )

        self.criterion = (
            nn.CrossEntropyLoss()
        )

    def train(
        self,
        input_ids,
        attention_masks,
        labels
    ):

        dataset = TensorDataset(
            input_ids,
            attention_masks,
            labels
        )

        dataloader = DataLoader(
            dataset,
            batch_size=self.batch_size,
            shuffle=True
        )

        self.model.train()

        for epoch in range(
            self.epochs
        ):

            total_loss = 0

            for batch in dataloader:

                ids, masks, y = batch

                self.optimizer.zero_grad()

                outputs = self.model(
                    ids,
                    masks
                )

                loss = self.criterion(
                    outputs,
                    y
                )

                loss.backward()

                self.optimizer.step()

                total_loss += loss.item()

            avg_loss = (
                total_loss /
                len(dataloader)
            )

            print(
                f"Epoch "
                f"{epoch + 1}/"
                f"{self.epochs}"
            )
            print(
                f"Loss: "
                f"{avg_loss:.4f}"
            )

    def evaluate(
        self,
        input_ids,
        attention_masks,
        labels
    ):

        self.model.eval()

        with torch.no_grad():

            logits = self.model(
                input_ids,
                attention_masks
            )

        predictions = (
            torch.argmax(
                logits,
                dim=1
            )
            .cpu()
            .numpy()
        )

        labels = (
            labels.cpu()
            .numpy()
        )

        accuracy = accuracy_score(
            labels,
            predictions
        )

        f1 = f1_score(
            labels,
            predictions,
            average="weighted"
        )

        return {
            "accuracy": accuracy,
            "f1_score": f1
        }