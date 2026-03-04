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

    // --- КНОПКА НАВЕРХ (BACK TO TOP) ---
    const backToTopBtn = document.getElementById("backToTopBtn");

    if (backToTopBtn) {
        // Появление после 800px скролла (примерно Hero + Services)
        window.addEventListener("scroll", () => {
            if (window.scrollY > 800) {
                backToTopBtn.classList.add("show");
            } else {
                backToTopBtn.classList.remove("show");
            }
        });

        // Плавный скролл наверх
        backToTopBtn.addEventListener("click", (e) => {
            e.preventDefault(); // Отключаем стандартное поведение
            window.scrollTo({
                top: 0,
                left: 0,
                behavior: "smooth"
            });
        });
    }

});