# Import necessary libraries
import os
from pathlib import Path
import logging

# Configure logging to show timestamp, log level, and message
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] - [%(levelname)s] - %(message)s')

# List of files and directories to be created in the project structure
list_of_files = [
    "app.py",
    "requirements.txt",
    "setup.py",
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "experiments/experiment.ipynb",
]

# Loop through each file path in the list
for filepath in list_of_files:
    # Convert string path to Path object for better path handling
    filepath = Path(filepath)

    # Split the path into directory and filename components
    filedir, filename = os.path.split(filepath)

    # If the file path has a directory component, create the directory
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    # If the file does not exist or is empty, create an empty file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            logging.info(f"Creating empty file: {filepath}")
            pass
    else:
        logging.info(f"File already exists: {filepath}")
