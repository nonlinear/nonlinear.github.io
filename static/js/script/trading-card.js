// Mostra status de suporte ao fullscreen
var statusDiv = document.getElementById('fullscreen-status');
var startButton = document.getElementById('startButton');
var cardContainer = document.querySelector('.card-container');
var supportMsg = '';
if (window.screenfull) {
  supportMsg = 'screenfull.js carregado. ';
  supportMsg += 'isEnabled: ' + screenfull.isEnabled;
} else {
  supportMsg = 'screenfull.js NÃO carregado.';
}
statusDiv && (statusDiv.textContent = supportMsg);

startButton && startButton.addEventListener('click', function() {
  if (window.screenfull && screenfull.isEnabled && cardContainer) {
    try {
      screenfull.request(cardContainer);
      statusDiv.textContent = 'Tentou fullscreen (veja se mudou algo na tela)';
    } catch (err) {
      statusDiv.textContent = 'Erro ao tentar fullscreen: ' + err;
    }
  } else {
    statusDiv.textContent = 'Fullscreen não suportado neste device/browser.';
  }
});

if (window.screenfull) {
  screenfull.on('change', function() {
    if (screenfull.isFullscreen) {
      document.body.style.background = '#222';
      statusDiv.textContent = 'Entrou em fullscreen!';
    } else {
      document.body.style.background = 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)';
      statusDiv.textContent = supportMsg;
    }
  });
}
// Modal logic removido

// Phase 1: Basic setup with CSS variables approach
const card = document.querySelector('.card');
const status = document.getElementById('status');
const debug = document.getElementById('debug');

let isGyroActive = false;
let isMouseActive = false;

// Toggle debug with 'd' key
document.addEventListener('keydown', (e) => {
  if (e.key === 'd') {
    debug.classList.toggle('active');
  }
});

// Mouse parallax (desktop)
document.addEventListener('mousemove', (e) => {
  if (isGyroActive) return; // Gyro takes priority

  isMouseActive = true;
  const rect = card.getBoundingClientRect();
  const centerX = rect.left + rect.width / 2;
  const centerY = rect.top + rect.height / 2;

  const deltaX = (e.clientX - centerX) / (rect.width / 2);
  const deltaY = (e.clientY - centerY) / (rect.height / 2);

  updateCardTransform(deltaX * 10, deltaY * 10);
  status && (status.textContent = 'Mouse parallax active');

  updateDebug('mouse', deltaX, deltaY);
});

// Gyroscope (mobile)
function handleOrientation(event) {
  isGyroActive = true;
  isMouseActive = false;

  const beta = event.beta;  // X axis (-180 to 180)
  const gamma = event.gamma; // Y axis (-90 to 90)

  // Normalize and limit range
  const normalizedX = Math.max(-30, Math.min(30, beta)) / 30;
  const normalizedY = Math.max(-30, Math.min(30, gamma)) / 30;

  updateCardTransform(normalizedY * 15, normalizedX * 15);
  status && (status.textContent = 'Gyroscope active');

  updateDebug('gyro', gamma, beta);
}

function updateCardTransform(x, y) {
  // Disable default animation when interactive
  if (isMouseActive || isGyroActive) {
    card.style.animation = 'none';
  }

  // Calculate shadow offset (opposite direction for realism)
  const shadowX = x * 0.3;
  const shadowY = 20 + (y * 0.3);

  // Update CSS variables
  card.style.setProperty('--shadow-x', shadowX);
  card.style.setProperty('--shadow-y', shadowY);

  card.style.transform = `
    translateX(${x}px)
    translateY(${y}px)
    rotateY(${x * 0.5}deg)
    rotateX(${-y * 0.5}deg)
  `;

  // Update debug
  if (debug && debug.classList.contains('active')) {
    document.getElementById('debug-shadow-x').textContent = shadowX.toFixed(2);
    document.getElementById('debug-shadow-y').textContent = shadowY.toFixed(2);
  }
}

function updateDebug(mode, x, y) {
  document.getElementById('debug-mode').textContent = mode;
  document.getElementById('debug-x').textContent = x.toFixed(2);
  document.getElementById('debug-y').textContent = y.toFixed(2);
}
