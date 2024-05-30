function previewImage(event) {
    var reader = new FileReader();
    reader.onload = function(){
        var imagePreview = document.getElementById('image-preview');
        imagePreview.src = reader.result;
        imagePreview.style.display = 'block';
    }
    reader.readAsDataURL(event.target.files[0]);
}
