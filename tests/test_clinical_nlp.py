from transformers import (
    AutoTokenizer
)


def test_tokenizer():

    tokenizer = (
        AutoTokenizer
        .from_pretrained(
            "bert-base-uncased"
        )
    )

    text = (
        "Patient diagnosed with diabetes."
    )

    tokens = tokenizer(
        text
    )

    assert (
        len(
            tokens["input_ids"]
        ) > 0
    )