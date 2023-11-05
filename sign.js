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


function showContent() {
    
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
    var formData = {
      name: document.getElementById('name').value,
      email: document.getElementById('email').value,
      password: document.getElementById('password').value,
      mobilenumber: document.getElementById('mobilenumber').value,
      dob: document.getElementById('dob').value,
      referal: document.getElementById('referal').value,
      randomCode: randomCode
    };
    // Get existing data from the Excel sheet (if any)
    var workbook = XLSX.utils.book_new();
    var sheet = XLSX.utils.json_to_sheet([formData]);
  
    // Append new data to the existing sheet
    if (workbook.Sheets['Sheet1']) {
      XLSX.utils.sheet_add_json(workbook.Sheets['Sheet1'], [formData], {origin: -1});
    } else {
      workbook.Sheets['Sheet1'] = sheet;
    }
  
    // Convert the workbook to a blob
    var blob = XLSX.write(workbook, { bookType: 'xlsx', type: 'blob' });
  
    // Save the Excel file
    saveAs(blob, 'user.xlsx');
  }