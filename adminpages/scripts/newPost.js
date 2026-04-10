document.getElementById("newPost").addEventListener("submit", async function(e) {
    e.preventDefault();

    const data = {
        adminID: localStorage.getItem("adminId"),
        authors: document.getElementById("author").value,
        title: document.getElementById("title").value,
        content: document.getElementById("content").value,
        image: document.getElementById("photo").value,
        dateOfPublish: new Date().toISOString().split("T")[0]
    };

    try {
        const response = await fetch(`${URL}/api/blogPosts`, {
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
            document.getElementById("newPost").reset();
        }

    } catch (error) {
        console.error(error);
        alert("UH OH.");
    }
});