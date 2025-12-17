document.addEventListener("DOMContentLoaded", function () {
  const previews = document.querySelectorAll('.illustration-preview .preview');
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });
    previews.forEach(preview => observer.observe(preview));
  } else {
    // Fallback: mostra tudo se não suportar IntersectionObserver
    previews.forEach(preview => preview.classList.add('visible'));
  }
});
