// Awill auto update at the end
const userid = 1;

// well behaved elements
const elementAttractedGender = document.getElementById("attractedGender");
const elementFirstName = document.getElementById("firstName");
const elementLastName = document.getElementById("lastName");
const elementContent = document.getElementById("profileContent");
const elementGender = document.getElementById("ownGender");
const elementEmail = document.getElementById("email");

//q and a
const elementQ1 = document.getElementById("questionOne");
const elementQ2 = document.getElementById("questionTwo");
const elementQ3 = document.getElementById("questionThree");

const elementA1 = document.getElementById("answerOne");
const elementA2 = document.getElementById("answerTwo");
const elementA3 = document.getElementById("answerThree");

//annoying things
const elementBirthday = document.getElementById("birthday");
const elementImage = document.getElementById("profilePicture");
const elementPassword = document.getElementById("password");

// same as the function form the external api mildly changed to format dif
function formatDate(dateString) {
    const date = new Date(dateString);

    const day = String(date.getDate()).padStart(2, '0');
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const year = date.getFullYear();

    return `${year}-${month}-${day}`;
}


// Load user details on page load
async function loadUsers() {
    try {
        const response = await fetch(`${URL}/api/users`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                "x-api-key": KEY
            }
        });

        if (response.ok) {
            const users = await response.json();
            const user = users.find(u => u.id == userid);
            if (!user) {
                console.error("User not found");
                return;
            }

            // Fill form with user data
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
            elementContent.value = user.profileContent;
            //elementPassword.value = user.password;
        }
    } catch (error) {
        console.error(error);
    }
}

// Update user on submit
document.getElementById("userDetailsForm").addEventListener("submit", async function(e) {
    e.preventDefault();

    const data = {
        id: userid,
        firstName: elementFirstName.value,
        lastName: elementLastName.value,
        birthday: elementBirthday.value,
        email: elementEmail.value,
        mobileNo: "", // not used anymore to ambitious :(
        ownGender: elementGender.value,
        attractedGender: elementAttractedGender.value,
        profileContent: elementContent.value,
        //  password: elementPassword.value, //dont wanna get or send later cuz security
        q1: elementQ1.value,
        a1: elementA1.value,
        q2: elementQ2.value,
        a2: elementA2.value,
        q3: elementQ3.value,
        a3: elementA3.value,
        image: elementImage.value,
        activeUser: true
    };

    try {
        const response = await fetch(`${URL}/api/users`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
                "x-api-key": KEY
            },
            body: JSON.stringify(data)
        });

        if (response.ok) {
            alert("User updated successfully!");
        } else {
            const errorText = await response.text();
            console.error(errorText);
            alert("Something went wrong :(");
        }
    } catch (error) {
        console.error(error);
        alert("Network error!");
    }
});

window.onload = loadUsers;