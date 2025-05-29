# Loads and parses BiB YAML
import yaml


def load_yaml(path: str) -> dict:
    """Load a BiB DSL YAML file into a Python dictionary."""
    with open(path, 'r') as f:
        data = yaml.safe_load(f)
    return data
