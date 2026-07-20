"""Config loading."""
import yaml


def load(path: str) -> dict:
    with open(path) as fh:
        return yaml.safe_load(fh)
