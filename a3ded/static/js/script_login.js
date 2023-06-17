// JavaScript code for the login page animation

// Select the title element
const title = document.querySelector('.title');

// Add event listener to the title for animation
title.addEventListener('mouseenter', () => {
    title.style.transform = 'scale(1.1)';
});

title.addEventListener('mouseleave', () => {
    title.style.transform = 'scale(1)';
});
