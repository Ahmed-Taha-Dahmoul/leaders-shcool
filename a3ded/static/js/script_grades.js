document.addEventListener('DOMContentLoaded', function() {
    // Get the table element
    var table = document.querySelector('table');

    // Add a class to each table row after a delay
    var rows = table.querySelectorAll('tr');
    var delay = 200;
    rows.forEach(function(row, index) {
        setTimeout(function() {
            row.classList.add('visible');
        }, delay * index);
    });
});
