


const userid = localStorage.getItem("selectedUserId");
const logid = localStorage.getItem("userId");




const elementGender = document.getElementById("gender");
const elementAttractedGender = document.getElementById("attractedGender");
const elementName = document.getElementById("name");


const elementCompatability = document.getElementById("Compatibility");


const elementQ1 = document.getElementById("q1");
const elementQ2 = document.getElementById("q2");
const elementQ3 = document.getElementById("q3");

const elementA1 = document.getElementById("a1");
const elementA2 = document.getElementById("a2");
const elementA3 = document.getElementById("a3");


const elementBirthday = document.getElementById("birthday");
const elementAge = document.getElementById("age");
const elementImage = document.getElementById("pfpImage");

const elementContent = document.getElementById("content");

function getAge(dateOfBirth) {

    //current date in years minus birthday in years need to check month later
    const today = new Date();
    const dob = new Date(dateOfBirth);

    let age = today.getFullYear() - dob.getFullYear();

    return age;
}

//fixes format of date becuase the external api hates being normal and using a normal date 
function formatDate(dateString) {
    const date = new Date(dateString);

    const day = String(date.getDate()).padStart(2, '0');
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const year = date.getFullYear();

    return `${month}/${day}/${year}`;
}

async function checkMatch(users) {
    const user = users.find(u => u.id == userid);
    const user2 = users.find(u => u.id == logid);

    if (!user || !user2) {
        console.error("User not found");
        return;
    }

    const name1 = user.firstName;
    const name2 = user2.firstName;

    const dob1 = formatDate(user.birthday);
    const dob2 = formatDate(user2.birthday);

    const params = encodeURIComponent(
        `name=${name1}&dob=${dob1}&name1=${name2}&dob1=${dob2}&sort=L&NC=C&ryr=2026&details=N`
    );

    const url = `https://starlovematch.p.rapidapi.com/api/?birthdetails=${params}`;

    const response = await fetch(url, {
        method: "GET",
        headers: {
            "x-rapidapi-key": "ff9205a93bmsh388aaac8adccb5bp128ac4jsn2cd2d4f5ee6b", //is just a public key so doesnt need to be hidden
            "x-rapidapi-host": "starlovematch.p.rapidapi.com"
        }
    });

    const result = await response.json();
    console.log(result);

    if (result.length > 0) {
            const love = result[0].love;
            elementCompatability.innerHTML = `${love}%`;
        } else {
            elementCompatability.innerHTML = "No match found";
        }
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
                    elementGender.innerHTML = user.ownGender;
             
                    elementName.innerHTML = `${user.firstName} ${user.lastName}`;
                    elementImage.src = user.image;
                    elementAttractedGender.innerHTML = user.attractedGender;

                    elementQ1.innerHTML = user.q1;
                    elementQ2.innerHTML = user.q2;
                    elementQ3.innerHTML = user.q3;

                    elementA1.innerHTML = user.a1;
                    elementA2.innerHTML = user.a2;
                    elementA3.innerHTML = user.a3;

                    elementAge.innerHTML = getAge(user.birthday);
                    
                    var dateString = `${user.birthday}`;
                    dateString = new Date(dateString).toUTCString();
                    dateString = dateString.split(' ').slice(0, 4).join(' ');

                    elementBirthday.innerHTML = dateString;
                    elementContent.innerHTML = user.profileContent;

                    checkMatch(users);


                };
            }

    catch(error)
    {
        console.error(error);
    }        
}

window.onload = loadUsers;