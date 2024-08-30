document.addEventListener('DOMContentLoaded', () => {

    const searchBar = document.getElementById('search-bar');
    const exercises = document.querySelectorAll('.excercise');
    const noResultsMessage = document.getElementById('no-results');

    searchBar.addEventListener('keyup', () => {
        const searchTerm = searchBar.value.toLowerCase();
        let hasResults = false;

        exercises.forEach(exercise => {
            const exerciseName = exercise.querySelector('.excercise-name').textContent.toLowerCase();
            if (exerciseName.includes(searchTerm)) {
                exercise.style.display = 'block';
                hasResults = true;
            } else {
                exercise.style.display = 'none';
            }
        });

        if (hasResults) {
            noResultsMessage.style.display = 'none';
        } else {
            noResultsMessage.style.display = 'block';
        }
    });
});