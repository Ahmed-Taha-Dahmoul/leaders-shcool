document.addEventListener('DOMContentLoaded', function() {
    // Get the ul element
    var classesList = document.querySelector('ul.classes');

    // Add a class to each li element after a delay
    var listItems = classesList.querySelectorAll('li');
    var delay = 200;
    listItems.forEach(function(item, index) {
        setTimeout(function() {
            item.classList.add('visible');
        }, delay * index);
    });
});
