

const postid = localStorage.getItem("PostId");
//const postid = 11;
const adminid = 1; //will update when we make admin login page
async function loadPosts() {    
    const elementTitle = document.getElementById("displayTitle");
    const elementAuthor = document.getElementById("displayAuthor");
    const elementContent = document.getElementById("displayContent");
    const elementImage = document.getElementById("displayImage");
    const elementImageURL = document.getElementById("displayImageURL");

    try {
            const response = await fetch(`${URL}/api/blogPosts`, {
                method: "GET",
                headers: {
                    "Content-Type": "application/json",
                    "x-api-key": KEY 
                }
            });
            if (response.ok) 
                {
                    const posts = await response.json();
                    const post = posts.find(p => p.id == postid);
                        
                            //update view
                            elementTitle.innerHTML = post.title;
                            elementAuthor.innerHTML = post.author;
                            elementContent.innerHTML = post.content;
                            elementImage.src = post.image;
                            elementImageURL.innerHTML = post.image;

                            //update form
                            document.getElementById("title").value = post.title;
                            document.getElementById("author").value = post.author;
                            document.getElementById("content").value = post.content;
                            document.getElementById("photo").value = post.image;
                };
            }

    catch(error)
    {
        console.error("Uh oh we have an error", error);
    }      
}

document.getElementById("editPost").addEventListener("submit", async function (e) {
    e.preventDefault();

    const data = {
        id: postid,
        adminID: adminid, 
        author: document.getElementById("authors").value,
        title: document.getElementById("title").value,
        content: document.getElementById("content").value,
        image: document.getElementById("photo").value,
    };



    try {
        const response = await fetch(`${URL}/api/blogPosts`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
                "x-api-key": KEY
            },
            body: JSON.stringify(data)
        });

        if (response.ok) {
            alert("Post updated! yay");
            document.getElementById("login").reset();
            loadPosts();    
        }

    } catch (error) {
        console.error(error);
        alert("UH OH.");
    }
    
});

window.onload = loadPosts;