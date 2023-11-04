function showContent(showId, hideId) {
    // Hide the div with hideId
    const hideDiv = document.getElementById(hideId);
    if (hideDiv) {
        hideDiv.style.display = 'none';
    }

    // Show the div with showId
    const showDiv = document.getElementById(showId);
    if (showDiv) {
        showDiv.style.display = 'block';
    }

    event.preventDefault();
}

function validatePassword() {
    var setPassword = document.getElementById('password').value;
    var confirmPassword = document.getElementById('confirmPassword').value;
    var name = document.getElementById('name').value;
    var mobilenumber = document.getElementById('mobilenumber').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    var dob = document.getElementById('dob').value;
    var referral = document.getElementById('referral').value;
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    function rc(){
        let randomCode = '';
        for (let i = 0; i < length; i++) {
            const randomIndex = Math.floor(Math.random() * characters.length);
            randomCode += characters[randomIndex];
        return randomCode;
    }
    randomCode = rc();
    }
    while(randomCode in eel.uniquerefergen()){
        randomCode = rc();
    }
    if (setPassword !== confirmPassword) {
        alert("Passwords do not match. Please make sure both passwords are the same.");
        return false; // Prevent form submission
    }

    return true; // Allow form submission


}

