// date and time
n = new Date();
y = n.getFullYear();
m = n.getMonth() + 1;
d = n.getDate();
document.getElementById("date").innerHTML = d + "/" + m + "/" + y

/* this is the page selector or u can say the sidebar buttons */
function showContent(contentId) {
    // Hide all content divs
    const contentDivs = document.querySelectorAll('.content-of-page div');
    for (const div of contentDivs) {
        div.style.display = 'none';
    }

    // Show the selected content div
    const selectedContent = document.getElementById(contentId);
    if (selectedContent) {
        selectedContent.style.display = 'flex';
    }
}

/* for the community page */
function investi(){ window.location.href="https://www.investmentnews.com"; }
function yahoo(){ window.location.href="https://finance.yahoo.com/"; }
function tradev(){ window.location.href="https://www.tradingview.com/"; }
function money(){ window.location.href="https://MoneyControl.com"; }
function conomic(){ window.location.href="https://tradingeconomics.com/"; }
function nse(){ window.location.href="https://www.nseindia.com/"; }

/* data analysis */

// Function to read and parse the CSV file
function readCSVa() {
    fetch('ADANIPORTS.csv') // Replace 'ADANIPORTS.csv' with the actual URL or file path
        .then(response => response.text())
        .then(parseCSVa)
        .catch(error => console.error('Error loading CSV data:', error));
}

// Function to parse the CSV data
function parseCSVa(csv) {
    var lines = csv.split('\n');
    var tableBody = document.querySelector('#csvTable tbody');
    
    var labels = [];
    var data = [];
    
    for (var i = 1; i <= 10000 && i < lines.length; i++) {
        var parts = lines[i].split(',');
        if (parts.length >= 2) {
            var date = parts[0];
            var close = parseFloat(parts[8]); // Assuming 'Close' is in the 9th column (index 8)
            
            var row = tableBody.insertRow();
            var dateCell = row.insertCell(0);
            var closeCell = row.insertCell(1);
            
            dateCell.innerHTML = date;
            closeCell.innerHTML = close;
            
            labels.push(date);
            data.push(close);
        }
    }

    createLineCharta(labels, data);
}

function createLineCharta(labels, data) {
    var ctx = document.getElementById('lineChart').getContext('2d');
    
    var chart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Close Value',
                data: data,
                backgroundColor: 'rgba(0, 119, 204, 0.2)',
                borderColor: 'rgba(0, 119, 204, 1)',
                borderWidth: 1,
                pointRadius: 3
            }]
        },
        options: {
            scales: {
                x: [{
                    type: 'time',
                    time: {
                        unit: 'day',
                        displayFormats: {
                            day: 'MMM DD'
                        }
                    }
                }],
                y: [{
                    scaleLabel: {
                        display: true,
                        labelString: 'Close Value'
                    }
                }]
            }
        }
    });
}

readCSVa();

/* second graph */

// Function to read and parse the CSV file
function readCSV() {
    fetch('AMZN.csv') // Replace 'AMZN.csv' with the actual URL or file path
        .then(response => response.text())
        .then(parseCSV)
        .catch(error => console.error('Error loading CSV data:', error));
}

// Function to parse the CSV data
function parseCSV(csv) {
    var lines = csv.split('\n');
    var tableBody = document.querySelector('#csvTable tbody');

    var labels = [];
    var data = [];

    for (var i = 1; i < lines.length; i++) {
        var parts = lines[i].split(',');
        if (parts.length === 7) {
            var date = parts[0];
            var close = parseFloat(parts[5]); // Close price in the 6th column (index 5)

            var row = tableBody.insertRow();
            var dateCell = row.insertCell(0);
            var closeCell = row.insertCell(1);

            dateCell.innerHTML = date;
            closeCell.innerHTML = close;

            labels.push(date);
            data.push(close);
        }
    }

    createLineChart(labels, data);
}

function createLineChart(labels, data) {
    var ctx = document.getElementById('lineCharta').getContext('2d');

    var chart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Close Price',
                data: data,
                borderColor: 'rgba(0, 119, 204, 1)',
                borderWidth: 1,
                pointRadius: 0, // Change to adjust the point size
            }]
        },
        options: {
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Date',
                    },
                },
                y: {
                    title: {
                        display: true,
                        text: 'Close Price',
                    },
                },
            },
        },
    });
}

readCSV();


/* explore companies */

var xlsxFileLocation = 'book.xlsx';
        function readAndDisplayXLSXData() {
            var xhr = new XMLHttpRequest();
            xhr.open('GET', xlsxFileLocation, true);
            xhr.responseType = 'arraybuffer';

            xhr.onload = function (e) {
                var arrayBuffer = xhr.response;
                var data = new Uint8Array(arrayBuffer);
                var workbook = XLSX.read(data, { type: 'array' });
                var sheetName = workbook.SheetNames[0]; // Assuming you have only one sheet
                var sheet = workbook.Sheets[sheetName];
                var jsonData = XLSX.utils.sheet_to_json(sheet);

                var table = document.getElementById('dataTable');
                var tbody = table.getElementsByTagName('tbody')[0];

                jsonData.forEach(function (row) {
                    var newRow = tbody.insertRow(tbody.rows.length);
                    Object.keys(row).forEach(function (key, index) {
                    var cell = newRow.insertCell(index);
                    cell.innerHTML = row[key];
                    });
                });
            };

            xhr.send();
        }

        readAndDisplayXLSXData();

// refer and earn

function redirectToWhatsApp() {
    var phonenumber = document.getElementById("mn").value;
    var whatsappUrl = 'https://wa.me/' + 91+ phonenumber + '?text=Hello, this is the pre-filled message!';
    window.location.href = whatsappUrl;
}


// compro

// Function to read and parse the CSV file
function readCSVb() {
    fetch('cp.csv') // Replace 'ADANIPORTS.csv' with the actual URL or file path
        .then(response => response.text())
        .then(parseCSVb)
        .catch(error => console.error('Error loading CSV data:', error));
}

// Function to parse the CSV data
function parseCSVb(csv) {
    var lines = csv.split('\n');
    var tableBody = document.querySelector('#compro tbody');
    
    var labels = [];
    var data = [];
    
    for (var i = 1; i <= 10 && i < lines.length; i++) {
        var parts = lines[i].split(',');
        if (parts.length >= 2) {
            var date = parts[0];
            var close = parts[1]; 
            
            var row = tableBody.insertRow();
            var dateCell = row.insertCell(0);
            var closeCell = row.insertCell(1);
            
            dateCell.innerHTML = date;
            closeCell.innerHTML = close;
            
            labels.push(date);
            data.push(close);
        }
    }

    createLineCharta(labels, data);
}

readCSVb();




