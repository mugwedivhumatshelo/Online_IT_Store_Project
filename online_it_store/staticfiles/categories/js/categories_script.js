document.addEventListener('DOMContentLoaded', event => {
    const categoryList = document.querySelector('ul');
    categoryList.addEventListener('mouseover', event => {
        if (event.target.tagName === 'LI') {
            event.target.style.backgroundColor = '#f5f5f5';
        }
    });
    categoryList.addEventListener('mouseout', event => {
        if (event.target.tagName === 'LI') {
            event.target.style.backgroundColor = '';
        }
    });
});
