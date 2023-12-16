// script.js

console.log(document.querySelector('#myId'));

document.querySelector('h1').innerHTML = 'Hello World!';

document.querySelector('#myId').innerHTML = 'This is <strong>bold</strong>.';

document.querySelector('body').innerHTML += '<h2>I am now on the page!</h2>';

console.log(document.querySelector('#classesExample').classList);

console.log(document.querySelector('#classesExample').classList.contains('title'));

document.querySelector('#classesExample').classList.add('another-class');

console.log(document.querySelector('#classesExample').classList);

document.querySelector('#classesExample').classList.remove('title');

console.log(document.querySelector('#classesExample').classList);

document.querySelector('#classesExample').classList.toggle('second-h1');

console.log(document.querySelector('#classesExample').classList);

console.log(document.querySelector('img').getAttribute('src'));

alert("The image on the page will be changed!");

document.querySelector('img').setAttribute('src', './images/Vaquero.jpg');

alert("The color of the H1 heading will change!");

document.querySelector('h1').style.color = 'red';

alert("The background color will now be changed!");

document.querySelector('body').style.backgroundColor = 'orange';

console.log(document.querySelectorAll('h1'));

var elements = document.querySelectorAll('h1');

for(var i = 0; i < elements.length; i++) {
    elements[i].style.color = 'green';
}