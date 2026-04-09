
//const userid = localStorage.getItem("userId");
const userid = 2;

const elementAttractedGender = document.getElementById("attractedGender");
const elementFirstName = document.getElementById("firstName");
const elementLastName = document.getElementById("lastName");

const elementCompatability = document.getElementById("Compatibility");


const elementQ1 = document.getElementById("questionOne");
const elementQ2 = document.getElementById("questionTwo");
const elementQ3 = document.getElementById("questionThree");

const elementA1 = document.getElementById("answerOne");
const elementA2 = document.getElementById("answerTwo");
const elementA3 = document.getElementById("answerThree");

const elementContent = document.getElementById("profileContent");
const elementGender = document.getElementById("ownGender");

const elementEmail = document.getElementById("email");
const elementBirthday = document.getElementById("birthday");
const elementImage = document.getElementById("profilePicture");




//fixes format of date becuase the external api hates being normal and using a normal date (copied over) changed slightly
function formatDate(dateString) {
    const date = new Date(dateString);

    const day = String(date.getDate()).padStart(2, '0');
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const year = date.getFullYear();

    return `${year}-${month}-${day}`;
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

                    const user = users.find(u => u.id == userid);

                    if (!user) {
                        console.error("User not found");
                        return;
                    }

                    elementGender.value = user.ownGender;
                    elementAttractedGender.value = user.attractedGender;

                    elementFirstName.value = user.firstName;
                    elementLastName.value = user.lastName;

                    elementImage.value = user.image;

                    elementQ1.value = user.q1;
                    elementQ2.value = user.q2;
                    elementQ3.value = user.q3;

                    elementA1.value = user.a1;
                    elementA2.value = user.a2;
                    elementA3.value = user.a3;

                    elementEmail.value = user.email;
                    elementBirthday.value = formatDate(user.birthday);



                    elementContent.innerHTML = user.profileContent;

                };
            }

    catch(error)
    {
        console.error(error);
    }        
}

window.onload = loadUsers;