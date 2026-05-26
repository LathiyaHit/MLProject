## It will have the common functions that will be used across the project.
import os
import sys

import numpy as np
import pandas as pd

from src.exception import CustomException
from src.logger import logging
import dill ## Dill is a library that is used to serialize and deserialize Python objects. It is used to save the preprocessor object in the artifacts folder.

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)## Dump the object to the file using dill

    except Exception as e:
        raise CustomException(e, sys)
