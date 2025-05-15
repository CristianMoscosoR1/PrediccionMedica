import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import joblib

# --- CONFIGURACIÓN ---
DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'diabetes_prediction_dataset.csv')
MODEL_DIR = os.path.join(os.path.dirname(__file__), '..', 'models')
os.makedirs(MODEL_DIR, exist_ok=True)

# 1. Carga de datos
df = pd.read_csv(DATA_PATH)

# 2. Preprocesamiento
df['gender'] = df['gender'].map({'Male': 0, 'Female': 1, 'Other': 2})
df = pd.get_dummies(df, columns=['smoking_history'], drop_first=True)

X = df.drop('diabetes', axis=1)
y = df['diabetes']

num_cols = ['age', 'bmi', 'HbA1c_level', 'blood_glucose_level']
scaler = StandardScaler()
X[num_cols] = scaler.fit_transform(X[num_cols])

# 3. Entrenamiento
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

# 4. Serializar modelo y escalador
joblib.dump(model, os.path.join(MODEL_DIR, 'logistic_regression_model.pkl'))
joblib.dump(scaler, os.path.join(MODEL_DIR, 'standard_scaler.pkl'))

print("Entrenamiento completo. Modelos guardados en /models.")