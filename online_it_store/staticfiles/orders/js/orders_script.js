// Get all order list items
const orderListItems = document.querySelectorAll('ul li');

// Add event listener to each order list item
orderListItems.forEach((item) => {
    item.addEventListener('click', () => {
        // Get the order id and user from the list item
        const orderId = item.textContent.split(' ')[1];
        const orderUser = item.textContent.split(' ')[3];

        // Create a new order detail page
        const orderDetailPage = window.open('', '_blank');
        orderDetailPage.document.write(`
            <h1>Order Detail</h1>
            <p>Order ${orderId} by ${orderUser}</p>
        `);
    });
});

