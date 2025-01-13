document.addEventListener('DOMContentLoaded', function () {
    const nav = document.querySelector('.nav');

    window.addEventListener('scroll', function () {
        if (window.scrollY > 50) { 
            nav.classList.add('solid');
        } else {
            nav.classList.remove('solid');
        }
    });
});
