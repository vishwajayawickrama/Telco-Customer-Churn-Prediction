import openai, groq
import logging
import pandas as pd
from enum import Enum
from typing import Optional
from dotenv import load_dotenv
from pydantic import BaseModel
from abc import ABC, abstractmethod
logging.basicConfig(level=logging.INFO, format=
    '%(asctime)s - %(levelname)s - %(message)s')
load_dotenv()


class MissingValueHandlingStrategy(ABC):
    @abstractmethod
    def handle(self, df: pd.DataFrame) ->pd.DataFrame:
        pass


class DropMissingValuesStrategy(MissingValueHandlingStrategy):
    def __init__(self, critical_columns=[]):
        self.critical_columns = critical_columns
        logging.info(f"Dropping rows with missing values in critical columns: {self.critical_columns}")


    def handle(self, df: pd.DataFrame) ->pd.DataFrame:
        """
            df.dropna(subset=subset) -> removes rows from a DataFrame where any of the columns listed in subset have NaN (missing) values.
            If you don't pass subset=..., dropna() will check all columns for missing values before dropping rows.
        """
        df_cleaned = df.dropna(subset=self.critical_columns)
        n_dropped = len(df) - len(df_cleaned)
        logging.info(f"{n_dropped} has been dropped")
        return df_cleaned


class FillMissingValuesStrategy(MissingValueHandlingStrategy):
    """
    Missing -> Mean ( Age )
            -> Custom (Gender)
    """

    def __init__(self, method='mean', fill_value=None, relavant_columns=None, is_custom_imputer=False, custom_imputer=None):
        self.method = method
        self.fill_value = fill_value
        self.relavant_columns = relavant_columns
        self.is_custom_imputer = is_custom_imputer
        self.custom_imputer = custom_imputer

    def handle(self, df) -> pd.DataFrame:
        if self.is_custom_imputer:
            return self.custom_imputer.impute(df)
        
        df[self.relavant_columns] = df[self.relavant_columns].fillna(df[self.relavant_columns].mean())
        logging.info(f"Missing Value Filled in Columns {self.relavant_columns}")
        return df