// script.js

var myDate = new Date();

console.log("Stardate: " + myDate + "\n");
console.log("Timestamp: " + myDate.getTime() + "\n");

myDate.setTime(0);
console.log("Back to the beginning of UNIX:\n");
console.log(myDate);

myDate.setTime(9999999999999);
console.log("To infinity and beyond!\n");
console.log(myDate);

// Get the date and day
var daysOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
var months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
var myDate = new Date();

console.log("Today\'s date: " + daysOfWeek[myDate.getDay()] + " " + months[myDate.getMonth()] + " " + myDate.getDate() + " " + myDate.getFullYear());

console.log("The current time is: " + myDate.getHours() + ":" + myDate.getMinutes() + ":" + myDate.getSeconds());

console.log("Displaying the current date and time by\n");
console.log("using .toDateString() and .toTimeString():\n");
console.log(myDate.toDateString());
console.log(myDate.toTimeString());

