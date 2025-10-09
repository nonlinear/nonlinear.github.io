// Função para criar e gerenciar o canvas dentro de um <section>
function setupCanvasForSection(p, sectionId) {
  const parentId = sectionId; // ID do <section> pai
  const canvasId = `${parentId}-canvas`; // Define o ID do canvas

  // Cria o canvas e anexa ao <section>
  const canvas = p.createCanvas(window.innerWidth, window.innerHeight);
  canvas.parent(parentId);

  // Define o ID do canvas
  const canvasElt = canvas.elt;
  canvasElt.id = canvasId;

  // Ajusta o estilo para corresponder aos atributos HTML
  canvasElt.style.width = `${window.innerWidth}px`;
  canvasElt.style.height = `${window.innerHeight}px`;

  // Retorna o ID do canvas para referência futura
  return canvasId;
}

// Função para redimensionar o canvas
function resizeCanvasForSection(p, canvasId) {
  // Recalcula o tamanho do canvas quando a janela é redimensionada
  p.resizeCanvas(window.innerWidth, window.innerHeight);

  // Ajusta o estilo novamente após o redimensionamento
  const canvas = document.getElementById(canvasId);
  if (canvas) {
    canvas.style.width = `${window.innerWidth}px`;
    canvas.style.height = `${window.innerHeight}px`;
  }
}