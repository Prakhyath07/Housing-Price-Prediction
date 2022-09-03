import os
from datetime import datetime

ROOT_DIR= os.getcwd()

CONFIG_DIR = "config"
CONFIG_FILE_NAME = "config.yaml"
CONFIG_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILE_NAME)

CURRENT_TIME_STAMP =f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"


## training pipeline constants

TRAINING_PIPELINE_CONFIG_KEY = "training_pipeline_config"
TRAINING_PIPELINE_ARTIFACT_DIR_KEY = "artifact_dir"
TRAINING_PIPELINE_NAME_KEY = "pipeline_name"

## Data ingestion constants
DATA_INGESTION_CONFIG_KEY = "data_ingestion_config"
DATA_INGESTION_ARTIFACT_DIR = "data_ingestion"
DATA_INGESTION_DOWNLOAD_URL_KEY = "dataset_download_url"
DATA_INGESTION_RAW_DATA_DIR_KEY = "raw_data_dir"
DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY = "tgz_download_dir"
DATA_INGESTION_INGESTED_DIR_NAME_KEY = "ingested_dir"
DATA_INGESTION_TRAIN_DIR_KEY = "ingested_train_dir"
DATA_INGESTION_TEST_DIR_KEY = "ingested_test_dir"

## Data validation constants
DATA_VALIDATION_CONFIG_KEY = "data_validation_config"
DATA_VALIDATION_SCHEMA_DIR_KEY = "schema_dir"
DATA_VALIDATION_SCHEMA_NAME_KEY = "schema_file_name"
REPORT_FILE_NAME_KEY = "report_file_name"
REPORT_FILE_PAGE_NAME_KEY = "report_page_file_name"
DATA_VALIDATION_ARTIFACT_DIR_NAME = "data_validation"

## Data transfrom constants
DATA_TRANSFORMATION_CONFIG_KEY = "data_transformation_config"
BEDROOM_PER_ROOM_KEY = "add_bedroom_per_room"
DATA_TRANSFORMED_DIR_KEY = "transformed_dir"
DATA_TRANSFORMED_TRAIN_DIR_KEY = "transformed_train_dir"
DATA_TRANSFORMED_TEST_DIR_KEY = "transformed_test_dir"
PREPROCESSED_OBJECT_DIR_KEY = "preprocessing_dir"
PREPROCESSED_OBJECT_NAME_KEY = "preprocessed.pkl"


## model training constants
MODEL_TRAINED_CONFIG_KEY = "model_trainer_config"
MODEL_TRAINED_DIR_KEY = "trained_model_dir"
MODEL_TRAINED_NAME_KEY = "model_file_name"
BASE_ACCURACY_KEY = "base_accuracy"
MODEL_CONFIG_DIR_KEY = "model_config_dir"
MODEL_CONFIG_FILE_NAME_KEY = "model_config_file_name"

## model evaluation constants
MODEL_EVALUATION_CONFIG_KEY = "model_evaluation_config"
MODEL_EVALUATION_FILE_NAME_KEY = "model_evaluation_file_name"

## model pusher constants
MODEL_PUSHER_CONFIG_KEY = "model_pusher_config"
EXPORT_DIR_PATH_KEY = "model_export_dir"

