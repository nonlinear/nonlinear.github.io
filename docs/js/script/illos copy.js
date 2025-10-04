const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, index) => {
      if (entry.isIntersecting) {
        setTimeout(() => {
          entry.target.classList.add('in-view');
        }, index * 300);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });
  document.querySelectorAll('.illo-wrapper').forEach(wrapper => {
    observer.observe(wrapper);
  });
  document.querySelectorAll('.illo-wrapper').forEach(wrapper => {
    const img = wrapper.querySelector('img');
    const isTouch = 'ontouchstart' in window || navigator.maxTouchPoints > 0;

    if (isTouch) {
      let animActive = false;
      wrapper.addEventListener('touchstart', () => {
        if (!animActive) {
          img.src = img.dataset.anim;
          animActive = true;
        } else {
          img.src = img.dataset.static;
          animActive = false;
        }
      });
    } else {
      const activate = () => {
        img.src = img.dataset.anim;
      };
      const deactivate = () => {
        img.src = img.dataset.static;
      };
      wrapper.addEventListener('mouseenter', activate);
      wrapper.addEventListener('mouseleave', deactivate);
    }
  });