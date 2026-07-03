from .data_cleaning import DataCleaner
from .missing_value_handler import (
    MissingValueHandler
)
from .duplicate_removal import (
    DuplicateRemover
)


class DataProcessingPipeline:

    def __init__(self):

        self.cleaner = DataCleaner()
        self.missing_handler = (
            MissingValueHandler()
        )
        self.duplicate_remover = (
            DuplicateRemover()
        )

    def run(self, df):

        print(
            "Starting Processing Pipeline..."
        )

        df = self.cleaner.clean(df)

        df = (
            self.missing_handler
            .median_imputation(df)
        )

        df = (
            self.missing_handler
            .mode_imputation(df)
        )

        df = (
            self.duplicate_remover
            .remove_duplicates(df)
        )

        print(
            "Processing Complete."
        )

        return df