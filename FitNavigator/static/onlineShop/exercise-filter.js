document.addEventListener('DOMContentLoaded', () => {
    console.log("works");

    const filter = document.querySelector('.filter-window');
    const closeBtn = document.querySelector('.filter-close-btn .bx-x'); 
    const openBtn = document.querySelector('.filter-btn'); 
    const keywords = document.querySelectorAll('.keyword');
    const background = document.querySelector('.filter-background');
    const exercises = document.querySelectorAll('.exercise'); // Corrected the spelling here
    const noResults = document.getElementById('no-results');

    if (openBtn) {
        openBtn.addEventListener('click', () => {
            filter.classList.add('opened');
            background.classList.add('opened');
        });
    }

    if (closeBtn) {
        closeBtn.addEventListener('click', () => {
            filter.classList.remove('opened');
            background.classList.remove('opened');
        });
    }

    if (background) {
        background.addEventListener('click', () => {
            filter.classList.remove('opened');
            background.classList.remove('opened');
        });
    }

    keywords.forEach(keyword => keyword.addEventListener('click', () => {
        keyword.classList.toggle('selected');
        filterExercises();
    }));

    function filterExercises() {
        const selectedKeywordsWithData = Array.from(keywords)
            .filter(keyword => keyword.classList.contains('selected'))
            .map(keyword => keyword.getAttribute('data-exercise'));

        // Show all exercises if no filters are selected
        if (selectedKeywordsWithData.length === 0) {
            exercises.forEach(exercise => {
                exercise.style.display = 'block';
            });
            noResults.style.display = 'none';
            return;
        }

        // Filter exercises based on selected keywords
        exercises.forEach(exercise => {
            const exerciseKeyword = exercise.getAttribute('data-exercise');
            if (selectedKeywordsWithData.includes(exerciseKeyword)) {
                exercise.style.display = 'block';
            } else {
                exercise.style.display = 'none';
            }
        });

        // Check if any exercises are visible
        const anyVisible = Array.from(exercises).some(exercise => exercise.style.display === 'block');
        noResults.style.display = anyVisible ? 'none' : 'block';
    }
});
