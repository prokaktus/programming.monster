import './css/main.css';
import './css/codehilite.css';

function init() {
    const burger = <HTMLElement>document.querySelector('.burger')!;
    const menu = document.querySelector('#' + burger.dataset.target)!;
    burger.addEventListener('click', function() {
        burger.classList.toggle('is-active');
        menu.classList.toggle('is-active');
    });
}

window.addEventListener('DOMContentLoaded', init);
