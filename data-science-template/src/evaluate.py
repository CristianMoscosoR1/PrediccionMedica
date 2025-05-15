from sklearn.metrics import classification_report
import pandas as pd
import joblib

def evaluate_model(model_path, data_path):
    """Evalúa un modelo guardado usando un conjunto de datos."""
    model = joblib.load(model_path)
    data = pd.read_csv(data_path)
    X = data.drop('target', axis=1)
    y = data['target']
    predictions = model.predict(X)
    print(classification_report(y, predictions))