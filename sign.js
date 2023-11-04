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
}
