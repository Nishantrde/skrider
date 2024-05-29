// JavaScript for scroll event
window.addEventListener('scroll', function() {
    const h2Elements = document.querySelectorAll('h2');
  
    h2Elements.forEach(function(h2) {
      // Check if the element is in the viewport
      const bounding = h2.getBoundingClientRect();
  
      // If the h2 element is in the viewport, add the fade-in class
      if (
        bounding.top >= 0 &&
        bounding.bottom <= (window.innerHeight || document.documentElement.clientHeight)
      ) {
        h2.classList.add('fade-in');
      } else {
        h2.classList.remove('fade-in');
      }
    });
  });
  document.addEventListener('DOMContentLoaded', function() {
    const aboutSection = document.querySelector('#about');
    const destinationsSection = document.querySelector('#destinations');
  
    // Add fade-in class to about and destinations sections after a delay
    setTimeout(function() {
      aboutSection.classList.add('fade-in');
      destinationsSection.classList.add('fade-in');
    }, 500); // Adjust delay as needed
  });