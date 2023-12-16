// script.js

const gallery = document.querySelector('.gallery');
const lightbox = document.querySelector('.lightbox');
const close = document.querySelector('.close');
const lightboxImg = lightbox.querySelector('img');

gallery.addEventListener('click', function (event) {
    event.preventDefault();
    lightbox.style.display = 'flex';
    lightboxImg.src = event.target.src || event.target.parentNode.href;
});

close.addEventListener('click', function () {
    lightbox.style.display = 'none';
});
