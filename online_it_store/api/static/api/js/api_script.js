// Get all product list items
const productListItems = document.querySelectorAll('ul li');

// Add event listener to each product list item
productListItems.forEach((item) => {
    item.addEventListener('click', () => {
        // Get the product name and price from the list item
        const productName = item.textContent.split('(')[0].trim();
        const productPrice = item.textContent.split('(')[1].split(')')[0].trim();

        // Create a new product detail page
        const productDetailPage = window.open('', '_blank');
        productDetailPage.document.write(`
            <h1>Product Detail</h1>
            <p>${productName} (${productPrice})</p>
        `);
    });
});

