import os
from pathlib import Path
import logging

logging.basicConfig(Level=loggin.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    
]