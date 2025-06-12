import axios from 'https://cdn.jsdelivr.net/npm/axios@1.6.7/+esm';

// Crear instancia de Axios
const axiosInstance = axios.create({
  headers: {
    'X-CSRFToken': Cookies.get('csrftoken')
  }
});

// Interceptores para loader global (opcional)
axiosInstance.interceptors.request.use(config => {
  const loader = document.getElementById('load-content');
  if (loader) {
    loader.style.display = 'flex'; // O 'block' según tu HTML/CSS
    loader.style.opacity = 1;
  }
  return config;
}, error => {
  const loader = document.getElementById('load-content');
  if (loader) {
    loader.style.display = 'none';
    loader.style.opacity = 0;
  }
  return Promise.reject(error);
});

axiosInstance.interceptors.response.use(response => {
  const loader = document.getElementById('load-content');
  if (loader) {
    loader.style.opacity = 0;
    setTimeout(() => { loader.style.display = 'none'; }, 200);
  }
  return response;
}, error => {
  const loader = document.getElementById('load-content');
  if (loader) {
    loader.style.opacity = 0;
    setTimeout(() => { loader.style.display = 'none'; }, 200);
  }
  return Promise.reject(error);
});

export default axiosInstance;
