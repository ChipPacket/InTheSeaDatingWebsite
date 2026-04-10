const KEY = "ffe4423b530667ef207db2f52df52a241657d1e5f62b84fb6a1af7961e8f1e22";
const URL = "http://127.0.0.1:5000";

function logout(){
    localStorage.removeItem("adminID");
    window.location.href = "adminLogin.html";
}