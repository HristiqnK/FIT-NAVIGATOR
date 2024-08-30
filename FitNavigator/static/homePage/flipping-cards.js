document.addEventListener('DOMContentLoaded', () => {
    const flippingContainers = document.querySelectorAll('.flipping-container');
    const hoveredContainers = document.querySelectorAll('.general-info-container');
    const contents = document.querySelectorAll('.general-info-container .container-content');
    const headings = []; // Няма заглавия в новия HTML, затова махаме
    
    function turn() {
        const index = Array.from(flippingContainers).indexOf(this);
        hoveredContainers[index].classList.add('hovered');
        contents[index].classList.add('hovered');
    }
    
    function reset() {
        const index = Array.from(flippingContainers).indexOf(this);
        hoveredContainers[index].classList.remove('hovered');
        contents[index].classList.remove('hovered');
    }
    
    flippingContainers.forEach(flippingContainer => {
        flippingContainer.addEventListener('mouseover', turn);
        flippingContainer.addEventListener('mouseout', reset);
    });
})
