document.addEventListener("DOMContentLoaded", () => {
    const faqQuestions = document.querySelectorAll('.faq-question');
    
    faqQuestions.forEach(question => {
        question.addEventListener('click', function() {
            const currentAnswer = this.nextElementSibling;
            const btn = this.querySelector('.btn');
            
            // Close all open elements except the current one
            const openedQuestions = document.querySelectorAll('.faq-question.opened');
            openedQuestions.forEach(openedQuestion => {
                if (openedQuestion !== this) {
                    openedQuestion.classList.remove('opened');
                    const openedAnswer = openedQuestion.nextElementSibling;
                    openedAnswer.classList.remove('opened');
                    const openedBtn = openedQuestion.querySelector('.btn');
                    openedBtn.classList.remove('opened');
                }
            });

            // Toggle current element
            this.classList.toggle('opened');
            currentAnswer.classList.toggle('opened');
            btn.classList.toggle('opened');
        });
    });
});