#stage_02_data_validation.py


from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.logging import logger
from TextSummarizer.components.data_validation import DataValidation


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_files_exists()