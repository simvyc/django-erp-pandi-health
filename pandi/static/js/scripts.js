document.addEventListener('DOMContentLoaded', function () {
    const nav = document.querySelector('.nav');

    window.addEventListener('scroll', function () {
        if (window.scrollY > 50) { // Adjust threshold as needed
            nav.classList.add('solid');
        } else {
            nav.classList.remove('solid');
        }
    });
});
