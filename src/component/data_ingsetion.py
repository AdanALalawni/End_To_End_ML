import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from src import logger
from src import exception
from src.component import data_transformation
from src.component import modle_trainer
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngsetionConfig:
    train_data_path:str= os.path.join("artifacts","train.csv")
    test_data_path:str = os.path.join("artifacts","test.csv")
    raw_data_path:str = os.path.join("artifacts","raw.csv")
class DataIngsetion:
    def __init__(self):
        self.ingsetion_config = DataIngsetionConfig()
    def intitiate_data_ingsetion(self):
        logger.logging.info("Entered the data ingseiton method")
        try:
            df = pd.read_csv('src/nootbooks/data/stud.csv')
            logger.logging.info("Read dataset")
            os.makedirs(os.path.dirname(self.ingsetion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingsetion_config.raw_data_path,index=False,header=True)
            logger.logging.info("Try to split the dataset")
            train_split, test_split = train_test_split(df, test_size=0.2,random_state=45)
            train_split.to_csv(self.ingsetion_config.train_data_path,index=False,header=True)
            test_split.to_csv(self.ingsetion_config.test_data_path,index=False,header=True)
            logger.logging.info("Completed")
            return(
                self.ingsetion_config.train_data_path,
                self.ingsetion_config.test_data_path
            )
        except Exception as e:
           raise exception.CustomException(e,sys)
if __name__=="__main__":
    obj= DataIngsetion()
    train_data,test_data=obj.intitiate_data_ingsetion()

    data_transformation=data_transformation.DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    modeltrainer = modle_trainer.ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))


