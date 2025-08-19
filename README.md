# 🩺 Predicción de Diabetes &mdash; App Web Flask

<p align="center">
  <img src="data-science-template/app/static/media/hero.jpg" alt="Hero" width="60%"/>
</p>

<p align="center">
  <b>Predice el riesgo de diabetes de manera rápida, visual y profesional.</b><br>
  <a href="#demo">Ver demo</a> • <a href="#instalacion">Instalación</a> • <a href="#tecnologias">Tecnologías</a>
</p>

---

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?logo=python"/>
  <img src="https://img.shields.io/badge/Flask-%20web%20app-000?logo=flask"/>
  <img src="https://img.shields.io/badge/Model-Logistic%20Regression-green"/>
  <img src="https://img.shields.io/badge/Deploy-Render-430098?logo=render"/>
</p>

---

## 📋 Tabla de Contenidos
- [Descripción](#descripcion)
- [Demo](#demo)
- [Estructura del Proyecto](#estructura)
- [Instalación](#instalacion)
- [Uso](#uso)
- [Entrenamiento y CLI](#cli)
- [Tecnologías](#tecnologias)
- [Notas](#notas)
- [Créditos](#creditos)

---

## ✨ Descripción <a name="descripcion"></a>
Esta aplicación web permite predecir la probabilidad de diabetes en pacientes usando un modelo de Regresión Logística entrenado con datos reales. Incluye:
- Formulario web validado (frontend y backend)
- Predicción instantánea vía AJAX (sin recargar la página)
- Mensajes claros, recomendaciones y métricas del modelo
- Diseño responsive y moderno

---

## 🚀 Demo <a name="demo"></a>

<p align="center">
  <img src="data-science-template/app/static/media/hero.jpg" alt="Demo" width="60%"/>
</p>

Prueba la app localmente o despliega en Render para verla en acción.

---

## 🗂️ Estructura del Proyecto <a name="estructura"></a>

```
PrediccionMedica/
├── data-science-template/
│   ├── app/
│   │   ├── app.py                # Backend Flask
│   │   └── static/
│   │       ├── style.css         # Estilos
│   │       └── prediccion.js     # Lógica AJAX y validación
│   ├── models/
│   │   ├── logistic_regression_model.pkl
│   │   └── standard_scaler.pkl
│   ├── templates/
│   │   ├── index.html            # Formulario web
│   │   └── result.html           # Resultado (legacy)
│   ├── src/
│   │   ├── train.py              # Entrenamiento
│   │   └── predict.py            # Predicción CLI
│   └── requirements.txt
└── README.md
```

---

## ⚡ Instalación <a name="instalacion"></a>

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/CristianMoscosoR1/PrediccionMedica.git
   cd PrediccionMedica
   ```
2. **Instala dependencias:**
   ```bash
   pip install -r data-science-template/requirements.txt
   ```
3. **(Opcional) Entrena el modelo:**
   ```bash
   python data-science-template/src/train.py
   ```
4. **Ejecuta la app Flask:**
   ```bash
   python data-science-template/app/app.py
   ```
5. **Abre tu navegador:**
   [http://localhost:5000/formulario](http://localhost:5000/formulario)

---

## 🖱️ Uso <a name="uso"></a>
- Ingresa los datos del paciente en el formulario web.
- Haz clic en <b>Predecir</b>.
- Verás el resultado y recomendaciones al instante.

---

## 🛠️ Entrenamiento y CLI <a name="cli"></a>
- Entrena el modelo:  
  `python data-science-template/src/train.py`
- Predice desde la terminal:  
  `python data-science-template/src/predict.py '{"gender":"Male","age":60,...}'`

---

## 🧰 Tecnologías <a name="tecnologias"></a>
- Python 3.11
- Flask
- Scikit-learn
- HTML5, CSS3, JavaScript (AJAX puro)
- Render (deploy)

---

## 📝 Notas <a name="notas"></a>
- El modelo y el preprocesamiento están alineados con los valores y columnas del dataset.
- El formulario web solo permite valores válidos para cada campo.
- Si cambias el dataset, vuelve a ejecutar el script de entrenamiento.
- Puedes personalizar el diseño y las métricas fácilmente.

---

## 👨‍💻 Créditos <a name="creditos"></a>
Desarrollado por **Cristian Moscoso**.

<p align="center">
  <img src="https://img.shields.io/github/stars/CristianMoscosoR1/PrediccionMedica?style=social"/>
  <img src="https://img.shields.io/github/forks/CristianMoscosoR1/PrediccionMedica?style=social"/>
</p>
