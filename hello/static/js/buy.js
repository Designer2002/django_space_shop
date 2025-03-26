buybtn.onclick = function() {
    const weaponId = buybtn.getAttribute("data-weapon-id");
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value; // Get CSRF token

    fetch(`/add-to-cart/${weaponId}/`, {  // Adjust the URL to match your Django URL pattern
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken, // Include CSRF token for security
        },
        body: JSON.stringify({ quantity: 1 }) // You can change this to allow different quantities
    })
    .then(response => {
        if (response.ok) {
            return response.json(); // Parse the JSON response
        }
        throw new Error('Network response was not ok.');
    })
    .then(data => {
        // Handle success (e.g., update the cart UI, show a message)
        console.log('Item added to cart:', data);
        alert('Item added to cart successfully!');
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });
};