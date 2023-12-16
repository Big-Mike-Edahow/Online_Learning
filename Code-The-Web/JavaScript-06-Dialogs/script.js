// script.js

alert("JavaScript is fun!");

let result = confirm("Press one of the buttons...");

if(result == true) {
    alert("You clicked OK!");
} else {
    alert("You clicked Cancel!");
}

let text = prompt("Type some text:");

if(text == null) {
    alert("You hit Cancel!");
}
else if (text == '') {
    alert("You didn't type anything!");
}
else {
    alert("You typed:\n" + text);
}
