// Function to confirm form submission
function confirmSubmission(event) {
    if (!confirm("Are you sure you want to submit this form?")) {
        event.preventDefault(); // Prevent submission if canceled
    }
}

// Attach the confirmSubmission function to the form's submit event
document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    if (form) {
        form.addEventListener("submit", confirmSubmission);
    }

    // Flash message fade-out effect
    const flashMessage = document.querySelector(".flash-message");
    if (flashMessage) {
        setTimeout(() => {
            flashMessage.style.transition = "opacity 1s ease";
            flashMessage.style.opacity = "0";
        }, 3000); // Delay for 3 seconds

        setTimeout(() => {
            flashMessage.style.display = "none";
        }, 4000); // Hide completely after 4 seconds
    }

    // Optional: Clear form fields after submission
    form.addEventListener("submit", function () {
        setTimeout(() => {
            form.reset();
        }, 1000); // Clear form 1 second after submission
    });
});
