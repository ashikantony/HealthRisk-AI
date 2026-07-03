from pathlib import Path
import logging
import time
import requests
import pandas as pd
import yaml


class BaseLoader:
    """
    Base class for all HealthRisk AI data loaders.
    """

    def __init__(
        self,
        data_source: str,
        save_directory: str = "data/raw"
    ):
        self.data_source = data_source
        self.save_directory = Path(save_directory)
        self.save_directory.mkdir(
            parents=True,
            exist_ok=True
        )

        self.logger = self._setup_logger()

    def _setup_logger(self):

        logger = logging.getLogger(self.data_source)
        logger.setLevel(logging.INFO)

        if not logger.handlers:
            console_handler = logging.StreamHandler()

            formatter = logging.Formatter(
                "%(asctime)s | %(name)s | "
                "%(levelname)s | %(message)s"
            )

            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)

        return logger

    def load_yaml_config(self, file_path: str):

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:
            return yaml.safe_load(file)

    def create_directory(self, directory: str):

        path = Path(directory)
        path.mkdir(
            parents=True,
            exist_ok=True
        )
        return path

    def save_csv(
        self,
        dataframe: pd.DataFrame,
        file_name: str
    ):

        file_path = self.save_directory / file_name

        dataframe.to_csv(
            file_path,
            index=False
        )

        self.logger.info(
            f"Saved file -> {file_path}"
        )

        return file_path

    def save_json(
        self,
        data,
        file_name: str
    ):

        import json

        file_path = self.save_directory / file_name

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(
                data,
                file,
                indent=4
            )

        self.logger.info(
            f"Saved file -> {file_path}"
        )

        return file_path

    def request_with_retry(
        self,
        url: str,
        params=None,
        retries: int = 3,
        delay: int = 5,
    ):

        for attempt in range(retries):

            try:
                response = requests.get(
                    url,
                    params=params,
                    timeout=60
                )

                response.raise_for_status()

                self.logger.info(
                    f"Request successful: {url}"
                )

                return response

            except requests.RequestException as e:

                self.logger.warning(
                    f"Attempt {attempt+1} failed."
                )

                self.logger.warning(str(e))

                if attempt < retries - 1:
                    time.sleep(delay)
                else:
                    raise e

    def validate_dataframe(
        self,
        dataframe: pd.DataFrame
    ):

        if dataframe.empty:
            raise ValueError(
                f"{self.data_source} "
                f"returned an empty dataframe."
            )

        self.logger.info(
            f"Data Shape : {dataframe.shape}"
        )

        return True