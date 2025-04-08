document.addEventListener('DOMContentLoaded', event => {
    const userList = document.querySelector('ul');
    if (userList) {
        userList.addEventListener('mouseover', event => {
            if (event.target.tagName === 'LI') {
                event.target.style.backgroundColor = '#f5f5f5';
            }
        });
        userList.addEventListener('mouseout', event => {
            if (event.target.tagName === 'LI') {
                event.target.style.backgroundColor = '';
            }
        });
    }

    const userDetail = document.querySelector('.user-detail');
    if (userDetail) {
        userDetail.addEventListener('mouseover', event => {
            userDetail.style.boxShadow = '0 0 20px rgba(0, 0, 0, 0.2)';
        });
        userDetail.addEventListener('mouseout', event => {
            userDetail.style.boxShadow = '0 0 10px rgba(0, 0, 0, 0.1)';
        });
    }
});

