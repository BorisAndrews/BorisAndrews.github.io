// scripts/script.js
document.addEventListener("DOMContentLoaded", function() {
    const typingElement = document.querySelector('.typing-content');
    const text = typingElement.innerHTML;
    let index = 0;

    typingElement.innerHTML = ''; // Clear the initial text

    function typeText() {
        if (index < text.length) {
            typingElement.innerHTML += text[index] === ' ' ? '&nbsp;' : text[index];
            index++;
            setTimeout(typeText, 100); // Adjust the speed here (in milliseconds)
        }
    }

    typeText(); // Start the typing effect
});