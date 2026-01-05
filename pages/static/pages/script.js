document.addEventListener('DOMContentLoaded', () => {
    
    // --- 1. МОБИЛЬНОЕ МЕНЮ (ГАМБУРГЕР) ---
    const hamburger = document.querySelector('.hamburger');
    const nav = document.querySelector('.main-nav');

    if (hamburger && nav) {
        hamburger.addEventListener('click', () => {
            hamburger.classList.toggle('active');
            nav.classList.toggle('active');
        });

        // Закрывать меню при клике на ссылку
        nav.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                hamburger.classList.remove('active');
                nav.classList.remove('active');
            });
        });
    }

    // --- 2. АНИМАЦИЯ ПРИ СКРОЛЛЕ ---
    function reveal() {
        var reveals = document.querySelectorAll(".reveal");

        for (var i = 0; i < reveals.length; i++) {
            var windowHeight = window.innerHeight;
            var elementTop = reveals[i].getBoundingClientRect().top;
            var elementVisible = 150; // Начинаем анимацию, когда элемент показался на 150px

            if (elementTop < windowHeight - elementVisible) {
                reveals[i].classList.add("active");
            }
        }
    }

    // Слушаем скролл
    window.addEventListener("scroll", reveal);
    
    // Запускаем один раз сразу, чтобы показать верхние элементы
    reveal();
    const cookieBanner = document.getElementById('cookie-banner');
    const acceptBtn = document.getElementById('accept-cookies');

    // Проверяем, есть ли запись в памяти браузера
    if (!localStorage.getItem('cookiesAccepted')) {
        // Если нет, показываем баннер через 2 секунды (чтобы не пугать сразу)
        setTimeout(() => {
            cookieBanner.classList.add('show');
        }, 2000);
    }

    // Когда нажали кнопку "Accetto"
    if (acceptBtn) {
        acceptBtn.addEventListener('click', () => {
            // Убираем баннер
            cookieBanner.classList.remove('show');
            // Записываем в память: "Этот человек согласился!"
            localStorage.setItem('cookiesAccepted', 'true');
        });
    }
});