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
    const revealElements = document.querySelectorAll(".reveal");

    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("active");
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.15
    });

    revealElements.forEach(el => revealObserver.observe(el));
    // --- 3. COOKIE BANNER ---
    const cookieBanner = document.getElementById('cookie-banner');
    const acceptBtn = document.getElementById('accept-cookies');

    if (!localStorage.getItem('cookiesAccepted') && cookieBanner) {
        setTimeout(() => {
            cookieBanner.classList.add('show');
        }, 2000);
    }

    if (acceptBtn) {
        acceptBtn.addEventListener('click', () => {
            cookieBanner.classList.remove('show');
            localStorage.setItem('cookiesAccepted', 'true');
        });
    }

    // --- 4. АВТО-ЗАКРЫТИЕ СООБЩЕНИЙ ---
    const alerts = document.querySelectorAll('.alert');

    if (alerts.length > 0) {
        alerts.forEach(alert => {
            setTimeout(() => {
                alert.style.transition = "opacity 0.5s ease";
                alert.style.opacity = "0";
                setTimeout(() => {
                    alert.remove();
                }, 500);
            }, 5000);
        });
    }

    // --- 5. СЛАЙДЕР БРЕНДОВ (SWIPER) ---
    // Проверяем, есть ли слайдер на странице, чтобы избежать ошибок
    if (document.querySelector(".myBrandSwiper")) {
        const swiper = new Swiper(".myBrandSwiper", {
            slidesPerView: 1,     // На мобильном
            spaceBetween: 20,
            loop: true,           // Бесконечная прокрутка

            navigation: {
                nextEl: ".swiper-button-next",
                prevEl: ".swiper-button-prev",
            },
            pagination: {
                el: ".swiper-pagination",
                clickable: true,
            },
            breakpoints: {
                640: {
                    slidesPerView: 1, // Планшет
                    spaceBetween: 20,
                },
                1024: {
                    slidesPerView: 5, // ПК
                    spaceBetween: 40,
                },
            },
        });
    }

});