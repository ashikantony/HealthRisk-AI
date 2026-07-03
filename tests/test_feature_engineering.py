import numpy as np


def test_no_missing_values(
    sample_dataframe
):

    assert (
        sample_dataframe
        .isnull()
        .sum()
        .sum()
        == 0
    )


def test_numeric_columns(
    sample_dataframe
):

    numeric = (
        sample_dataframe
        .select_dtypes(
            include=np.number
        )
    )

    assert len(
        numeric.columns
    ) == 4