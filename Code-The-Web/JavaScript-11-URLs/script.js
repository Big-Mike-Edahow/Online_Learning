// script.js

console.log(window.location);

var myURL = new URL('https://example.com:4000/folder/page.html?x=y&a=b#section-2');
console.log(myURL);

console.log("The URL as a string of text:\n");
console.log(myURL.href);

console.log("The protocol of the URL:\n");
console.log(myURL.protocol);

console.log("The hostname of the URL:\n");
console.log(myURL.hostname);

console.log("The port number of the URL:\n");
console.log(myURL.port);

console.log("The host of the URL:\n");
console.log(myURL.host);

console.log("The origin of the URL:\n");
console.log(myURL.origin);

console.log("The pathname of the URL:\n");
console.log(myURL.pathname);

console.log("The element id# of the URL:\n");
console.log(myURL.hash);

console.log("The search query parameters of the URL:\n");
console.log(myURL.search);

/* Getting the query search parameters
   from a URL search parameters object. */
var searchParams = new URLSearchParams(myURL.search);
console.log(searchParams.get('x'));
// Output: "y"
console.log(searchParams.get('a'));
// Output: "b"
