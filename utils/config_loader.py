from pathlib import Path
import yaml


class ConfigLoader:
    """
    Centralized YAML configuration loader.
    """

    CONFIG_DIR = Path("configs")

    @classmethod
    def load(cls, filename: str):
        file_path = cls.CONFIG_DIR / filename

        if not file_path.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {file_path}"
            )

        with open(file_path, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)


if __name__ == "__main__":
    app_config = ConfigLoader.load("app_config.yaml")
    print(app_config)