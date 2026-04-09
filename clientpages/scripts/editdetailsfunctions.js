(function (global) {
    // function to make things editable onclick
    document.getElementById("editDetails").addEventListener("click", function() {

        var fieldset1 = document.getElementById("fieldset1");
        var fieldset2 = document.getElementById("fieldset2");
        var editDetailsbtn = document.getElementById("editDetails");

        if (fieldset1.disabled===true){
            fieldset1.disabled = false;
            fieldset2.disabled = false;
            editDetailsbtn.style.backgroundColor = "#FF0000";
            editDetailsbtn.innerHTML = "Cancel Editing";

        }
        else {
            fieldset1.disabled = true;
            fieldset2.disabled = true;
            editDetailsbtn.style.backgroundColor = "#7CD5E0";
            editDetailsbtn.innerHTML = "Edit Details";
        }
    })

    //function to make password viewable onclick
    document.addEventListener('click', function (event) {

	    // If the clicked element isn't our show password checkbox, bail
	    if (event.target.id !== 'show_password') return;

	    // Get the password field
	    var password = document.querySelector('#password');
	    if (!password) return;

	    // Check if the password should be shown or hidden
	    if (event.target.checked) {
		    // Show the password
		    password.type = 'text';
	    } 
        else {
		    // Hide the password
		    password.type = 'password';
	    }
    }, false);

}(window));