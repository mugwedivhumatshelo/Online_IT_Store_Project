// Get all user list items
const userListItems = document.querySelectorAll('ul li');

// Add event listener to each user list item
userListItems.forEach((item) => {
    item.addEventListener('click', () => {
        // Get the user username and email from the list item
        const userUsername = item.textContent.split(' ')[0];
        const userEmail = item.textContent.split(' ')[2];

        // Create a new user detail page
        const userDetailPage = window.open('', '_blank');
        userDetailPage.document.write(`
            <h1>User Detail</h1>
            <p>Username: ${userUsername}</p>
            <p>Email: ${userEmail}</p>
        `);
    });
});

