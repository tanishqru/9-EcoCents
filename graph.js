// Get a reference to the canvas element and its 2d context.
var canvas = document.getElementById('chart');
var ctx = canvas.getContext('2d');

// Define variables to keep track of data and time.
var data = [];
var time = 0;
var maxDataPoints = 50; // Maximum number of data points to display.

// Function to add a new data point every second.
function addDataPoint() {
    data.push(Math.random() * canvas.height); // You can replace this with your data source.
    time++;

    // Limit the number of data points to the specified maximum.
    if (data.length > maxDataPoints) {
        data.shift(); // Remove the oldest data point.
    }

    // Clear the canvas and redraw the line chart.
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawLineChart();

    // Call the function again in one second.
    setTimeout(addDataPoint, 1000);
}

// Function to draw the line chart.
function drawLineChart() {
    var stepX = canvas.width / data.length;
    ctx.beginPath();
    ctx.moveTo(0, canvas.height - data[0]);
    for (var i = 1; i < data.length; i++) {
        ctx.lineTo(i * stepX, canvas.height - data[i]);
    }
    ctx.strokeStyle = 'blue';
    ctx.lineWidth = 2;
    ctx.stroke();
}

// Start the data generation and chart drawing.
addDataPoint();