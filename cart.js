// cart.js

// Sample data for products (you can replace this with actual data)
const products = [
    { id: 1, name: 'Product 1', price: 10 },
    { id: 2, name: 'Product 2', price: 20 },
    // Add more products as needed
];

// Cart to store selected items
const cart = [];

// Function to update cart items and total
function updateCart() {
    const cartItemsContainer = document.querySelector('.cart-items');
    const cartTotal = document.querySelector('.cart-total p');
    cartItemsContainer.innerHTML = '';
    
    let total = 0;

    cart.forEach(item => {
        const cartItem = document.createElement('div');
        cartItem.classList.add('cart-item');
        cartItem.innerHTML = `
            <span>${item.name}</span>
            <span>$${item.price}</span>
        `;
        cartItemsContainer.appendChild(cartItem);

        total += item.price;
    });

    cartTotal.textContent = `Total: $${total}`;
}

// Function to add product to cart
function addToCart(productId) {
    const product = products.find(item => item.id === productId);
    if (product) {
        cart.push(product);
        updateCart();
    }
}

// Initialize event listeners
document.addEventListener('DOMContentLoaded', () => {
    const productButtons = document.querySelectorAll('.product button');
    productButtons.forEach(button => {
        button.addEventListener('click', () => {
            const productId = parseInt(button.getAttribute('data-id'));
            addToCart(productId);
        });
    });
});
