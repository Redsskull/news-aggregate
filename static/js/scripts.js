document.addEventListener('DOMContentLoaded', function() {
    const messageModalElement = document.getElementById('messageModal');
    if (messageModalElement) {
        const messageModal = new bootstrap.Modal(messageModalElement);
        messageModal.show();
    }
});
