from housing.pipeline.pipeline import Pipeline
from housing.logger import logging
from housing.exception import customException
from housing.config.configuration import Configuration
def main():
    try:
        pipeline=Pipeline()
        pipeline.run_pipeline()
        # config = Configuration()
        # data_valid_config=config.get_data_validation_config()
        # print(data_valid_config)

    except Exception as e:
        print(e)
        logging.error(f"{e}")

if __name__=="__main__":
    main()
