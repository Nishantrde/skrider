 // JavaScript for rendering star ratings dynamically
 document.addEventListener('DOMContentLoaded', function() {
    var ratings = document.querySelectorAll('.rating');
    ratings.forEach(function(rating) {
        var stars = '';
        var ratingValue = parseInt(rating.getAttribute('data-rating'));
        for (var i = 5; i >= 1; i--) {
            if (i <= ratingValue) {
                stars += '<i class="fas fa-star"></i>';
            } else {
                stars += '<i class="far fa-star"></i>';
            }
        }
        rating.innerHTML = stars;
    });
});