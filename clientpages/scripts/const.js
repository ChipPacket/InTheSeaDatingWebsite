const KEY = "3441462ecb5c1866294702d261de3d861d4636786208992d212a702233267367";
const URL = "http://127.0.0.1:5000";

function logout(){
    localStorage.removeItem("userId");
    window.location.href = "login.html";
}