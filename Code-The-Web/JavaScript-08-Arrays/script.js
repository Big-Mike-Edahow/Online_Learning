// script.js

// Array declartions

let myString = "Pineapples, Bananas, Carrots, and Mangoes are awesome.";
let myStringOne = "Code+The+Web+Is+Awesome";
let myStringTwo = "I^$^Like^$^Money^$^!";
let myStringThree = "Hello how are you today?";

let myArray = [4, 5, 3, 7, 'Hello', 2, 1, true, false, 0];
let myArrayOne = ["Dashes", "are", "awesome", "!"];
let myArrayTwo = ["Dashes", "are", "awesome", "!"];
let myArrayThree = [4,5,6,7,8];
let myArrayFour = [4, 5, 3, 7, 'Hello', 2, 1, true, false, 0];
let myArrayFive = ['a', 'b', 'a', 'a', 'b', 'a' ,'b', 'b', 'a'];


console.log(myString.split(",") );
console.log(myStringOne.split("+") );
console.log(myStringTwo.split("^$^") );
console.log(myStringThree.split("") );

alert(myArray[1]);
alert(myArray[4]);
alert(myArray[8]);

console.log(myArrayOne.join("-"));
console.log(myArrayTwo.join("-").split("-") );

console.log(myArrayThree.reverse());

// Find the index of the first instance of the given value
console.log(myArrayFour.indexOf(7));
console.log(myArrayFive.indexOf('a'));

// Find the index of the last instance of the given value
console.log(myArrayFour.lastIndexOf('0'));
console.log(myArrayFive.lastIndexOf('a'));

// Find if the array includes the given value
console.log(myArrayFour.includes(3));
console.log(myArrayFour.includes(9));
console.log(myArrayFour.includes('Hello'));

// Find the first item in an array that passes a certain test
let wordArray = 'stronger'.split('');

function isVowel(letter) {
    let lowerCase = letter.toLowerCase();
    return(lowerCase == 'a' || lowerCase == 'e' || lowerCase == 'i' || lowerCase == 'o' || lowerCase == 'u');
}

console.log( wordArray.find(isVowel) );

// .map()
var myArraySix = [3, 6, 2, 5, 1, -5];

function addTwo(num) {
    return(num + 2);
}

console.log( myArraySix.map(addTwo) );

// .filter()
var myArraySeven = [3, 14, -21, 0, 662];

function isBelowFive(num) {
    return(num < 5);
}

console.log( myArraySeven.filter(isBelowFive) );

// .reduce()
var myArrayEight = [2, 3, 5, 110];

function addTogether(total, num) {
    return(total + num);
}

console.log( myArrayEight.reduce(addTogether) );

// .sort()
var languages = ['HTML', 'CSS', 'JavaScript'];
console.log( languages.sort() );

var numbers = [1, 2, 3, 12, 22, 32, 199, 299, 399];
console.log( numbers.sort() );

// .splice()
var myArrayNine = [1, 2, 3, 4, 5];
myArrayNine.splice(2, 1, 8, 9)
console.log(myArrayNine);

var nestedArray = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ];

alert("Open the console to see the output.");

