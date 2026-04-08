
async function loadUsers() {
    
    try {
            const response = await fetch(`${URL}/api/users`, {
                method: "GET",
                headers: {
                    "Content-Type": "application/json",
                    "x-api-key": KEY 
                }
            });

        

            if (response.ok) 
                {
                    const users = await response.json();
                    const container = document.getElementById("usersprofiles");


                        users.forEach(user => {
                            
                            const card = document.createElement("div");

                            card.className = "col-md-4 mb-4";
                            
                            //card for each user
                            // button will redirect to user page as well as storing the users id again
                            card.innerHTML = `
                                <div class="card w-100">
                                    <div class="card-body">
                                        <h5 class="card-title">User ID:${user.id}</h5>
                                        <p class="card-text">Name: ${user.firstName} ${user.lastName}</p>
                                        <a href="#" class="btn btn-primary" onclick="deleteAccount('${user.id}')">Delete Account</a>
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

async function deleteAccount(userid) {
    
    const data = {
        id: userid
    }
    

    try {
            const response = await fetch(`${URL}/api/users`, {
                method: "DELETE",
                headers: {
                    "Content-Type": "application/json",
                    "x-api-key": KEY
                },
                body: JSON.stringify(data)
            });

        

            if (response.ok) 
                {
                    window.location.href = "adminUserlist.html"
                };
            }

    catch(error)
    {
        console.error(error);
        alert("error");
    }        
}

window.onload = loadUsers;