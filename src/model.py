import joblib
import numpy as np
from tensorflow.keras.models import load_model
from category_encoders import TargetEncoder
from sklearn.preprocessing import StandardScaler
import pandas as pd
from datetime import datetime
from feature_engineering import FeatureEngineer


class Model:
    def __init__(self):
        try:
            self.price_model = joblib.load("price_model.pkl")
        except Exception as e:
            print(f"[CHYBA] Nepodařilo se načíst price_model.pkl: {e}")
            self.price_model = None

        try:
            self.deal_model = load_model("deal_model.h5")
        except Exception as e:
            print(f"[CHYBA] Nepodařilo se načíst deal_model.h5: {e}")
            self.deal_model = None

        try:
            self.encoder = joblib.load("deal_encoder.pkl")
        except Exception as e:
            print(f"[CHYBA] Nepodařilo se načíst deal_encoder.pkl: {e}")
            self.encoder = None

        try:
            self.scaler = joblib.load("deal_scaler.pkl")
        except Exception as e:
            print(f"[CHYBA] Nepodařilo se načíst deal_scaler.pkl: {e}")
            self.scaler = None

    def _log_prediction(self, input_data: dict, prediction, prediction_type: str):
        log_entry = {
            "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "prediction_type": prediction_type,
            "prediction_result": prediction
        }
        log_entry.update(input_data)
        df_log = pd.DataFrame([log_entry])
        try:
            df_log.to_csv("predictions_log.csv", mode='a', index=False, header=not pd.io.common.file_exists("predictions_log.csv"))
        except Exception as e:
            print(f"[LOGGING ERROR] Nepodařilo se zapsat log: {e}")

    def predict_price(self, input_data: dict) -> float:
        if self.price_model is None:
            raise RuntimeError("Model pro odhad ceny není načten.")
        df = pd.DataFrame([input_data])
        prediction = self.price_model.predict(df)[0]
        rounded = round(prediction, 2)
        self._log_prediction(input_data, rounded, "price")
        return rounded

    def predict_deal(self, input_data: dict) -> int:
        if None in [self.deal_model, self.encoder, self.scaler]:
            raise RuntimeError("Modely pro deal score nejsou načteny.")
        df = pd.DataFrame([input_data])
        df_encoded = self.encoder.transform(df)
        X = pd.concat([df_encoded[["Značka", "Model"]],
                       df[["Najeto", "Výkon", "Spotřeba", "První registrace", "Cena"]]], axis=1)
        X_scaled = self.scaler.transform(X)
        probabilities = self.deal_model.predict(X_scaled)
        predicted_class = np.argmax(probabilities, axis=1)[0] + 1
        self._log_prediction(input_data, predicted_class, "deal")
        return predicted_class
