// Get all category list items
const categoryListItems = document.querySelectorAll('ul li');

// Add event listener to each category list item
categoryListItems.forEach((item) => {
    item.addEventListener('click', () => {
        // Get the category name from the list item
        const categoryName = item.textContent.trim();

        // Create a new category detail page
        const categoryDetailPage = window.open('', '_blank');
        categoryDetailPage.document.write(`
            <h1>Category Detail</h1>
            <p>${categoryName}</p>
        `);
    });
});

