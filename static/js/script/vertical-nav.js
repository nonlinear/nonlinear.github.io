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
      id = `slide${(idx + 1).toString().padStart(2, '0')}`;
      section.id = id;
    }
    const link = document.createElement('a');
    link.href = `#${id}`;
    link.textContent = idx + 1;
    nav.appendChild(link);
  });

  // Intersection Observer para .active e .visited com delay + URL hash update
  const navLinks = nav.querySelectorAll('a');
  const visitTimers = {};
  let lastActiveId = null;

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
            // Atualiza o hash na URL se mudou
            if (lastActiveId !== entry.target.id) {
              history.replaceState(null, '', '#' + entry.target.id);
              lastActiveId = entry.target.id;
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
        history.replaceState(null, '', link.getAttribute('href'));
        lastActiveId = targetSection.id;
      }
    });
  });

  // Scroll para o hash ao carregar a página
  const hash = window.location.hash.replace('#', '');
  if (hash) {
    const targetSection = Array.from(sections).find(sec => sec.id === hash);
    if (targetSection) {
      setTimeout(() => {
        targetSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }, 100); // pequeno delay para garantir que o DOM está pronto
    }
  }

  // Após criar os links:
  if (navLinks.length > 0 && !window.location.hash) {
    navLinks[0].classList.add('active');
  }

  // Tippy tooltips para cada link do nav
  navLinks.forEach((link, idx) => {
    const section = sections[idx];
    let label = section.getAttribute('aria-label');
    if (!label) {
      label = `Slide ${idx + 1}`;
    }
    tippy(link, {
      content: label,
      placement: 'right',
      theme: 'light',
      arrow: true,
      delay: [100, 0],
      onShow(instance) {
        instance.popper.querySelector('.tippy-box').classList.add('nav-tooltip');
      }
    });
  });
});