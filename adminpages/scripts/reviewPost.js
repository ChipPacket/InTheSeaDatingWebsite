async function DltPosts(postid) {
    
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
                    window.location.href = "reviewPost.html"
                };
            }

    catch(error)
    {
        console.error(error);
        alert("error");
    }        
}

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
                    const container = document.getElementById("table");


                        posts.forEach(post => {


                            const entry = document.createElement("tr");
                
                            //table for each post

                            entry.innerHTML = `
                                    <td>${post.id}</td>
                                    <td>${post.title}</td>
                                    <td>${post.author}</td>
                                    <td>${post.dateOfPublish}</td>
                                    <td><button class="bt1" onclick="ViewPosts(${post.id})">Edit</button></td>
                                    <td><button class="btn btn-danger" onclick="DltPosts(${post.id})">Delete</button></td>
                            `;

                            container.appendChild(entry);

                            
                    });
                };
            }

    catch(error)
    {
        console.error(error);
    }        
}

function ViewPosts(postid) {

    localStorage.setItem("PostId", postid);
    window.location.href = "editPost.html"
}



window.onload = loadPosts;