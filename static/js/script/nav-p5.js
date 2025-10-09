// Função para criar e gerenciar o canvas dentro de um <section>
function setupCanvasForSection(p, sectionId) {
  const parentId = sectionId; // ID do <section> pai
  const canvasId = `${parentId}-canvas`; // Define o ID do canvas

  // Remove margens e padding do <section> pai
  const section = document.getElementById(parentId);
  if (section) {
    section.style.margin = "0";
    section.style.padding = "0";
    section.style.width = "100%";
    section.style.height = "100%";
    section.style.boxSizing = "border-box"; // Garante que o padding não afete o tamanho
  }

  // Cria o canvas e anexa ao <section>
  const canvas = p.createCanvas(window.innerWidth, window.innerHeight);
  canvas.parent(parentId);

  // Define o ID do canvas
  const canvasElt = canvas.elt;
  canvasElt.id = canvasId;

  // Remove margens e padding do canvas
  canvasElt.style.margin = "0";
  canvasElt.style.padding = "0";
  canvasElt.style.display = "block"; // Remove comportamento inline
  canvasElt.style.boxSizing = "border-box"; // Garante que o padding não afete o tamanho

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