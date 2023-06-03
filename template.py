import os
from pathlib import Path
import logging


logging.basicConfig(level = logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name = "cnnClassifier"

list_of_files  = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "test.py"
]

for filepath in list_of_files:
    filepathh = Path(filepath)
    filedir, filename = os.path.split(filepathh)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory {filedir} for the file: {filename}")

    if (not os.path.exists(filepathh)) or (os.path.getsize(filepathh) == 0):
        with open(filepathh,"w") as f:
            logging.info(f"Creating emty file: {filepathh}")
    else:
        logging.info(f"{filepathh} already exist")