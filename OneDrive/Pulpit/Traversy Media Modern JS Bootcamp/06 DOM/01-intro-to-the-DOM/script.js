// =============== 01 DOM Intro =============== //

console.log(window);
console.dir(window.document);
console.log(document.body.innerText);
console.log(document.links[0]);
document.body.innerHTML += '<h2>Hello World</h2>';

console.log(document.getElementById('main'));
const main = document.getElementById('main');
main.innerHTML = '<h1>Hello from main</h2>';
document.querySelector('#main h1').innerText = 'Hello';
