// highlight.js
// Envelopa cada quebra de linha visível em <span class="highlight"> dentro de .content p
// Reage a resize e reprocessa os parágrafos

function highlightTextNodes(node) {
  // Se for nó de texto, processa
  if (node.nodeType === Node.TEXT_NODE) {
    const text = node.nodeValue;
    if (!text.trim()) return;
    // Não processa se já está dentro de um span.highlight
    let parent = node.parentNode;
    while (parent) {
      if (parent.classList && parent.classList.contains('highlight')) return;
      if (parent.tagName === 'SECTION') break;
      parent = parent.parentNode;
    }
    // Divide por quebras de linha
    const lines = text.split(/\n/);
    // Envelopa cada linha
    const frag = document.createDocumentFragment();
    lines.forEach((line, idx) => {
      const span = document.createElement('span');
      span.className = 'highlight';
      span.textContent = line;
      frag.appendChild(span);
      // Adiciona espaço entre spans ao invés de <br>
      if (idx < lines.length - 1) {
        frag.appendChild(document.createTextNode(' '));
      }
    });
    node.parentNode.replaceChild(frag, node);
  } else if (node.nodeType === Node.ELEMENT_NODE) {
    // Não processa se já for highlight
    if (node.classList && node.classList.contains('highlight')) return;
    // Não processa se for marcado para pular
    if (node.hasAttribute && node.hasAttribute('data-skip-highlight')) return;
    // Processa recursivamente os filhos
    // Array.from para evitar problemas ao modificar filhos durante o loop
    Array.from(node.childNodes).forEach(highlightTextNodes);
  }
}

function highlightLineBreaks() {
  // Processa .header
  document.querySelectorAll('section.recap .header').forEach(function (header) {
    highlightTextNodes(header);
  });

  // Processa .content
  document.querySelectorAll('section.recap .content').forEach(function (content) {
    // Marca botões para não processar
    Array.from(content.querySelectorAll('a.button')).forEach(btn => {
      btn.setAttribute('data-skip-highlight', 'true');
    });
    highlightTextNodes(content);
  });
}

// Rodar ao carregar
window.addEventListener('DOMContentLoaded', function() {
  // Pequeno delay para garantir que o conteúdo está renderizado
  setTimeout(highlightLineBreaks, 100);
});
// Rodar ao redimensionar
window.addEventListener('resize', function () {
  // Pequeno debounce para evitar excesso de processamento
  clearTimeout(window._highlightResizeTimeout);
  window._highlightResizeTimeout = setTimeout(highlightLineBreaks, 150);
});
