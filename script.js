
document.addEventListener('DOMContentLoaded', () => {
    // Smooth scrolling for navigation links
    document.querySelectorAll('a.nav-link, .btn, #scroll-to-top').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            if (this.hash !== '') {
                e.preventDefault();
                const hash = this.hash;
                const targetElement = document.querySelector(hash);

                if (targetElement) {
                    const headerOffset = document.querySelector('.header').offsetHeight;
                    const elementPosition = targetElement.getBoundingClientRect().top + window.pageYOffset;
                    const offsetPosition = elementPosition - headerOffset;

                    window.scrollTo({
                        top: offsetPosition,
                        behavior: 'smooth'
                    });

                    // Close mobile nav if open
                    if (document.body.classList.contains('nav-open')) {
                        document.body.classList.remove('nav-open');
                        navToggle.classList.remove('active');
                        navbar.classList.remove('active');
                    }
                }
            }
        });
    });

    // Mobile Navigation Toggle
    const navToggle = document.querySelector('.nav-toggle');
    const navbar = document.querySelector('.navbar');
    const navLinks = document.querySelectorAll('.nav-link');

    navToggle.addEventListener('click', () => {
        document.body.classList.toggle('nav-open');
        navToggle.classList.toggle('active');
        navbar.classList.toggle('active');
    });

    // Close mobile nav when a link is clicked
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            if (document.body.classList.contains('nav-open')) {
                document.body.classList.remove('nav-open');
                navToggle.classList.remove('active');
                navbar.classList.remove('active');
            }
        });
    });

    // Highlight active nav link on scroll
    const sections = document.querySelectorAll('section');
    const navList = document.querySelector('.nav-list');
    const headerHeight = document.querySelector('.header').offsetHeight;

    const activateNavLink = () => {
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop - headerHeight - 1; // Adjusted for header height
            const sectionHeight = section.clientHeight;
            if (pageYOffset >= sectionTop && pageYOffset < sectionTop + sectionHeight) {
                current = section.getAttribute('id');
            }
        });

        navList.querySelectorAll('.nav-link').forEach(link => {
            link.classList.remove('active');
            if (link.href.includes(current)) {
                link.classList.add('active');
            }
        });
        // Special case for hero section when at very top
        if (window.scrollY === 0) {
            navList.querySelector('a[href="#hero"]').classList.add('active');
        }
    };

    window.addEventListener('scroll', activateNavLink);
    activateNavLink(); // Call on load to set initial active link

    // Scroll-to-top button functionality
    const scrollToTopBtn = document.getElementById('scroll-to-top');

    window.addEventListener('scroll', () => {
        if (window.pageYOffset > 300) { // Show button after scrolling 300px
            scrollToTopBtn.classList.add('show');
        } else {
            scrollToTopBtn.classList.remove('show');
        }
    });

    scrollToTopBtn.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    // Dynamically set current year in footer
    document.getElementById('current-year').textContent = new Date().getFullYear();
});
