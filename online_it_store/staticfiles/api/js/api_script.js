// Add event listener to navigation links
document.querySelectorAll('nav a').forEach(link => {
    link.addEventListener('click', event => {
        event.preventDefault();
        const url = link.getAttribute('href');
        fetch(url)
            .then(response => response.text())
            .then(html => {
                document.body.innerHTML = html;
            })
            .catch(error => console.error(error));
    });
});

// Add event listener to product list items
document.querySelectorAll('.product-list-item').forEach(item => {
    item.addEventListener('mouseover', event => {
        item.style.backgroundColor = '#f5f5f5';
    });
    item.addEventListener('mouseout', event => {
        item.style.backgroundColor = '';
    });
});

// Add event listener to product list pagination
document.querySelectorAll('.pagination a').forEach(link => {
    link.addEventListener('click', event => {
        event.preventDefault();
        const url = link.getAttribute('href');
        fetch(url)
            .then(response => response.text())
            .then(html => {
                document.body.innerHTML = html;
            })
            .catch(error => console.error(error));
    });
});

