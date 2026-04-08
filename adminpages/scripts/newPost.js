document.getElementById("newPost").addEventListener("submit", async function(e) {
    e.preventDefault();

    const data = {
        adminID: 1, 
        authors: document.getElementById("author").value,
        title: document.getElementById("title").value,
        content: document.getElementById("content").value,
        image: document.getElementById("photo").value,
        dateOfPublish: new Date().toISOString().split("T")[0]
    };

    try {
        const response = await fetch("http://127.0.0.1:5000/api/blogPosts", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "x-api-key": "7b26804109382641a54ff1ded939045d8978542fe8b0f14cbd51b44fc302f4c9" 
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (response.ok) {
            alert("New Post yay");
            document.getElementById("newPost").reset();
        } else {
            alert("Something has broke :(");
        }

    } catch (error) {
        console.error(error);
        alert("UH OH.");
    }
});