import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os

# Cargar el dataset
df = pd.read_csv('data/diabetes_prediction_dataset.csv')

# Preprocesamiento
df = df.dropna()  # Eliminar valores nulos
df = pd.get_dummies(df, drop_first=True)  # Codificar variables categóricas

# Separar características (X) y etiqueta (y)
X = df.drop('diabetes', axis=1)  # Reemplaza 'diabetes' con el nombre de la columna objetivo
y = df['diabetes']

# Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar el modelo
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluar el modelo
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión del modelo: {accuracy:.2f}")

# Crear el directorio para guardar el modelo si no existe
os.makedirs('model', exist_ok=True)

# Guardar el modelo entrenado
joblib.dump(model, 'model/diabetes_model.pkl')