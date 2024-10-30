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

@ensure_annotations
def read_yaml_file(file_path) -> ConfigBox:
    """reads yamk and returns ConfigBox type"""
    try:
        with open(file_path, 'r') as file:
            content = yaml.safe_load(file)
            logger.info(f"yaml file: {file_path} loaded successfully")
            return content
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
