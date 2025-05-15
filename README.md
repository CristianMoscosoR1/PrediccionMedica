# Predicción de Diabetes - Aplicación Flask

Esta aplicación permite predecir la probabilidad de diabetes en pacientes usando un modelo de Regresión Logística entrenado con datos reales. Incluye un formulario web para ingresar los datos y obtener la predicción de manera sencilla.

## Estructura del proyecto

```
PrediccionMedica/
│
├── data-science-template/
│   ├── app/
│   │   ├── app.py                # Aplicación Flask
│   │   └── static/style.css      # Estilos CSS
│   ├── data/
│   │   └── diabetes_prediction_dataset.csv  # Dataset de entrenamiento
│   ├── models/
│   │   ├── logistic_regression_model.pkl   # Modelo entrenado
│   │   └── standard_scaler.pkl            # Escalador
│   ├── src/
│   │   ├── train.py              # Script de entrenamiento
│   │   ├── predict.py            # Script de predicción por línea de comandos
│   │   └── ...                   # Otros scripts auxiliares
│   ├── templates/
│   │   ├── index.html            # Formulario web
│   │   └── result.html           # Resultado de la predicción
│   └── requirements.txt          # Dependencias del proyecto
└── README.md
```

## Instalación y uso

1. **Clona el repositorio y entra a la carpeta:**
   ```bash
   git clone <url-del-repo>
   cd PrediccionMedica
   ```

2. **Instala las dependencias:**
   ```bash
   pip install -r data-science-template/requirements.txt
   ```

3. **Entrena el modelo (solo la primera vez o si cambias el dataset):**
   ```bash
   python data-science-template/src/train.py
   ```
   Esto generará los archivos `logistic_regression_model.pkl` y `standard_scaler.pkl` en la carpeta `models/`.

4. **Ejecuta la aplicación Flask:**
   ```bash
   python data-science-template/app/app.py
   ```
   Luego abre tu navegador en [http://localhost:5000](http://localhost:5000)

## Uso de la aplicación

- Ingresa los datos del paciente en el formulario web.
- Haz clic en "Predecir".
- Verás el resultado: si se predice DIABETES o NO DIABETES.

## Entrenamiento y predicción por línea de comandos

- Para entrenar el modelo: `python data-science-template/src/train.py`
- Para predecir desde la terminal:
  ```bash
  python data-science-template/src/predict.py '{"gender":"Male","age":60,...}'
  ```

## Notas
- El modelo y el preprocesamiento están alineados con los valores y columnas del dataset.
- El formulario web solo permite valores válidos para cada campo.
- Si cambias el dataset, vuelve a ejecutar el script de entrenamiento.

---

Desarrollado por [Tu Nombre].
