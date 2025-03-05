// Autor: Diego 
function irAModulos() {
    alert('Redirigiendo a los módulos de aprendizaje...');
    window.location.href = 'modulos.html';
}

function denunciar() {
    alert('Dirigiéndote a un centro de denuncias');
    window.location.href = 'https://www.denuncias.gob';
}

// Advanced Scroll and Reveal Animations
document.addEventListener('DOMContentLoaded', () => {
const sections = document.querySelectorAll('section');
const headerTitle = document.querySelector('header h1');
const navLinks = document.querySelectorAll('nav ul li a');

// Intersection Observer for Section Animations
const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.1
};

const sectionObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('section-visible');
            
            // Additional animation based on section ID
            switch(entry.target.id) {
                case 'info':
                    animateInfoSection(entry.target);
                    break;
                case 'estadisticas':
                    animateStatisticsSection(entry.target);
                    break;
                case 'modulos':
                    animateModulesSection(entry.target);
                    break;
                case 'denuncias':
                    animateDenunciasSection(entry.target);
                    break;
            }
        }
    });
}, observerOptions);

// Observe all sections
sections.forEach(section => {
    section.classList.add('section-hidden');
    sectionObserver.observe(section);
});

// Header Title Animation
function animateHeaderTitle() {
    headerTitle.classList.add('title-animation');
    headerTitle.addEventListener('animationend', () => {
        headerTitle.classList.remove('title-animation');
    });
}
animateHeaderTitle();

// Nav Links Hover Effects
navLinks.forEach(link => {
    link.addEventListener('mouseenter', () => {
        link.classList.add('link-hover');
    });
    link.addEventListener('mouseleave', () => {
        link.classList.remove('link-hover');
    });
});

// Specific Section Animations
function animateInfoSection(section) {
    const paragraph = section.querySelector('p');
    paragraph.classList.add('slide-in-right');
}

function animateStatisticsSection(section) {
    const paragraph = section.querySelector('p');
    paragraph.classList.add('pulse-animation');
}

function animateModulesSection(section) {
    const button = section.querySelector('button');
    button.classList.add('bounce-in');
}

function animateDenunciasSection(section) {
    const button = section.querySelector('button');
    button.classList.add('shake-animation');
}

// Button Interaction Enhancements
const buttons = document.querySelectorAll('button');
buttons.forEach(button => {
    button.addEventListener('click', (e) => {
        button.classList.add('button-click');
        setTimeout(() => {
            button.classList.remove('button-click');
        }, 300);
    });
});
});

// Custom Function Enhancements
function irAModulos() {
const confirmacion = confirm('¿Estás seguro de que quieres ir a los módulos de aprendizaje? Esta información es importante.');
if (confirmacion) {
    window.location.href = 'modulos.html';
}
}

function denunciar() {
const confirmacion = confirm('Estás a punto de ser redirigido a un centro de denuncias. ¿Deseas continuar?');
if (confirmacion) {
    window.location.href = 'https://www.denuncias.gob';
}
}

document.addEventListener("DOMContentLoaded", function() {
    const loginBtn = document.getElementById("loginBtn");
    if (loginBtn) {
        loginBtn.addEventListener("click", function() {
            window.location.href = "/Login";
        });
    }
});

document.addEventListener("DOMContentLoaded", function() {
    const loginBtn = document.getElementById("registerBtn");
    if (loginBtn) {
        loginBtn.addEventListener("click", function() {
            window.location.href = "/Registro";
        });
    }
});
