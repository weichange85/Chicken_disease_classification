import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from typing import Any
import base64
from pathlib import Path

@ensure_annotations
def read_yaml_file(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(directory_paths:list, verbase=True):
    """Create list of directories"""

    for path in directory_paths:
        os.makedirs("path", exist_ok=True)
        if verbase:
            logger.info(f"created directories: {path}")


@ensure_annotations
def save_json(out_filepath, data:dict):
    with open(out_filepath, 'r') as file:
        json.dump(data, file, indent=4)

    logger.info(f"json file saved at: {out_filepath}")


@ensure_annotations
def get_size(path: Path) -> str:
    """get size in kb.

    Args:
        path (Path): path to the file.

    Returns:
        str: size in kB
    """

    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"