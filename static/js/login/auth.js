import axiosInstance from '../http/axios-instance.js';

export async function login(email, password) {
  try {

    const formData = new FormData();
    formData.append('email', email);
    formData.append('password', password);
    // Request Post hacia servicio de autenticación - Django
    const response = await axiosInstance.post('/seguridad/auth/', formData);

    if (response.status == 200) {
      return { success: true, data: response.data };
    } else {
      return { success: false, message: response.data?.error || 'Error de conexión con el servidor' };
    }
  } catch (err) {
    return { success: false, message: err.response?.data?.error || 'Error de conexión con el servidor' };
  }
}
