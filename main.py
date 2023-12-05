from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.logging import logger

STAGE_NAME = "Data Ingestion stage"

logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
data_ingestion = DataIngestionTrainingPipeline()
data_ingestion.main()
logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")


STAGE_NAME = "Data validation stage"

logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
data_ingestion = DataValidationTrainingPipeline()
data_ingestion.main()
logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
