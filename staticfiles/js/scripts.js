document.addEventListener('DOMContentLoaded', function() {

    // Show message modal if it exists
    const messageModalElement = document.getElementById('messageModal');
    if (messageModalElement) {
        const messageModal = new bootstrap.Modal(messageModalElement);
        messageModal.show();
    }

    // Get all delete buttons
const deleteButtons = document.querySelectorAll('.delete-testimonial-btn');

// Attach the event listener to each delete button
deleteButtons.forEach(function(button) {
    button.addEventListener('click', function() {
        // Store the testimonial ID in a data attribute
        const testimonialId = button.getAttribute('data-id');
        const a = document.querySelector('#confirmDeleteBtnModal');
        a.href = "/testimonials/"+ testimonialId +"/delete/" ;

        // Show the delete modal
        const deleteModalElement = document.getElementById('deleteModal');
        if (deleteModalElement) {
            const deleteModal = new bootstrap.Modal(deleteModalElement);
            deleteModal.show();
        }

        // Event listener for the confirm delete button
        const confirmDeleteBtn = document.getElementById('confirmDeleteBtn');
        if (confirmDeleteBtn) {
            confirmDeleteBtn.addEventListener('click', function() {
                // Close the modal
                if (deleteModalElement) {
                    const deleteModal = new bootstrap.Modal(deleteModalElement);
                    deleteModal.hide();
                }
            });
        }
    });
});});
