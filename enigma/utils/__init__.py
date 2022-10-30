import yaml
import os 
from typing import Dict

_YML_EXT = ".yml"
_YAML_EXT = ".yaml"


def load_config_from_file(path: str) -> Dict:
    file_ext = os.path.splitext(path)[-1]
    assert file_ext in {_YML_EXT, _YAML_EXT}, "Only yaml and yml configs are supported. "
    with open(path, "r") as f:
        config = yaml.load(f, Loader=yaml.SafeLoader)
    return config
