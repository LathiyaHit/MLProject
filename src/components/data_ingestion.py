import os ## Working with the file system, creating directories, and handling file paths.
import sys ## Used for system level operations, such as handling exceptions and accessing system-specific parameters and functions.
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass 

@dataclass ## This is a decorator that is used to create a class that is used to store the configuration of the data ingestion process. It is used to store the paths of the train, test and raw data.
class DataIngestionConfig: ## This is a class that is used to store the configuration of the data ingestion process. It is used to store the paths of the train, test and raw data.
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "data.csv")

## Use dataclass when variables are used to store the configuration of the data ingestion process. It is used to store the paths of the train, test and raw data. It is used to create an instance of the DataIngestionConfig class and then use it to store the paths of the train, test and raw data.

class DataIngestion: ## This is a class that is used to perform the data ingestion process. It is used to read the data from the source, split the data into train and test and then save the train and test data in the specified paths.
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv("notebook/data/stud.csv")
            logging.info("Read the dataset as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()