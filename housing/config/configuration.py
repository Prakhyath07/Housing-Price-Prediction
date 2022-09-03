from housing.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformConfig, \
    ModelTrainerConfig, ModelEvaluationConfig, ModelPusherConfig, TrainingPipelineConfig
from housing.util.util import read_yaml_file
from housing.logger import logging
from housing.exception import customException
import sys, os
from housing.constant import *


class Configuration:
    def __init__(self,
                 config_file_path:str = CONFIG_FILE_PATH,
                 current_time_stamp:str = CURRENT_TIME_STAMP
                 ) -> None:
        try:
            self.config_info = read_yaml_file(file_path=config_file_path)
            self.training_pipeline_config = self.get_training_pipeline_config()
            self.time_stamp = current_time_stamp
        except Exception as e:
            raise customException(e,sys) from e


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:

            artifact_dir = self.training_pipeline_config.artifact_dir
            data_ingestion_artifact_dir= os.path.join(artifact_dir,DATA_INGESTION_ARTIFACT_DIR,self.time_stamp)
            data_ingestion_config = self.config_info[DATA_INGESTION_CONFIG_KEY]
            dataset_download_url = data_ingestion_config[DATA_INGESTION_DOWNLOAD_URL_KEY]
            tgz_download_dir = os.path.join(data_ingestion_artifact_dir,data_ingestion_config[DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY])
            raw_data_dir = os.path.join(data_ingestion_artifact_dir,data_ingestion_config[DATA_INGESTION_RAW_DATA_DIR_KEY])

            ingested_data_dir = os.path.join(data_ingestion_artifact_dir,data_ingestion_config[DATA_INGESTION_INGESTED_DIR_NAME_KEY])
            ingested_train_dir = os.path.join(ingested_data_dir,data_ingestion_config[DATA_INGESTION_TRAIN_DIR_KEY])
            ingested_test_dir = os.path.join(ingested_data_dir,data_ingestion_config[DATA_INGESTION_TEST_DIR_KEY])

            data_ingestion_config=DataIngestionConfig(
                dataset_download_url = dataset_download_url,
                tgz_download_dir = tgz_download_dir,
                raw_data_dir = raw_data_dir,
                ingested_train_dir = ingested_train_dir,
                ingested_test_dir = ingested_test_dir

            )
            return data_ingestion_config



        except Exception as e:
            raise customException(e, sys) from e

    def get_data_validation_config(self) -> DataValidationConfig:
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir
            data_validation_artifact_dir = os.path.join(artifact_dir, DATA_VALIDATION_ARTIFACT_DIR_NAME, self.time_stamp)
            data_validation_config = self.config_info[DATA_VALIDATION_CONFIG_KEY]
            schema_dir = data_validation_config[DATA_VALIDATION_SCHEMA_DIR_KEY]
            schema_file = os.path.join(ROOT_DIR,schema_dir,data_validation_config[DATA_VALIDATION_SCHEMA_NAME_KEY])
            report_file_path = os.path.join(data_validation_artifact_dir,data_validation_config[REPORT_FILE_NAME_KEY])
            report_page_file_path = os.path.join(data_validation_artifact_dir,data_validation_config[REPORT_FILE_PAGE_NAME_KEY])

            data_validation_config = DataValidationConfig(schema_file_path= schema_file,
                                                          report_file_path=report_file_path,
                                                          report_page_file_path=report_page_file_path)
            return data_validation_config

        except Exception as e:
            raise customException(e, sys) from e

    def get_data_transformation_config(self) -> DataTransformConfig:
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir
            data_transformation_artifact_dir = os.path.join(artifact_dir,
                                                            DATA_TRANSFORMATION_ARTIFACT_DIR,
                                                            self.time_stamp)
            data_transformation_config = self.config_info[DATA_TRANSFORMATION_CONFIG_KEY]
            add_bedroom_per_room = data_transformation_config[BEDROOM_PER_ROOM_KEY]
            transformed_dir = data_transformation_config[DATA_TRANSFORMED_DIR_KEY]
            transformed_train_dir = os.path.join(data_transformation_artifact_dir,transformed_dir,data_transformation_config[DATA_TRANSFORMED_TRAIN_DIR_KEY])
            transformed_test_dir = os.path.join(data_transformation_artifact_dir,transformed_dir,data_transformation_config[DATA_TRANSFORMED_TEST_DIR_KEY])
            preprocessing_dir = data_transformation_config[PREPROCESSED_OBJECT_DIR_KEY]
            preprocessed_object_file_path = os.path.join(data_transformation_artifact_dir,preprocessing_dir,data_transformation_config[PREPROCESSED_OBJECT_NAME_KEY])

            data_transformation_config = DataTransformConfig(add_bedroom_per_room=add_bedroom_per_room,
                                                             transformed_train_dir=transformed_train_dir,
                                                             transformed_test_dir=transformed_test_dir,
                                                             preprocessed_object_file_path=preprocessed_object_file_path)

            logging.info(f"data transformation config: {data_transformation_config}")

            return data_transformation_config

        except Exception as e:
            raise customException(e, sys) from e

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        try:
            model_trainer_config = self.config_info[MODEL_TRAINED_CONFIG_KEY]
            trained_model_dir = model_trainer_config[MODEL_TRAINED_DIR_KEY]
            trained_model_file_path = os.path.join(ROOT_DIR,trained_model_dir,model_trainer_config[MODEL_TRAINED_NAME_KEY])
            base_accuracy = model_trainer_config[BASE_ACCURACY_KEY]

            model_trainer_config = ModelTrainerConfig(trained_model_file_path=trained_model_file_path,
                                                      base_accuracy =base_accuracy )
            return model_trainer_config

        except Exception as e:
            raise customException(e, sys) from e

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        try:
            model_evaluation_config = self.config_info[MODEL_TRAINED_CONFIG_KEY]
            model_evaluation_file_path = model_evaluation_config[MODEL_EVALUATION_FILE_NAME_KEY]

            model_evaluation_config = ModelEvaluationConfig(model_evaluation_file_path= model_evaluation_file_path,
                                                            time_stamp= CURRENT_TIME_STAMP)

            return model_evaluation_config

        except Exception as e:
            raise customException(e, sys) from e

    def get_model_pusher_config(self) -> ModelPusherConfig:
        try:
            model_pusher_config = self.config_info[MODEL_PUSHER_CONFIG_KEY]
            export_dir_path = model_pusher_config[EXPORT_DIR_PATH_KEY]

            model_pusher_config = ModelPusherConfig(export_dir_path=export_dir_path )
        except Exception as e:
            raise customException(e, sys) from e

    def get_training_pipeline_config(self) ->TrainingPipelineConfig:
        try:
            training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir = os.path.join(ROOT_DIR,
                                        training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
                                        training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY]
                                        )
            training_pipeline_config = TrainingPipelineConfig(artifact_dir=artifact_dir)
            logging.info(f"Training pipline config: {training_pipeline_config}")
            return training_pipeline_config

        except Exception as e:
            raise customException(e,sys) from e
