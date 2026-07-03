from pathlib import Path


class FeatureStoreBuilder:

    def __init__(
        self,
        save_directory="data/features_store"
    ):

        self.save_directory = (
            Path(save_directory)
        )

        self.save_directory.mkdir(
            parents=True,
            exist_ok=True
        )

    def save_feature_set(
        self,
        dataframe,
        file_name
    ):

        file_path = (
            self.save_directory
            / file_name
        )

        dataframe.to_parquet(
            file_path,
            index=False
        )

        return file_path

    def load_feature_set(
        self,
        file_name
    ):

        file_path = (
            self.save_directory
            / file_name
        )

        return (
            file_path.read_text()
            if not file_path.exists()
            else None
        )