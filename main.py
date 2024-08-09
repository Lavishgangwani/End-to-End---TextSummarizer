#main.py


from TextSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from TextSummarizer.logging import logger

STAGE_NAME= "Data Ingestion Stage"

try:
    logger.info(f">>>>>>>{STAGE_NAME}<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>{STAGE_NAME} completed successfully.<<<<<<<\n\nx=======x")
except Exception as e:
    logger.exception(e)
    raise e