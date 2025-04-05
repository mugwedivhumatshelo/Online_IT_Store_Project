console.log('Hello, World!');

// Add event listener to the login form
document.querySelector('form').addEventListener('submit', (e) => {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    // Send a POST request to the server with the username and password
    fetch('/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            username,
            password,
        }),
    })
    .then((response) => response.json())
    .then((data) => {
        if (data.success) {
            // Login successful, redirect to the dashboard
            window.location.href = '/dashboard/';
        } else {
            // Login failed, display an error message
            alert('Invalid username or password');
        }
    })
    .catch((error) => {
        console.error(error);
    });
});

// Add event listener to the register form
document.querySelector('form').addEventListener('submit', (e) => {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirm_password').value;
    // Send a POST request to the server with the username, email, password, and confirm password
    fetch('/register/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            username,
            email,
            password,
            confirmPassword,
        }),
    })
    .then((response) => response.json())
    .then((data) => {
        if (data.success) {
            // Registration successful, redirect to the login page
            window.location.href = '/login/';
        } else {
            // Registration failed, display an error message
            alert('Invalid registration');
        }
    })
    .catch((error) => {
        console.error(error);
    });
});

