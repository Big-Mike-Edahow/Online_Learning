// script.js

// Timeouts
function myTimeoutFunction() {
    console.log('3 seconds have passed!');
}

var myTimeout = setTimeout(myTimeoutFunction, 3000);
// clearTimeout(myTimeout);

// Intervals
function myIntervalFunction() {
    console.log('I will log every 5 seconds!');
}

var myInterval = setInterval(myIntervalFunction, 5000);
// clearInterval(myInterval);

// Log the time every second
function myIntervalFunction() {
    console.log(new Date().toLocaleTimeString());
}

var myInterval = setInterval(myIntervalFunction, 1000);

