document.addEventListener('DOMContentLoaded', () => {
    // Elementos del DOM
    const moduleGrid = document.querySelector('.modules-grid');
    const moduleTitle = document.getElementById('module-title');
    const moduleDescription = document.getElementById('module-description');

    // Cargar módulos desde la API
    fetch('/Modulos')
        .then(response => response.json())
        .then(modulos => {
            moduleGrid.innerHTML = '';  // Limpiar módulos previos

            modulos.forEach(modulo => {
                const moduleCard = document.createElement('div');
                moduleCard.classList.add('module-card');
                moduleCard.setAttribute('data-module', modulo.id_modulo);
                moduleCard.innerHTML = `
                    <h2>${modulo.emoji} ${modulo.titulo}</h2>
                    <p>${modulo.descripcion}</p>
                `;

                moduleCard.addEventListener('click', () => {
                    fetch('/Modulos', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ modulo_id: modulo.id_modulo })
                    })
                    .then(response => response.json())
                    .then(data => {
                        moduleTitle.textContent = data.titulo;
                        moduleDescription.textContent = data.descripcion_detallada;
                    })
                    .catch(error => console.error('Error al obtener detalles del módulo:', error));
                });

                moduleGrid.appendChild(moduleCard);
            });

            applyModuleAnimations();
        })
        .catch(error => console.error('Error al cargar los módulos:', error));

    function applyModuleAnimations() {
        const moduleCards = document.querySelectorAll('.module-card');
        moduleCards.forEach(card => {
            card.addEventListener('mouseenter', () => card.classList.add('hover-effect'));
            card.addEventListener('mouseleave', () => card.classList.remove('hover-effect'));
        });
    }

    document.addEventListener('DOMContentLoaded', () => {
        const sections = {
            'modulos': {
                link: document.getElementById('modulos-link'),
                fullScreen: document.getElementById('modulos-full-screen'),
                closeBtn: document.getElementById('close-modulos')
            },
            'estadisticas': {
                link: document.getElementById('estadisticas-link'),
                fullScreen: document.getElementById('estadisticas-full-screen'),
                closeBtn: document.getElementById('close-estadisticas')
            },
            'denuncias': {
                link: document.getElementById('denuncias-link'),
                fullScreen: document.getElementById('denuncias-full-screen'),
                closeBtn: document.getElementById('close-denuncias')
            },
            'recursos': {
                link: document.getElementById('recursos-link'),
                fullScreen: document.getElementById('recursos-full-screen'),
                closeBtn: document.getElementById('close-recursos')
            },
            'bot': {
                link: document.getElementById('bot-link'),
                fullScreen: document.getElementById('bot-full-screen'),
                closeBtn: document.getElementById('close-bot')
            }
        };
    
        function hideAllFullScreenSections() {
            Object.values(sections).forEach(section => {
                if (section.fullScreen) {
                    section.fullScreen.classList.add('hidden');
                }
            });
        }
    
        Object.entries(sections).forEach(([name, section]) => {
            if (section.link) {
                section.link.addEventListener('click', (e) => {
                    e.preventDefault();
                    hideAllFullScreenSections();
                    if (section.fullScreen) {
                        section.fullScreen.classList.remove('hidden');
                    }
                });
            }
    
            if (section.closeBtn) {
                section.closeBtn.addEventListener('click', () => {
                    if (section.fullScreen) {
                        section.fullScreen.classList.add('hidden');
                    }
                });
            }
        });
    
        // Agregar smooth scroll a los enlaces internos
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const targetElement = document.querySelector(this.getAttribute('href'));
                if (targetElement) {
                    targetElement.scrollIntoView({ behavior: 'smooth' });
                }
            });
        });
    
        console.log("✅ `principal1.js` se ejecutó correctamente.");
    });
});
