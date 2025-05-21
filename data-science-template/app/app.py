from flask import Flask, render_template, request, send_from_directory, jsonify
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
MODEL_DIR   = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'models'))
MODEL_PATH  = os.path.join(MODEL_DIR, 'logistic_regression_model.pkl')
SCALER_PATH = os.path.join(MODEL_DIR, 'standard_scaler.pkl')

model  = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)


# Rutas principales
@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/negocio-datos')
def negocio_datos():
    return render_template('negocio-datos.html')

@app.route('/ingenieria-datos')
def ingenieria_datos():
    return render_template('ingenieria-datos.html')

@app.route('/modelo')
def modelo():
    return render_template('modelo.html')

@app.route('/evaluacion')
def evaluacion():
    return render_template('evaluacion.html')

@app.route('/despliegue')
def despliegue():
    return render_template('despliegue.html')

@app.route('/monitoreo')
def monitoreo():
    return render_template('monitoreo.html')

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        # Soportar JSON (AJAX) y form-data
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form
        # Validación backend
        try:
            gender = data['gender']
            age = float(data['age'])
            hypertension = int(data['hypertension'])
            heart_disease = int(data['heart_disease'])
            smoking_history = data['smoking_history']
            bmi = float(data['bmi'])
            HbA1c_level = float(data['HbA1c_level'])
            blood_glucose_level = int(data['blood_glucose_level'])
        except Exception:
            error_msg = 'Datos inválidos o incompletos.'
            if request.is_json:
                return jsonify({'error': error_msg}), 400
            return render_template('index.html', error=error_msg)
        # Validaciones de rango
        errores = []
        if gender not in ['Masculino', 'Femenino', 'Otro']: errores.append('Género inválido.')
        if not (1 <= age <= 120): errores.append('Edad fuera de rango.')
        if hypertension not in [0, 1]: errores.append('Valor de hipertensión inválido.')
        if heart_disease not in [0, 1]: errores.append('Valor de enfermedad cardíaca inválido.')
        if smoking_history not in ['nunca', 'actual', 'anterior', 'alguna vez', 'no actual', 'desconocido']: errores.append('Historial de tabaquismo inválido.')
        if not (10 <= bmi <= 60): errores.append('BMI fuera de rango.')
        if not (3 <= HbA1c_level <= 15): errores.append('HbA1c fuera de rango.')
        if not (50 <= blood_glucose_level <= 500): errores.append('Glucosa fuera de rango.')
        if errores:
            if request.is_json:
                return jsonify({'error': ' '.join(errores)}), 400
            return render_template('index.html', error=' '.join(errores))
        rec = {
            'gender': gender,
            'age': age,
            'hypertension': hypertension,
            'heart_disease': heart_disease,
            'smoking_history': smoking_history,
            'bmi': bmi,
            'HbA1c_level': HbA1c_level,
            'blood_glucose_level': blood_glucose_level
        }
        df = pd.DataFrame([rec])
        df['gender'] = df['gender'].map({'Masculino': 0, 'Femenino': 1, 'Otro': 2})
        # Mapear valores de smoking_history a los usados en el modelo
        smoking_map = {
            'actual': 'current',
            'alguna vez': 'ever',
            'anterior': 'former',
            'nunca': 'never',
            'no actual': 'not current'
        }
        df['smoking_history'] = df['smoking_history'].map(smoking_map)
        df = pd.get_dummies(df, columns=['smoking_history'], drop_first=True)
        dummy_cols = [
            'smoking_history_current',
            'smoking_history_ever',
            'smoking_history_former',
            'smoking_history_never',
            'smoking_history_not current'
        ]
        for col in dummy_cols:
            if col not in df:
                df[col] = 0
        ordered_cols = [
            'gender', 'age', 'hypertension', 'heart_disease', 'bmi', 'HbA1c_level', 'blood_glucose_level'
        ] + dummy_cols
        df = df.reindex(columns=ordered_cols, fill_value=0)
        num_cols = ['age', 'bmi', 'HbA1c_level', 'blood_glucose_level']
        df[num_cols] = scaler.transform(df[num_cols])
        pred = int(model.predict(df)[0])
        if request.is_json:
            return jsonify({'prediction': pred})
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
    # GET
    return render_template('index.html')

@app.errorhandler(404)
def not_found_error(error):
    if request.is_json or request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify({'error': 'Recurso no encontrado.'}), 404
    return render_template('index.html', error='Recurso no encontrado.'), 404

@app.errorhandler(500)
def internal_error(error):
    if request.is_json or request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify({'error': 'Error interno del servidor.'}), 500
    return render_template('index.html', error='Error interno del servidor.'), 500

if __name__ == '__main__':
    app.run(debug=True)