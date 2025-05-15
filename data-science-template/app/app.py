from flask import Flask, render_template, request
import os, joblib, pandas as pd

app = Flask(__name__, template_folder='../templates')

# --- Cargar artefactos ---
MODEL_DIR   = os.path.join(os.path.dirname(__file__), '..', 'models')
MODEL_PATH  = os.path.join(MODEL_DIR, 'logistic_regression_model.pkl')
SCALER_PATH = os.path.join(MODEL_DIR, 'standard_scaler.pkl')

model  = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

# Rutas
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Leer input del formulario
        rec = {
            'gender': request.form['gender'],
            'age': float(request.form['age']),
            'hypertension': int(request.form['hypertension']),
            'heart_disease': int(request.form['heart_disease']),
            'smoking_history': request.form['smoking_history'],
            'bmi': float(request.form['bmi']),
            'HbA1c_level': float(request.form['HbA1c_level']),
            'blood_glucose_level': int(request.form['blood_glucose_level'])
        }
        # Preproceso idéntico a train.py
        df = pd.DataFrame([rec])
        df['gender'] = df['gender'].map({'Male': 0, 'Female': 1, 'Other': 2})
        df = pd.get_dummies(df, columns=['smoking_history'], drop_first=True)
        for col in [
            'smoking_history_current',
            'smoking_history_ever',
            'smoking_history_former',
            'smoking_history_never',
            'smoking_history_not current'
        ]:
            if col not in df:
                df[col] = 0
        # Reordenar columnas para que coincidan con el entrenamiento
        ordered_cols = [
            'gender', 'age', 'hypertension', 'heart_disease', 'bmi', 'HbA1c_level', 'blood_glucose_level',
            'smoking_history_current', 'smoking_history_ever',
            'smoking_history_former', 'smoking_history_never', 'smoking_history_not current'
        ]
        df = df.reindex(columns=ordered_cols, fill_value=0)
        num_cols = ['age', 'bmi', 'HbA1c_level', 'blood_glucose_level']
        df[num_cols] = scaler.transform(df[num_cols])
        # Predicción
        pred = int(model.predict(df)[0])
        return render_template(
            'result.html',
            prediction=pred,
            gender=rec['gender'],
            age=rec['age'],
            hypertension=rec['hypertension'],
            heart_disease=rec['heart_disease'],
            smoking_history=rec['smoking_history'],
            bmi=rec['bmi'],
            HbA1c_level=rec['HbA1c_level'],
            blood_glucose_level=rec['blood_glucose_level']
        )
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)