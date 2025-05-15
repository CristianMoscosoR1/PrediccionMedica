from flask import Flask, render_template, request, send_from_directory
import os, joblib, pandas as pd

app = Flask(
    __name__,
    template_folder='../templates',
    static_folder='static'
)

# Servir archivos de la carpeta media
@app.route('/media/<path:filename>')
def media(filename):
    media_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../media'))
    return send_from_directory(media_dir, filename)

# --- Cargar artefactos ---
MODEL_DIR   = os.path.join(os.path.dirname(__file__), '..', 'models')
MODEL_PATH  = os.path.join(MODEL_DIR, 'logistic_regression_model.pkl')
SCALER_PATH = os.path.join(MODEL_DIR, 'standard_scaler.pkl')

model  = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

# Rutas
@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
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
        df = pd.DataFrame([rec])
        df['gender'] = df['gender'].map({'Masculino': 0, 'Femenino': 1, 'Otro': 2})
        df = pd.get_dummies(df, columns=['smoking_history'], drop_first=True)
        for col in [
            'smoking_history_actual',
            'smoking_history_anterior',
            'smoking_history_alguna vez',
            'smoking_history_nunca',
            'smoking_history_no actual'
        ]:
            if col not in df:
                df[col] = 0
        ordered_cols = [
            'gender', 'age', 'hypertension', 'heart_disease', 'bmi', 'HbA1c_level', 'blood_glucose_level',
            'smoking_history_actual', 'smoking_history_anterior',
            'smoking_history_alguna vez', 'smoking_history_nunca', 'smoking_history_no actual'
        ]
        df = df.reindex(columns=ordered_cols, fill_value=0)
        num_cols = ['age', 'bmi', 'HbA1c_level', 'blood_glucose_level']
        df[num_cols] = scaler.transform(df[num_cols])
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