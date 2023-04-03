const headerHamburger = document.querySelector('.header__hamburger');
const navMenu = document.querySelector('.nav__menu');
const itemLink = document.querySelectorAll('.item__link');

headerHamburger.addEventListener('click', () => {
    headerHamburger.classList.toggle('active');
    navMenu.classList.toggle('active');
})

itemLink.forEach(item => {
    item.addEventListener('click', () => {
        headerHamburger.classList.toggle('active');
        navMenu.classList.toggle('active');
    })
})