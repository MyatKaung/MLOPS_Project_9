import os 
import joblib
from sklearn.linear_model import LogisticRegression
from src.logger import get_logger
from src.custom_exception import CustomException
from sklearn.metrics import accuracy_score, classification_report

logger = get_logger(__name__)
class ModelTraining:
    def __init__(self, processed_data_path, model_output_path):
        self.processed_path = processed_data_path
        self.model_path = model_output_path 
        self.clf = None 
        self.X_train = None 
        self.X_test =None
        self.y_train = None
        self.y_test = None
        os.makedirs(self.model_path, exist_ok=True)
        logger.info(f"Model output directory created at {self.model_path}")
    
    def load_data(self):
        try:
            self.X_train = joblib.load(os.path.join(self.processed_path, "X_train.pkl"))
            self.X_test = joblib.load(os.path.join(self.processed_path, "X_test.pkl"))
            self.y_train = joblib.load(os.path.join(self.processed_path, "y_train.pkl"))
            self.y_test = joblib.load(os.path.join(self.processed_path, "y_test.pkl"))
            logger.info(f"Data loaded from {self.processed_path}")
        except Exception as e:
            logger.error(f"File not found: {e}")
            raise CustomException(f"Failed to load the data", e)
        
    def train_model(self):
        try:
            self.clf = LogisticRegression(random_state=42,max_iter=1000)
            self.clf.fit(self.X_train,self.y_train)
            joblib.dump(self.clf, os.path.join(self.model_path, "model.pkl"))
            logger.info(f"Model trained and saved at {os.path.join(self.model_path, 'model.pkl')}")
        except Exception as e:
            logger.error(f"Model training failed: {e}")
            raise CustomException(f"Failed to train the model", e)
    
    def evaluate_model(self):
        try:
            y_pred = self.clf.predict(self.X_test)
            accuracy = accuracy_score(self.y_test, y_pred)
        
            report = classification_report(self.y_test, y_pred)
            logger.info(f"Model evaluation completed. Accuracy: {accuracy}")
            logger.info(f"Classification Report:\n{report}")
        except Exception as e:
            logger.error(f"Model evaluation failed: {e}")
            raise CustomException(f"Failed to evaluate the model", e)
        
    def run(self):
        try:
            self.load_data()
            self.train_model()
            self.evaluate_model()
        except Exception as e:
            logger.error(f"An error occurred during the model training process: {e}")
            raise CustomException(f"Failed during the model training process", e)
if __name__ == "__main__":
    try:
        processed_data_path = "artifacts/processed_data"
        model_output_path = "artifacts/model"
        
        model_trainer = ModelTraining(processed_data_path, model_output_path)
        model_trainer.run()
    except CustomException as e:
        print(f"A custom error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")