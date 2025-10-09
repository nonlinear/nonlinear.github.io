let sketch = function (p) {
  let canvasId; // Variável para armazenar o ID do canvas

  p.setup = function () {
    // Configura o canvas para o <section> com ID "hedgehog"
    canvasId = setupCanvasForSection(p, "hedgehog");

    p.smooth();
    p.noLoop();
  };

  p.windowResized = function () {
    // Redimensiona o canvas quando a janela é redimensionada
    resizeCanvasForSection(p, canvasId);
  };

  p.draw = function () {
    p.background("#222");
    // Adicione sua lógica de desenho aqui
  };
};
new p5(sketch);
