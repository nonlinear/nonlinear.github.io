document.addEventListener('DOMContentLoaded', function() {
  // Seleciona o <article class="content"> como base
  const article = document.querySelector('article.content');
  if (!article) return;

  const sections = article.querySelectorAll('section');

  // Cria nav se não existir
  let nav = article.querySelector('nav');
  if (!nav) {
    nav = document.createElement('nav');
    article.insertBefore(nav, article.firstChild);
  }
  nav.innerHTML = '';

  // Cria links dinamicamente para cada section EXISTENTE
  sections.forEach((section, idx) => {
    let id = section.id;
    if (!id) {
      id = `section${(idx + 1).toString().padStart(2, '0')}`;
      section.id = id;
    }
    const link = document.createElement('a');
    link.href = `#${id}`;
    link.textContent = idx + 1;
    nav.appendChild(link);
  });

  // Intersection Observer para .active e .visited com delay
  const navLinks = nav.querySelectorAll('a');
  const visitTimers = {};

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      navLinks.forEach(link => {
        const linkTarget = link.getAttribute('href').replace('#', '');
        if (linkTarget === entry.target.id) {
          if (entry.isIntersecting) {
            link.classList.add('active');
            // Inicia timer para .visited
            if (!visitTimers[linkTarget]) {
              visitTimers[linkTarget] = setTimeout(() => {
                link.classList.add('visited');
              }, 500);
            }
          } else {
            link.classList.remove('active');
            // Cancela timer se saiu antes do delay
            if (visitTimers[linkTarget]) {
              clearTimeout(visitTimers[linkTarget]);
              visitTimers[linkTarget] = null;
            }
          }
        }
      });
    });
  }, { threshold: 0.5 });

  sections.forEach(section => observer.observe(section));

  navLinks.forEach((link, idx) => {
    link.addEventListener('click', function(e) {
      e.preventDefault();
      const targetSection = sections[idx];
      if (targetSection) {
        targetSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  // Após criar os links:
  if (navLinks.length > 0) {
    navLinks[0].classList.add('active');
  }
});