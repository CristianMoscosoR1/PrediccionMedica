import os
import sys
import pandas as pd
import joblib

# --- CONFIGURACIÓN ---
MODEL_DIR = os.path.join(os.path.dirname(__file__), '..', 'models')
MODEL_PATH = os.path.join(MODEL_DIR, 'logistic_regression_model.pkl')
SCALER_PATH = os.path.join(MODEL_DIR, 'standard_scaler.pkl')

# 1. Cargar modelo y escalador
model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

# 2. Función de predicción
def predict(record: dict) -> int:
    """
    record debe tener llaves:
      gender (str), age (float), hypertension (0/1), heart_disease (0/1),
      smoking_history (str), bmi (float), HbA1c_level (float), blood_glucose_level (int)
    Retorna: 0 (no diabetes) o 1 (diabetes)
    """
    # Preproceso idéntico al de entrenamiento
    df = pd.DataFrame([record])
    df['gender'] = df['gender'].map({'Male': 0, 'Female': 1, 'Other': 2})
    df = pd.get_dummies(df, columns=['smoking_history'], drop_first=True)
    
    # Asegurar columnas dummy
    for col in ['smoking_history_Formerly smoked', 'smoking_history_Never smoked',
                'smoking_history_Unknown', 'smoking_history_Currently smokes']:
        if col not in df:
            df[col] = 0
    
    num_cols = ['age', 'bmi', 'HbA1c_level', 'blood_glucose_level']
    df[num_cols] = scaler.transform(df[num_cols])
    
    return int(model.predict(df)[0])

# 3. CLI para prueba rápida
if __name__ == '__main__':
    import json
    if len(sys.argv) != 2:
        print("Uso: python predict.py '{\"gender\":\"Male\", \"age\":50, … }'")
        sys.exit(1)
    rec = json.loads(sys.argv[1])
    pred = predict(rec)
    print(f"Predicción de diabetes: {pred} (1 = diabetes, 0 = no)")