
//store user id and go to view their page
function goToProfile(id) {
    localStorage.setItem("selectedUserId", id);
    window.location.href = "profile.html";
}

function getAge(dateOfBirth) {

    //current date in years minus birthday in years need to check month later
    const today = new Date();
    const dob = new Date(dateOfBirth);

    let age = today.getFullYear() - dob.getFullYear();

    return age;
}

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
                                    <h5 class="card-title text-start">${user.firstName} ${user.lastName}</h5>
                                    <p class="card-text text-start">Age: ${getAge(user.birthday)}</p>
                                    <button class="btn btn-primary text-end" onclick="goToProfile('${user.id}')">Reel In?</button>
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

window.onload = loadUsers;