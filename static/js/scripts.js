document.addEventListener('DOMContentLoaded', function() {
    // Form validation
    const form = document.getElementById('transaction-form');
    if (form) {
        form.addEventListener('submit', function(event) {
            // Check if all required fields are filled
            const amount = document.getElementById('amount').value;
            const category = document.getElementById('category').value;
            const date = document.getElementById('date').value;

            if (!amount || !category || !date) {
                event.preventDefault();
                alert('All fields are required!');
            }
        });
    }
    
    // Additional interactivity can be added here
    console.log('JavaScript is properly linked and working!');
});

