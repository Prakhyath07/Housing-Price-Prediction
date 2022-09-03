import json
from housing.logger import logging
from housing.exception import customException
from housing.entity.config_entity import DataValidationConfig
from housing.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact
import os,sys
import pandas as pd
from housing.util.util import read_yaml_file

from evidently.model_profile import Profile
from evidently.model_profile.sections import DataDriftProfileSection
from evidently.dashboard import Dashboard
from evidently.dashboard.tabs import DataDriftTab

class DataValidation:

    def __init__(self,data_validation_config:DataValidationConfig,
                 data_ingestion_artifact:DataIngestionArtifact):
        try:
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact = data_ingestion_artifact

            self.training_file_path = self.data_ingestion_artifact.train_file_path
            self.testing_file_path = self.data_ingestion_artifact.test_file_path

        except Exception as e:
            raise customException(e,sys) from e

    def get_train_and_test_df(self):
        try:
            train_df = pd.read_csv(self.training_file_path)
            test_df = pd.read_csv(self.testing_file_path)

            return train_df,test_df

        except Exception as e:
            raise customException(e, sys) from e

    def is_train_test_file_exists(self):
        try:
            logging.info("checking if training and test file is available")
            is_train_file_exist =False
            is_test_file_exist =False


            is_train_file_exist = os.path.exists(self.training_file_path)
            is_test_file_exist = os.path.exists(self.testing_file_path)

            is_available = is_test_file_exist and is_train_file_exist

            logging.info(f"Does train and test file exists? -> {is_available}"
                         )

            if not is_available:
                message = f"Training file: {self.training_file_path} or testing file {self.testing_file_path} is not present"
                logging.info(message)
                raise Exception(message)

            return is_available

        except Exception as e:
            raise customException(e,sys) from e


    def validate_dataset_schema(self) ->bool:
        try:
            validation_status =True

            schema_file = self.data_validation_config.schema_file_path
            config_info = read_yaml_file(file_path=schema_file)

            df_train,df_test= self.get_train_and_test_df()
            cat_cols = config_info['categorical_columns']
            if len(config_info['columns']) != len(df_train.columns):
                logging.info(f" number of columns in schema file: {len(config_info['columns'])} "
                             f"is not equal to number of columns in train dataset: {len(df_train.columns)}")
                validation_status=False
            if sorted(config_info['columns'].keys()) != sorted(df_train.columns):
                logging.info(f" columns in schema file: {sorted(config_info['columns'].keys())} "
                             f"is not same as  columns in train dataset: {sorted(df_train.columns)}")
                validation_status = False
            for i in cat_cols:
                for j in sorted(config_info['domain_value'][i]):
                    if j not in sorted(df_train[i].unique()):
                        logging.info(f" categories in schema file for categorical column {i}: {sorted(config_info['domain_value'][i])}"
                                    f"does not contain: {j} which is present in train data set")
                        validation_status = False


            cat_cols = config_info['categorical_columns']
            if len(config_info['columns']) != len(df_test.columns):
                logging.info(f" number of columns in schema file: {len(config_info['columns'])} "
                             f"is not equal to number of columns in test dataset: {len(df_test.columns)}")
                validation_status = False
            if sorted(config_info['columns'].keys()) != sorted(df_test.columns):
                logging.info(f" columns in schema file: {sorted(config_info['columns'].keys())} "
                             f"is not same as  columns in test dataset: {sorted(df_test.columns)}")
                validation_status = False
            for i in cat_cols:
                for j in sorted(config_info['domain_value'][i]):
                    if j not in sorted(df_test['ocean_proximity'].unique()):
                        logging.info(
                            f" categories in schema file for categorical column {i}: {sorted(config_info['domain_value'][i])}"
                            f"does not contain: {j} which is present in test data set")
                        validation_status = False


            return validation_status
        except Exception as e:
            raise customException(e, sys) from e

    def is_data_drift_found(self) -> bool:
        try:
            report = self.get_and_save_data_drift_report()
            self.save_data_drift_report_page()

            return True

        except Exception as e:
            raise customException(e, sys) from e

    def get_and_save_data_drift_report(self):
        try:
            profile = Profile(sections=[DataDriftProfileSection()])
            train_df,test_df = self.get_train_and_test_df()

            profile.calculate(train_df,test_df)

            ## save data drift (str format)
            # profile.json()

            # convert json str to dictionary or list format
            report = json.loads(profile.json())

            report_file_path = self.data_validation_config.report_file_path

            report_dir = os.path.dirname(report_file_path)

            os.makedirs(report_dir,exist_ok=True)

            with open(report_file_path,"w") as report_file:
                json.dump(report,report_file,indent=6)

            return report

        except Exception as e:
            raise customException(e, sys) from e

    def save_data_drift_report_page(self):
        try:
            dashboard = Dashboard(tabs=[DataDriftTab()])
            train_df,test_df = self.get_train_and_test_df()

            dashboard.calculate(train_df,test_df)

            report_page_file_path = self.data_validation_config.report_page_file_path
            report_page_dir = os.path.dirname(report_page_file_path)
            os.makedirs(report_page_dir,exist_ok=True)
            dashboard.save(report_page_file_path)


        except Exception as e:
            raise customException(e, sys) from e


    def initiate_data_validation(self):

        try:
            a=self.is_train_test_file_exists()

            b=self.validate_dataset_schema()

            c=self.is_data_drift_found()

            validated = a and b and c

            data_validation_artifact = DataValidationArtifact(
                scehma_file_path= self.data_validation_config.schema_file_path,
                report_file_path= self.data_validation_config.report_file_path,
                report_page_file_path=self.data_validation_config.report_page_file_path,
                is_validated=validated,
                message="Data Validation completed successfully")

            logging.info(f"Data validation artifact {data_validation_artifact}")

            return data_validation_artifact





        except Exception as e:
            raise customException(e,sys) from e