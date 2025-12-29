// highlight.js
// Envelopa cada quebra de linha visível em <span class="highlight"> dentro de .content p
// Reage a resize e reprocessa os parágrafos

function highlightTextNodes(node) {
  // Se for nó de texto, processa
  if (node.nodeType === Node.TEXT_NODE) {
    const text = node.nodeValue;
    if (!text.trim()) return;
    // Divide por quebras de linha
    const lines = text.split(/\n/);
    // Envelopa cada linha
    const frag = document.createDocumentFragment();
    lines.forEach((line, idx) => {
      const span = document.createElement('span');
      span.className = 'highlight';
      span.textContent = line;
      frag.appendChild(span);
      if (idx < lines.length - 1) frag.appendChild(document.createElement('br'));
    });
    node.parentNode.replaceChild(frag, node);
  } else if (node.nodeType === Node.ELEMENT_NODE) {
    // Não processa se já for highlight
    if (node.classList && node.classList.contains('highlight')) return;
    // Processa recursivamente os filhos
    // Array.from para evitar problemas ao modificar filhos durante o loop
    Array.from(node.childNodes).forEach(highlightTextNodes);
  }
}

function highlightLineBreaks() {
  document.querySelectorAll('.slide-content, .slide-header').forEach(function (root) {
    highlightTextNodes(root);
  });
}

// Rodar ao carregar
window.addEventListener('DOMContentLoaded', highlightLineBreaks);
// Rodar ao redimensionar
window.addEventListener('resize', function () {
  // Pequeno debounce para evitar excesso de processamento
  clearTimeout(window._highlightResizeTimeout);
  window._highlightResizeTimeout = setTimeout(highlightLineBreaks, 150);
});
