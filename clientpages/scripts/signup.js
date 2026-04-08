document.getElementById("newUser").addEventListener("submit", async function(e) {
    e.preventDefault();

    const data = {
        firstName: document.getElementById("firstName").value,
        lastName: document.getElementById("lastName").value,
        birthday: document.getElementById("birthday").value,
        email: document.getElementById("email").value,
        mobileNo: "",
        ownGender: document.getElementById("ownGender").value,
        attractedGender: document.getElementById("attractedGender").value,
        profileContent: "",
        password: document.getElementById("password").value,
        q1: "",
        a1: "",
        q2: "",
        a2: "",
        q3: "",
        a3: "",
        image: ""
    };

    try {
        const response = await fetch(`${URL}/api/users`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "x-api-key": KEY
            },
            body: JSON.stringify(data)
        });

        const text = await response.text();
        console.log(text);

        if (response.ok) {
            alert("New User yay");
            document.getElementById("newUser").reset();
        } else {
            alert("Something has broke :(");
        }

    } catch (error) {
        console.error(error);
        alert("UH OH.");
    }
});