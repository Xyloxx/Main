document.addEventListener("DOMContentLoaded", function() {
    const cartItems = [];
    const itemsContainer = document.querySelector(".cart-items");
    const totalElement = document.getElementById("total");
    const taxElement = document.getElementById("tax");
    const grandTotalElement = document.getElementById("grand-total");

    // Example product data
    const products = [
        { name: "Product 1", price: 10.99 },
        { name: "Product 2", price: 5.99 },
        // Add more products here
    ];

    // Function to update cart information
    function updateCart() {
        itemsContainer.innerHTML = "";
        let total = 0;

        cartItems.forEach(item => {
            const listItem = document.createElement("li");
            listItem.textContent = `${item.name} - $${item.price.toFixed(2)}`;
            itemsContainer.appendChild(listItem);
            total += item.price;
        });

        const tax = total * 0.1; // Example tax calculation (10%)
        const grandTotal = total + tax;

        totalElement.textContent = total.toFixed(2);
        taxElement.textContent = tax.toFixed(2);
        grandTotalElement.textContent = grandTotal.toFixed(2);
    }

    // Function to add an item to the cart
    function addToCart(productIndex) {
        const selectedProduct = products[productIndex];
        cartItems.push(selectedProduct);
        updateCart();
    }

    // Add event listeners to product buttons
    const productButtons = document.querySelectorAll(".add-to-cart");
    productButtons.forEach((button, index) => {
        button.addEventListener("click", () => {
            addToCart(index);
        });
    });
});
