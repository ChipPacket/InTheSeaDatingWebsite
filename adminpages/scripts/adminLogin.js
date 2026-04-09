const KEY = "3441462ecb5c1866294702d261de3d861d4636786208992d212a702233267367";
const URL = "http://127.0.0.1:5000";

document.getElementById("login").addEventListener("submit", async function(e) {
    e.preventDefault();

    const data = {
        adminId: document.getElementById("adminId").value,
        password: document.getElementById("password").value,
    };

    try {
        const response = await fetch(`${URL}/api/admin/login`, {
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
            localStorage.setItem("adminId", result.admin.id);

            document.getElementById("login").reset();
            window.location.href = "adminhome.html"
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