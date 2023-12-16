// scripts.js

// Variable declarations

let triple_num = 10;
let userName;

// Function declarations

function myFirstFunction() {
    let x = 5;
    alert("x = 5\nx * 2 = " + x * 2);
}

function alertDouble(num) {
    alert("num = " + num + "\nnum * 2 = " + num * 2);
}

function alertMultiplied(num1, num2) {
    alert("num1 = " + num1 + "\nnum2 = " + num2 + "\nnum1 * num2 = " + num1 * num2);
}

function triple(num) {
    return(num * 3);
}

function introduce() {
    return("Hello, I\'m Big Mike.");
}

myFirstFunction();

alertDouble(2);

alertMultiplied(8, 21);

alert("Number to be trippled is: " + triple_num + "\n" + triple_num + " trippled is: " + triple(triple_num));

alert(introduce());

userName = prompt("What is your name?");
alert("Nice to meet you, " + userName + ".");

