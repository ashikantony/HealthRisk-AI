import pandas as pd


def test_dataframe_not_empty(
    sample_dataframe
):

    assert (
        len(sample_dataframe) > 0
    )


def test_required_columns(
    sample_dataframe
):

    expected = {
        "age",
        "income",
        "claim_amount",
        "target"
    }

    assert expected.issubset(
        sample_dataframe.columns
    )