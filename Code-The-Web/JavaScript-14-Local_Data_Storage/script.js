// script.js

localStorage.setItem('fullName', 'Jenny Smith');
localStorage.setItem('pageLoadCount', 0);

console.log(localStorage.getItem('fullName'));

var newPageLoadCountValue = Number(localStorage.getItem('pageLoadCount')) + 1;
localStorage.setItem('pageLoadCount', newPageLoadCountValue);

// Removing one item from local storage
localStorage.removeItem('fullName');

// Clearing everything from local storage
localStorage.clear();

// Storing an array to local storage
var user = {
    firstName: 'Jenny',
    lastName: 'Smith',
    username: 'jenny32',
    age: 45
  };
  
  var userString = JSON.stringify(user);
  
  localStorage.setItem('user', userString);

  // Retrieving array data from local storage
  var userStringFromLocalStorage = localStorage.getItem('user');

var userFromLocalStorage = JSON.parse(userStringFromLocalStorage);

console.log(userStringFromLocalStorage);

