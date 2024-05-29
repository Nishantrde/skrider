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
  