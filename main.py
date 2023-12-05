from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
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

STAGE_NAME = "Data transformation stage"
logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
data_ingestion = DataTransformationTrainingPipeline()
data_ingestion.main()
logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

STAGE_NAME = "Model training stage"
logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
data_ingestion = ModelTrainerTrainingPipeline()
data_ingestion.main()
logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")