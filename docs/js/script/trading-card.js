// Suporte ao fullscreen
var statusDiv = document.getElementById('fullscreen-status');
var startButton = document.getElementById('startButton');
var card = document.querySelector('.card');
var supportMsg = '';
if (window.screenfull) {
  supportMsg = 'screenfull.js carregado. ';
  supportMsg += 'isEnabled: ' + screenfull.isEnabled;
} else {
  supportMsg = 'screenfull.js NÃO carregado.';
}
if (statusDiv) statusDiv.textContent = supportMsg;

if (startButton) {
  startButton.addEventListener('click', function() {
    if (window.screenfull && screenfull.isEnabled && card) {
      try {
        screenfull.request(card);
        statusDiv && (statusDiv.textContent = 'Tentou fullscreen (veja se mudou algo na tela)');
      } catch (err) {
        statusDiv && (statusDiv.textContent = 'Erro ao tentar fullscreen: ' + err);
      }
    } else {
      statusDiv && (statusDiv.textContent = 'Fullscreen não suportado neste device/browser.');
    }
  });
}

if (window.screenfull) {
  screenfull.on('change', function() {
    if (screenfull.isFullscreen) {
      document.body.style.background = '#222';
      statusDiv && (statusDiv.textContent = 'Entrou em fullscreen!');
    } else {
      document.body.style.background = 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)';
      statusDiv && (statusDiv.textContent = supportMsg);
    }
  });
}

// Parallax e debug
const status = document.getElementById('status');
const debug = document.getElementById('debug');

let isGyroActive = false;
let isMouseActive = false;

// Toggle debug com 'd'
document.addEventListener('keydown', (e) => {
  if (e.key === 'd' && debug) {
    debug.classList.toggle('active');
  }
});

// Mouse parallax (desktop)
document.addEventListener('mousemove', (e) => {
  if (isGyroActive || !card) return;

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

  const beta = event.beta;  // Eixo X (-180 a 180)
  const gamma = event.gamma; // Eixo Y (-90 a 90)

  // Normaliza e limita o intervalo
  const normalizedX = Math.max(-30, Math.min(30, beta)) / 30;
  const normalizedY = Math.max(-30, Math.min(30, gamma)) / 30;

  updateCardTransform(normalizedY * 15, normalizedX * 15);
  status && (status.textContent = 'Gyroscope active');

  updateDebug('gyro', gamma, beta);
}

function updateCardTransform(x, y) {
  if (!card) return;
  // Desabilita animação padrão quando interativo
  if (isMouseActive || isGyroActive) {
    card.style.animation = 'none';
  }

  // Calcula o deslocamento da sombra (direção oposta para realismo)
  const shadowX = x * 0.3;
  const shadowY = 20 + (y * 0.3);

  // Atualiza as variáveis CSS
  card.style.setProperty('--shadow-x', shadowX);
  card.style.setProperty('--shadow-y', shadowY);

  card.style.transform = `
    translateX(${x}px)
    translateY(${y}px)
    rotateY(${x * 0.5}deg)
    rotateX(${-y * 0.5}deg)
  `;

  // Atualiza debug
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
