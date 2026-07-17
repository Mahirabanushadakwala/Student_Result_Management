// =========================================================
// Student Result Management System — front-end interactions
// =========================================================

document.addEventListener('DOMContentLoaded', () => {

    // Confirms JS actually loaded + ran — CSS only hides .reveal
    // sections for the fade-in animation once this class is present.
    // If this line never runs (script.js 404s, is blocked, or errors
    // earlier in this file), sections stay visible via the CSS default.
    document.documentElement.classList.add('js-ready');

    const navbar    = document.getElementById('navbar');
    const navToggle = document.getElementById('navToggle');
    const navLinks   = document.getElementById('navLinks');
    const scrollTopBtn = document.getElementById('scrollTop');
    const links = document.querySelectorAll('#navLinks a');
    const sections = document.querySelectorAll('section[id]');

    // ---- Navbar shrink + scroll-to-top visibility on scroll ----
    const onScroll = () => {
        const scrolled = window.scrollY > 40;
        navbar.classList.toggle('scrolled', scrolled);
        scrollTopBtn.classList.toggle('show', window.scrollY > 400);
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();

    // ---- Mobile hamburger menu ----
    navToggle.addEventListener('click', () => {
        const isOpen = navLinks.classList.toggle('open');
        navToggle.setAttribute('aria-expanded', isOpen);
        navToggle.innerHTML = isOpen
            ? '<i class="fa-solid fa-xmark"></i>'
            : '<i class="fa-solid fa-bars"></i>';
    });

    // close mobile menu after tapping a link
    links.forEach(link => {
        link.addEventListener('click', () => {
            navLinks.classList.remove('open');
            navToggle.setAttribute('aria-expanded', 'false');
            navToggle.innerHTML = '<i class="fa-solid fa-bars"></i>';
        });
    });

    // ---- Scroll-to-top trigger ----
    scrollTopBtn.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    // ---- Active nav link on scroll (scrollspy) ----
    const spy = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const id = entry.target.getAttribute('id');
                links.forEach(link => {
                    link.classList.toggle('active', link.getAttribute('href') === `#${id}`);
                });
            }
        });
    }, { rootMargin: '-45% 0px -50% 0px', threshold: 0 });

    sections.forEach(section => spy.observe(section));

    // ---- Reveal-on-scroll for sections ----
    const reveal = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('in-view');
                reveal.unobserve(entry.target);
            }
        });
    }, { threshold: 0.15 });

    document.querySelectorAll('.reveal').forEach(el => reveal.observe(el));

});
