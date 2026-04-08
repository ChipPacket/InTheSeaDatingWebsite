
async function loadPosts() {
    
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
                    const container = document.getElementById("usersprofiles");


                        posts.forEach(post => {
      
                            const card = document.createElement("div");

                            card.className = "col-md-4 mb-4";
                            
                            //card for each user
                            // button will redirect to user page as well as storing the users id again
                            card.innerHTML = `
                                <div class="card w-100">
                                    <div class="card-body">
                                        <h5 class="card-title">Post ID:${post.id}</h5>
                                        <p class="card-text">Title: ${post.title}</p>
                                        <a href="#" class="btn btn-primary" onclick="deletePost('${post.id}')">Delete Post</a>
                                    </div>
                                </div>
                            `;

                            container.appendChild(card);

                            
                    });
                };
            }

    catch(error)
    {
        console.error(error);
    }        
}

async function deletePost(postid) {
    
    const data = {
        id: postid
    }
    

    try {
            const response = await fetch(`${URL}/api/blogPosts`, {
                method: "DELETE",
                headers: {
                    "Content-Type": "application/json",
                    "x-api-key": KEY
                },
                body: JSON.stringify(data)
            });

        

            if (response.ok) 
                {
                    window.location.href = "adminPostlist.html"
                };
            }

    catch(error)
    {
        console.error(error);
        alert("error");
    }        
}

window.onload = loadPosts;