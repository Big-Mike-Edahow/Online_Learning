// script.js

// Math.random method

let randomNum = Math.random();

while(randomNum > 0.2) {
    alert(randomNum);
    randomNum = Math.random();
}

let counter = 1;

while(counter <= 5) {
    if (counter == 1) {
        alert("Hi " + counter + " time.")
        counter ++;
    }
    else {
    alert("Hi! " + counter + " times.");
    counter += 1;
    }
}

for(let i = 0; i <=5; i++) {
    if (i == 1) {
        alert("I have " + i + " banana.")
    }
    else {
        alert("I have " + i + " bannanas.");
    }
    
}

