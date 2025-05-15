document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('form-prediccion');
  const errorDiv = document.getElementById('error-messages');
  const resultadoDiv = document.getElementById('resultado-prediccion');

  function validarCampos(formData) {
    const errores = [];
    // Validaciones por campo
    if (!formData.gender) errores.push('Seleccione un género.');
    const edad = Number(formData.age);
    if (!formData.age || isNaN(edad) || edad < 1 || edad > 120) errores.push('Edad fuera de rango (1-120).');
    if (!['0', '1'].includes(formData.hypertension)) errores.push('Seleccione si tiene hipertensión.');
    if (!['0', '1'].includes(formData.heart_disease)) errores.push('Seleccione si tiene enfermedad cardíaca.');
    if (!formData.smoking_history) errores.push('Seleccione historial de tabaquismo.');
    const bmi = Number(formData.bmi);
    if (!formData.bmi || isNaN(bmi) || bmi < 10 || bmi > 60) errores.push('BMI fuera de rango (10-60).');
    const hba1c = Number(formData.HbA1c_level);
    if (!formData.HbA1c_level || isNaN(hba1c) || hba1c < 3 || hba1c > 15) errores.push('HbA1c fuera de rango (3-15).');
    const glucosa = Number(formData.blood_glucose_level);
    if (!formData.blood_glucose_level || isNaN(glucosa) || glucosa < 50 || glucosa > 500) errores.push('Glucosa fuera de rango (50-500).');
    return errores;
  }

  form && form.addEventListener('submit', function (e) {
    e.preventDefault();
    errorDiv.innerHTML = '';
    resultadoDiv.style.display = 'none';
    resultadoDiv.innerHTML = '';

    // Obtener datos
    const formData = {
      gender: form.gender.value,
      age: form.age.value,
      hypertension: form.hypertension.value,
      heart_disease: form.heart_disease.value,
      smoking_history: form.smoking_history.value,
      bmi: form.bmi.value,
      HbA1c_level: form.HbA1c_level.value,
      blood_glucose_level: form.blood_glucose_level.value
    };
    // Validar
    const errores = validarCampos(formData);
    if (errores.length > 0) {
      errorDiv.innerHTML = errores.map(e => `<div class='error'>${e}</div>`).join('');
      return;
    }
    // Enviar por fetch
    fetch('/formulario', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'X-Requested-With': 'XMLHttpRequest' },
      body: JSON.stringify(formData)
    })
      .then(res => res.json())
      .then(data => {
        if (data.error) {
          errorDiv.innerHTML = `<div class='error'>${data.error}</div>`;
        } else {
          resultadoDiv.style.display = 'block';
          if (data.prediction === 1) {
            resultadoDiv.innerHTML = `<h2>Resultado:</h2><p style='color:red;'><strong>Se predice DIABETES.</strong></p><p><b>Recomendación:</b> Consulte a su médico y siga hábitos saludables.</p>`;
          } else {
            resultadoDiv.innerHTML = `<h2>Resultado:</h2><p style='color:green;'><strong>No se predice diabetes.</strong></p><p><b>Recomendación:</b> Mantenga sus hábitos saludables y realice chequeos periódicos.</p>`;
          }
        }
      })
      .catch(() => {
        errorDiv.innerHTML = `<div class='error'>Error de conexión. Intente más tarde.</div>`;
      });
  });
});