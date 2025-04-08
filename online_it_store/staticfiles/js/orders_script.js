document.addEventListener('DOMContentLoaded', event => {
    const orderList = document.querySelector('ul');
    if (orderList) {
        orderList.addEventListener('mouseover', event => {
            if (event.target.tagName === 'LI') {
                event.target.style.backgroundColor = '#f5f5f5';
            }
        });
        orderList.addEventListener('mouseout', event => {
            if (event.target.tagName === 'LI') {
                event.target.style.backgroundColor = '';
            }
        });
    }

    const orderDetail = document.querySelector('.order-detail');
    if (orderDetail) {
        orderDetail.addEventListener('mouseover', event => {
            orderDetail.style.boxShadow = '0 0 20px rgba(0, 0, 0, 0.2)';
        });
        orderDetail.addEventListener('mouseout', event => {
            orderDetail.style.boxShadow = '0 0 10px rgba(0, 0, 0, 0.1)';
        });
    }
});
