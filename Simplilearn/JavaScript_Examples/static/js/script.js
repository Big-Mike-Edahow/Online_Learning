// script.js

alert("Hello World!");

function fact() {
    var i, num, f;
    f = 1;
    num = document.getElementById("num").value;

    for (i = 1; i <= num; i++) {
        f = f * i;
    }

    i = i - 1;
    document.getElementById("res").innerHTML = "The factorial of the number " + i + " is: " + f;
}

function pressButton() {
    var txt;

    if (confirm("Please press a button!")) {
        txt = "You pressed the OK Button!";
    } else {
        txt = "You pressed the Cancel Button!";
    }
    document.getElementById("test-confirm-box").innerHTML = txt;
}

function greetUser() {
    let text;
    let user = prompt("Please enter your first name:");

    if (user == null || user == "") {
        text = "User cancelled the prompt.";
    } else {
        text = "Hello " + user + "! How are you?";
    }
    document.getElementById("prompt-example").innerHTML = text;

}

document.getElementById("screen-color-depth").innerHTML = "Screen color depth is " + screen.colorDepth;

