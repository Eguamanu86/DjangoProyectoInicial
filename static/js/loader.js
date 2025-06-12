document.addEventListener("DOMContentLoaded", function (e) {
  e.preventDefault();
  // Ocultar con transición el elemento con id 'load-content'
  const loadContent = document.getElementById('load-content');
  if (loadContent) {
    setTimeout(() => {
      loadContent.style.display = 'none';
    }, 300);
  }
});
