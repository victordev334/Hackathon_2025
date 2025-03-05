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

    // Function to hide all full-screen sections
    function hideAllFullScreenSections() {
        Object.values(sections).forEach(section => {
            section.fullScreen.classList.add('hidden');
        });
    }

    // Event listeners for navigation links
    Object.entries(sections).forEach(([name, section]) => {
        section.link.addEventListener('click', (e) => {
            e.preventDefault();
            hideAllFullScreenSections();
            section.fullScreen.classList.remove('hidden');
        });

        if (section.closeBtn) {
            section.closeBtn.addEventListener('click', () => {
                section.fullScreen.classList.add('hidden');
            });
        }
    });

    // Módulos interactions
    const moduleCards = document.querySelectorAll('.module-card');
    const moduleTitle = document.getElementById('module-title');
    const moduleDescription = document.getElementById('module-description');

    const modulosData = {
        1: {
            title: "Grooming: Conceptos Fundamentales",
            description: "Análisis profundo del acoso sexual online, sus características, impactos psicológicos y sociales en menores."
        },
        2: {
            title: "Psicología del Groomer",
            description: "Estrategias de manipulación emocional, técnicas de engaño y perfilamiento de acosadores en entornos digitales."
        },
        3: {
            title: "Identificación de Riesgos Digitales",
            description: "Señales de alerta, comportamientos sospechosos y herramientas para reconocer situaciones de peligro online."
        },
        4: {
            title: "Estrategias de Protección Digital",
            description: "Técnicas avanzadas de prevención, configuración de privacidad y protocolos de seguridad para menores."
        },
        5: {
            title: "Seguridad en Redes Sociales",
            description: "Guía completa para gestionar configuraciones de privacidad, filtrar contactos y navegar con seguridad."
        },
        6: {
            title: "Marco Legal del Grooming",
            description: "Legislación vigente, consecuencias legales y recursos jurídicos contra el acoso sexual online."
        }
    };

    moduleCards.forEach(card => {
        card.addEventListener('click', () => {
            const moduleId = card.getAttribute('data-module');
            const moduleInfo = modulosData[moduleId];

            moduleTitle.textContent = moduleInfo.title;
            moduleDescription.textContent = moduleInfo.description;
        });
    });

    // Denuncias Interactive Guide
    const denunciasFullScreen = document.getElementById('denuncias-full-screen');
    const pasosDenunciaContainer = document.createElement('div');
    pasosDenunciaContainer.id = 'pasos-denuncia-container';
    pasosDenunciaContainer.classList.add('pasos-denuncia-container');

    const paginasDenuncia = [
        {
            titulo: 'Paso 1: Recopila Evidencias',
            contenido: `
                <div class="denuncia-card">
                    <h3>Conserva las Pruebas</h3>
                    <ul>
                        <li>No borres ninguna conversación</li>
                        <li>Toma capturas de pantalla detalladas</li>
                        <li>Registra fechas y horas exactas</li>
                        <li>Documenta todos los detalles relevantes</li>
                    </ul>
                    <p class="consejo">Consejo Pro: Usa múltiples métodos de captura</p>
                </div>
            `
        },
        {
            titulo: 'Paso 2: Busca Apoyo',
            contenido: `
                <div class="denuncia-card">
                    <h3>Red de Apoyo</h3>
                    <ul>
                        <li>Comunica la situación a adultos de confianza</li>
                        <li>Contacta orientadores escolares</li>
                        <li>Busca apoyo psicológico especializado</li>
                        <li>Mantén la calma y no te avergüences</li>
                    </ul>
                    <p class="consejo">Recuerda: Tienes derecho a estar seguro</p>
                </div>
            `
        },
        {
            titulo: 'Paso 3: Denuncia Oficial',
            contenido: `
                <div class="denuncia-card">
                    <h3>Canales de Denuncia</h3>
                    <ul>
                        <li>Contacta autoridades especializadas</li>
                        <li>Utiliza líneas de ayuda nacionales</li>
                        <li>Denuncia en plataformas online</li>
                        <li>Presenta evidencia recopilada</li>
                    </ul>
                    <p class="consejo">Actúa rápido, tu seguridad es primordial</p>
                </div>
            `
        }
    ];

    // Crear navegación de páginas
    const paginacionContainer = document.createElement('div');
    paginacionContainer.classList.add('paginacion-denuncia');

    const contenidoPagina = document.createElement('div');
    contenidoPagina.classList.add('contenido-pagina');

    let paginaActual = 0;

    function mostrarPagina(index) {
        contenidoPagina.innerHTML = paginasDenuncia[index].contenido;
        
        // Actualizar botones de navegación
        paginacionContainer.innerHTML = `
            <button id="btn-anterior" ${index === 0 ? 'disabled' : ''}>Anterior</button>
            <span>Paso ${index + 1} de ${paginasDenuncia.length}</span>
            <button id="btn-siguiente" ${index === paginasDenuncia.length - 1 ? 'disabled' : ''}>Siguiente</button>
        `;

        // Añadir event listeners
        const btnAnterior = document.getElementById('btn-anterior');
        const btnSiguiente = document.getElementById('btn-siguiente');

        if (btnAnterior) {
            btnAnterior.addEventListener('click', () => {
                if (paginaActual > 0) {
                    paginaActual--;
                    mostrarPagina(paginaActual);
                }
            });
        }

        if (btnSiguiente) {
            btnSiguiente.addEventListener('click', () => {
                if (paginaActual < paginasDenuncia.length - 1) {
                    paginaActual++;
                    mostrarPagina(paginaActual);
                }
            });
        }
    }

    // Añadir elementos al contenedor
    pasosDenunciaContainer.appendChild(contenidoPagina);
    pasosDenunciaContainer.appendChild(paginacionContainer);

    // Insertar en el contenedor de denuncias
    const denunciasGrid = denunciasFullScreen.querySelector('.denuncias-grid');
    if (denunciasGrid) {
        denunciasGrid.appendChild(pasosDenunciaContainer);
    }

    // Mostrar primera página
    mostrarPagina(0);

    // Optional: Add smooth scroll behavior
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});