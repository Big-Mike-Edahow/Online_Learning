// script.js

var myFriend = {
    firstName: 'John',
    lastName: 'Smith',
    age: 27,
    nationality: 'British',
    sayHi: function() {
        alert('Hi!');
    },
    introduce: function() {
        alert('My name is ' + this.firstName + ' ' + this.lastName + ". I'm " + this.nationality + " and I'm " + this.age + ' years old.');
    }
};

// Call the sayHi() and Introduce() functions of the myFriend object
myFriend.sayHi();
myFriend.introduce();

// Log the keys and values of the myFriend object
console.log(Object.keys(myFriend));
console.log(Object.values(myFriend));

var myObject = {favoriteFood: 'Pizza', hobby: 'Coding'};
console.log(JSON.stringify(myObject));

var myString = '{"favoriteFood":"Pizza","hobby":"Coding"}';
console.log(JSON.parse(myString));

