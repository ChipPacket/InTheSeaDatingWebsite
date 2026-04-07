//js for newPost.html
let newPost = document.getElementById("newPost");

newPost.addEventListener("submit", function(event) {
    event.preventDefault();

    let editor = document.getElementById("editor");
    let title = document.getElementById("title");
    let author = document.getElementById("author");
    let content = document.getElementById("content");
    let photo = document.getElementById("photo");

    alert(`New post submitted! This form has an editor of ${editor.value}, title of ${title.value}, author(s) of ${author.value}, content of ${content.value}, and photo of ${photo.value}`);
    console.log(
      `This form has an editor of ${editor.value}, title of ${title.value}, author(s) of ${author.value}, content of ${content.value}, and photo of ${photo.value}`
    );
});