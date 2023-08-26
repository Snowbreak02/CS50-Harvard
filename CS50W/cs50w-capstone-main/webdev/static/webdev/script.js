document.addEventListener('DOMContentLoaded', function() {
    const search_input = document.querySelector('#search-input');

    // Shortcut key
    onkeydown = event => {

        if (event.ctrlKey && event.key === '/') {
            search_input.focus();
        } else if (event.key === 'Escape') {
            if (document.activeElement === search_input) {
                search_input.blur();
            }
        }
    }
});