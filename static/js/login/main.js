import { login } from './auth.js';

const form = document.getElementById('id-form-login');
const emailInput = document.getElementById('id-email');
const passwordInput = document.getElementById('id-password');
const messageDiv = document.getElementById('id-alert');

form.addEventListener('submit', async (event) => {
  event.preventDefault();

  // Validación manual con Bootstrap
  if (!form.checkValidity()) {
    form.classList.add('was-validated');
    return;
  }

  const email = emailInput.value.trim();
  const password = passwordInput.value.trim();

  const result = await login(email, password); // Llamada a la función de autenticación
  messageDiv.classList.add('d-none'); // Ocultar mensaje de error al iniciar el proceso

  if (result.success) {
    window.location.href = '/'; // Redirigir a la página principal
  } else {
    // Mostrar mensaje de error
    messageDiv.innerHTML = result.message;
    messageDiv.classList.remove('d-none');
  }
});
