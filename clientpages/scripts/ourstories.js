
async function loadBlogs() {   
    
     if (response.ok) 
                {
                    const users = await response.json();
                    const container = document.getElementById("usersprofiles");


                        users.forEach(user => {
                            
                            //defualt
                            let image = user.image
                            if (image == "")
                                {
                                    image = "../assets/pfp.jpg"
                                    console.log("check");
                                }


                            const card = document.createElement("div");

                            card.className = "col-md-4 mb-4";
                            
                            //card for each user
                            // button will redirect to user page as well as storing the users id again
                            card.innerHTML = `
                                <div class="card my-3 h-100" style="width: 18rem;">
                                    <img class="card-img-top" src="${image}" alt="Card image cap" style="height:250px; width:100%; object-fit:cover;">
                                    <div class="card-body">
                                    </div>
                                </div>
                            `;

                            container.appendChild(card);

                            
                    });
                };
            }



window.onload = loadBlogs()
