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
            var testimonialId = button.getAttribute('data-testimonial-id');

            // Store the testimonial ID in a hidden input in the modal
            document.getElementById('testimonialIdInput').value = testimonialId;

            // Show the delete modal
            var deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));
            deleteModal.show();
        });
    });

    // Event listener for the confirm delete button
    document.getElementById('confirmDeleteBtn').addEventListener('click', function() {
        // Get the testimonial ID from the hidden input
        var testimonialId = document.getElementById('testimonialIdInput').value;

        // Use AJAX to delete the testimonial
        fetch('/testimonials/<int:testimonial_id>/delete/' + testimonialId, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value,
            },
        })
        .then(response => response.json())
        .then(data => {
            // Handle the response or perform additional actions
            console.log('Testimonial deleted successfully:', data);

            // Close the modal
            const deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));
            deleteModal.hide();

        })
        .catch(error => console.error('Error:', error));
    });
});
