from src.data_processing import DataProcessing
from src.model_training import ModelTraining
from src.logger import get_logger
from src.custom_exception import CustomException

logger = get_logger(__name__)

if __name__ == '__main__':
    try:
        # Paths
        raw_data_path = "artifacts/raw/data.csv"
        processed_data_path = "artifacts/processed_data"
        model_output_path = "artifacts/model"

        # Data Processing
        data_processor = DataProcessing(raw_data_path, processed_data_path)
        data_processor.run()

        # Model Training
        model_trainer = ModelTraining(processed_data_path, model_output_path)
        model_trainer.run()

        logger.info("✅ Training pipeline completed successfully.")
    except CustomException as e:
        logger.error(f"A custom error occurred: {e}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")