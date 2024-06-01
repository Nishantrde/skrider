document.addEventListener('DOMContentLoaded', function() {
    const aboutSection = document.querySelector('#about');
    const destinationsSection = document.querySelector('#destinations');
  
    // Add fade-in class to about and destinations sections after a delay
    setTimeout(function() {
      aboutSection.classList.add('fade-in');
      destinationsSection.classList.add('fade-in');
    }, 500); // Adjust delay as needed
  });