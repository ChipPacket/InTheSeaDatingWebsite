
function checkUserLogIn(){
    //check if user is logged in thus userID exists
    const imageid = localStorage.getItem("userId");
    // if (localStorage.getItem("userId")!==null){
        // enable links
    if (imageid){
        document.getElementById("findMyCatch").href = "findyourcatch.html";

        // change sign up
        document.getElementById("myProfile").href = "editdetails.html";

        // change log in -> myprofile
        document.getElementById("opt1").innerHTML = "My Profile";
        document.getElementById("opt1").href = "editdetails.html";

        // change sign up -> log out
        document.getElementById("opt2").innerHTML = "Log Out";
        document.getElementById("opt2").onclick = "logout()";
    }
}

checkUserLogIn();