function isStockEmpty(product) {
  const stock = product.dataset.stock;
  return stock === 0;
}

document.addEventListener("DOMContentLoaded", function () {
  const btnCarrito = document.getElementById("btn-carrito");

  btnCarrito.addEventListener("click", function () {
    const carro = document.getElementById("carro");
    carro.classList.toggle("c-active");
  });

  document.getElementById('c-finish').addEventListener('click', function() {
    window.open('https://wa.me/3878643194?text=Tu%20pedido%20ha%20sido%20realizado', '_blank');
});
});

function main() {
  const productList = document.getElementById("product-list");
  for (let i = 0; i < productList.children.length; i++) {
    const product = productList.children[i];
    if (isStockEmpty(product)) {
      addingCssClassToHTML(product, "empty");
    }
  }
}

main();
