function previewImage(inputId, previewId) {
    var input = document.getElementById(inputId);
    var imagePreview = document.getElementById(previewId);

    var reader = new FileReader();
    
    reader.onload = function(){
        console.log("previewing....")
        imagePreview.src = reader.result;
        imagePreview.style.display = 'block';
    }
    reader.readAsDataURL(input.files[0]);
}