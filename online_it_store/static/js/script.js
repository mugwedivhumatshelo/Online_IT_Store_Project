// Add event listener to each nav item
const navItems = document.querySelectorAll('nav li');

navItems.forEach((item) => {
    item.addEventListener('click', () => {
        // Get the nav item text
        const navItemText = item.textContent;

        // Create a new page for the nav item
        const newPage = window.open('', '_blank');
        newPage.document.write(`
            <h1>${navItemText}</h1>
        `);
    });
});

