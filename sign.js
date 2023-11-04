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

    if (setPassword !== confirmPassword) {
        alert("Passwords do not match. Please make sure both passwords are the same.");
        return false; // Prevent form submission
    }

    return true; // Allow form submission
}

