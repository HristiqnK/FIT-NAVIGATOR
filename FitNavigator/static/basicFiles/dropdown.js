document.addEventListener('DOMContentLoaded', () => {  
const toggleBtn = document.querySelector('.burger-menu');
const toggleBtnContent = document.querySelector('.bx-menu');
const dropdownMenu = document.querySelector('.mobile-content');

toggleBtn.addEventListener('click', () => {
    dropdownMenu.classList.toggle('opened');
    toggleBtnContent.className = toggleBtnContent.classList.contains('bx-menu') ? 'bx bx-x' : 'bx bx-menu';
}); } );