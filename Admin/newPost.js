//js for newPost.html
let newPost = document.getElementById("newPost");

newPost.addEventListener("submit", function(event) {
    event.preventDefault();

    let editor = document.getElementById("editor");
    let title = document.getElementById("title");
    let author = document.getElementById("author");
    let content = document.getElementById("content");
    let photo = document.getElementById("photo");

    alert(`New post submitted! This form has an editor of ${editor.value}, title of ${title.value}, author(s) of ${author.value}, content of ${content.value}`);
    console.log(
      `This form has an editor of ${editor.value}, title of ${title.value}, author(s) of ${author.value}, content of ${content.value}`
    );
});

//https://gist.github.com/MirzaLeka/db9386c400fd75edd99f6d5162728f7f
function upload() {
  const fileUploadInput = document.querySelector('.file-uploader');

  /// Validations ///

  if (!fileUploadInput.value) {
    return;
  }

  // using index [0] to take the first file from the array
  const image = fileUploadInput.files[0];

  // check if the file selected is not an image file
  if (!image.type.includes('image')) {
    return alert('Only images are allowed!');
  }

  // check if size (in bytes) exceeds 10 MB
  if (image.size > 10_000_000) {
    return alert('Maximum upload size is 10MB!');
  }

  /// Display the image on the screen ///

  const fileReader = new FileReader();
  fileReader.readAsDataURL(image);

  fileReader.onload = (fileReaderEvent) => {
    const profilePicture = document.querySelector('.profile-picture');
    profilePicture.style.backgroundImage = `url(${fileReaderEvent.target.result})`;
  }

  // upload image to the server or the cloud
}