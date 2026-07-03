import torch
import torch.nn as nn
from transformers import (
    AutoTokenizer,
    AutoModel
)


class ClinicalBERTClassifier(nn.Module):

    def __init__(
        self,
        model_name="emilyalsentzer/Bio_ClinicalBERT",
        num_classes=2
    ):
        super().__init__()

        self.tokenizer = AutoTokenizer.from_pretrained(
            model_name
        )

        self.bert = AutoModel.from_pretrained(
            model_name
        )

        self.dropout = nn.Dropout(0.30)

        self.classifier = nn.Linear(
            self.bert.config.hidden_size,
            num_classes
        )

    def tokenize(
        self,
        texts,
        max_length=512
    ):

        return self.tokenizer(
            texts,
            truncation=True,
            padding=True,
            max_length=max_length,
            return_tensors="pt"
        )

    def forward(
        self,
        input_ids,
        attention_mask
    ):

        outputs = self.bert(
            input_ids=input_ids,
            attention_mask=attention_mask
        )

        pooled_output = (
            outputs.last_hidden_state[:, 0]
        )

        pooled_output = self.dropout(
            pooled_output
        )

        logits = self.classifier(
            pooled_output
        )

        return logits