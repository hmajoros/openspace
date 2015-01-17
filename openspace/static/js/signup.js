function validateForm() {
	var username = document.forms["signUpForm"]["username"].value;
	var first_name = document.forms["signUpForm"]["firstname"].value;
	var last_name = document.forms["signUpForm"]["lastname"].value;
	var email = document.forms["signUpForm"]["email"].value;
	var password = document.forms["signUpForm"]["password"].value;
	var password_confirm = document.forms["signUpForm"]["password_confirm"].value;

	if (username == null  || username == ""  || first_name == null       || first_name == ""    ||
	    last_name == null || last_name == "" || email == null            || email == ""         ||
	    password == null  || password == ""  || password_confirm == null || password_confirm == "") {

		alert("Please fill in all information");
		return false;
	}

	isEmailValid = validateEmail(email);
	if (!isEmailValid) {
		alert("Please enter a valid email.");
		return false;
	}

	isPasswordSame = validatePasswordsAreEqual(password, password_confirm)
	if(!isPasswordSame) {
		alert("Passwords are not the same, please type them again.");
		return false;
	}
}

function validateEmail(email) { 
    var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
}

function validatePasswordsAreEqual(password, confirm) {
	if (password == confirm) {
		return true;
	} else {
		return false;
	}
	return false;
}