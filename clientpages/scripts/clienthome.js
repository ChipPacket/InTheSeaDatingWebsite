



async function loadBlogs() {   
    
    //create all the bits to change
    const Title1 = document.getElementById("p1title");
    const Author1 = document.getElementById("p1author");
    const Image1 = document.getElementById("p1image");
    const Title2 = document.getElementById("p2title");
    const Author2 = document.getElementById("p2author");
    const Image2 = document.getElementById("p2image");
    const Title3 = document.getElementById("p3title");
    const Author3 = document.getElementById("p3author");
    const Image3 = document.getElementById("p3image");

    //put them into an array to loop through
    const Titles = [Title1, Title2, Title3];
    const Authors = [Author1, Author2, Author3];
    const Images = [Image1, Image2, Image3];
    

    
    
    //get blog posts and make the most recent 3 pop up
    try {
            const response = await fetch(`${URL}/api/blogPosts`, {
                method: "GET",
                headers: {
                    "Content-Type": "application/json",
                    "x-api-key": KEY 
                }
            });

            const posts = await response.json();
            let index = posts.length;

            for (let i = 0; i < Math.min(3, posts.length); i++){
                
                Titles[i].innerHTML = posts[index- 1 - i].title;
                Authors[i].innerHTML = `By: ${posts[index- 1 - i].author}`;
                Images[i].src = posts[index- 1 - i].image;
            }



    
    }
    catch(error)
    {
        console.error("Uh oh we have an error", error);
    }     
}

//fills the modals with the content from database
async function openModal(i) {

    try {
            const response = await fetch(`${URL}/api/blogPosts`, {
                method: "GET",
                headers: {
                    "Content-Type": "application/json",
                    "x-api-key": KEY 
                }
            });

            const posts = await response.json();
            const post = posts[posts.length - i];

            document.getElementById("modalTitle").innerHTML = post.title;
            document.getElementById("modalContent").innerHTML = post.content;

            const modal = new bootstrap.Modal(document.getElementById('blogModal'));
            modal.show();

    }
    catch(error){
        console.error("Uh oh we have an error", error);
    }
}


window.onload = loadBlogs()


    