
```javascript
document.addEventListener('DOMContentLoaded', function() {
    const sidebarToggle = document.getElementById('sidebar-toggle');
    const sidebar = document.getElementById('sidebar');

    if (sidebarToggle && sidebar) {
        sidebarToggle.addEventListener('click', () => {
            sidebar.classList.toggle('visible');
            // Optionally, you might want to adjust main content padding or add an overlay
            // For this basic example, we'll just toggle the sidebar's visibility class
        });
    }

    // Optional: Close sidebar when clicking outside of it
    document.addEventListener('click', function(event) {
        // Check if the sidebar is visible and the click is outside the sidebar
        if (sidebar && sidebar.classList.contains('visible') && !sidebar.contains(event.target) && !sidebarToggle.contains(event.target)) {
            sidebar.classList.remove('visible');
        }
    });

    // Optional: Close sidebar when the window is resized beyond a certain breakpoint
    window.addEventListener('resize', function() {
        if (window.innerWidth > 768 && sidebar && sidebar.classList.contains('visible')) {
            sidebar.classList.remove('visible');
        }
    });
});
```