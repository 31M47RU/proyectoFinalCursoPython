function isStockEmpty(product) {
  const stock = product.attributes["data-stock"].value;
  return stock === "0";
}

function addingCssClassToHTML(product, className) {
  product.classList.add(className);
}

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
