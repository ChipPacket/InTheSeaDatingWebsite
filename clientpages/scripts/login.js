document.getElementById("login").addEventListener("submit", async function(e) {
    e.preventDefault();

    const data = {
        email: document.getElementById("email").value,
        password: document.getElementById("password").value,
    };

    try {
        const response = await fetch(`${URL}/api/login`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (response.ok) 
            
        {
            alert("Logged In success");

            //saves logged in user - not secure but not sure how else to do this tbh
            localStorage.setItem("userId", result.user.id);

            document.getElementById("login").reset();
            window.location.href = "clienthome.html"
        } 
        else 
        {
            alert("Login Failed");
        }

    } catch (error) {
        console.error(error);
        alert("UH OH.");
    }
});