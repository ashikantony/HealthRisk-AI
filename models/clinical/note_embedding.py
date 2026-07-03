import torch
from transformers import (
    AutoTokenizer,
    AutoModel
)


class ClinicalEmbeddingGenerator:

    def __init__(
        self,
        model_name="emilyalsentzer/Bio_ClinicalBERT"
    ):

        self.tokenizer = (
            AutoTokenizer.from_pretrained(
                model_name
            )
        )

        self.model = (
            AutoModel.from_pretrained(
                model_name
            )
        )

        self.model.eval()

    def generate_embedding(
        self,
        text,
        max_length=512
    ):

        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=max_length
        )

        with torch.no_grad():

            outputs = self.model(
                **inputs
            )

        embedding = (
            outputs.last_hidden_state
            [:, 0, :]
            .squeeze()
        )

        return embedding.numpy()

    def batch_embeddings(
        self,
        texts
    ):

        embeddings = []

        for text in texts:
            embeddings.append(
                self.generate_embedding(
                    text
                )
            )

        return embeddings