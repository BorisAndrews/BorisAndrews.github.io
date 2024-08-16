// scripts/script.js
document.addEventListener("DOMContentLoaded", function() {
  const typingElement = document.getElementById('type');
  const text = typingElement.innerText;
  let index = 0;

  typingElement.innerText = ''; // Clear the initial text

  function typeText() {
      if (index < text.length) {
          typingElement.innerText += text[index];
          index++;
          setTimeout(typeText, 100); // Adjust the speed here (in milliseconds)
      }
  }

  typeText(); // Start the typing effect
});