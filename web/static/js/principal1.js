document.addEventListener('DOMContentLoaded', () => {
    // Elementos del DOM
    const moduleGrid = document.querySelector('.modules-grid');
    const moduleDetails = document.getElementById('module-details');
    const moduleTitle = document.getElementById('module-title');
    const moduleDescription = document.getElementById('module-description');
    const questionsList = document.getElementById('questions-list');
    const completarBtn = document.getElementById('completar-modulo');
    const closeBtn = document.getElementById('close-modulos');

    let currentModuleId = null;
    let userId = document.getElementById('user-id')?.value || 1;

    // Cargar módulos desde la API
    fetch('/Modulos')
        .then(response => response.json())
        .then(modulos => {
            moduleGrid.innerHTML = '';

            modulos.forEach(modulo => {
                const moduleCard = document.createElement('div');
                moduleCard.classList.add('module-card');
                moduleCard.setAttribute('data-module', modulo.id_modulo);
                moduleCard.innerHTML = `
                    <h2>${modulo.titulo}</h2>
                    <p>${modulo.descripcion}</p>
                `;

                moduleCard.addEventListener('click', () => {
                    const moduloId = moduleCard.getAttribute('data-module');
                    if (!moduloId) {
                        console.error("⚠️ Error: El módulo seleccionado no tiene un ID válido.");
                        return;
                    }
                    cargarModulo(moduloId);
                });

                moduleGrid.appendChild(moduleCard);
            });

            applyModuleAnimations();
        })
        .catch(error => console.error('❌ Error al cargar los módulos:', error));

        function cargarModulo(moduloId) {
            fetch("/Modulos", {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ modulo_id: moduloId })
            })
            .then(response => response.json())
            .then(modulo => {
                if (!modulo || modulo.error) {
                    console.error("⚠️ Error: No se pudo obtener el módulo. Respuesta del servidor:", modulo);
                    alert("⚠️ No se encontró información para este módulo.");
                    return;
                }
        
                currentModuleId = modulo.id_modulo;
                moduleTitle.textContent = modulo.titulo;
                moduleDescription.textContent = modulo.descripcion_detallada || "Sin descripción disponible.";
                questionsList.innerHTML = '';
        
                if (modulo.preguntas && modulo.preguntas.length > 0) {
                    modulo.preguntas.forEach(pregunta => {
                        const preguntaItem = document.createElement('li');
                        preguntaItem.innerHTML = `
                            <strong>${pregunta.texto_pregunta}</strong>
                            <ul>
                                ${pregunta.opciones.map(opcion => `
                                    <li class="opcion" data-correcto="${opcion.es_correcta}">${opcion.texto}</li>
                                `).join('')}
                            </ul>
                        `;
                        questionsList.appendChild(preguntaItem);
                    });
                } else {
                    questionsList.innerHTML = "<p>Este módulo no tiene preguntas disponibles.</p>";
                }
        
                completarBtn.style.display = "block";
                moduleDetails.style.display = "block";
        
                asignarEventosRespuestas();
            })
            .catch(error => {
                console.error("❌ Error al obtener detalles del módulo:", error);
                alert("❌ Ocurrió un error al cargar el módulo. Inténtalo de nuevo.");
            });
        }
        

        function asignarEventosRespuestas() {
            document.querySelectorAll('.opcion').forEach(opcion => {
                opcion.addEventListener('click', () => {
                    const preguntaContainer = opcion.closest('ul'); // Encuentra la lista de opciones de la pregunta
        
                    // Verificar si la pregunta ya fue respondida
                    if (preguntaContainer.classList.contains('respondido')) {
                        alert("⚠️ Solo puedes seleccionar una respuesta por pregunta.");
                        return;
                    }
        
                    // Marcar la respuesta seleccionada
                    if (opcion.dataset.correcto === "true") {
                        opcion.style.color = "green";
                        opcion.style.fontWeight = "bold";
                        alert("✅ Respuesta Correcta!");
                    } else {
                        opcion.style.color = "red";
                        opcion.style.fontWeight = "bold";
                        alert("❌ Respuesta Incorrecta");
                    }
        
                    // Marcar la pregunta como respondida
                    preguntaContainer.classList.add('respondido');
        
                    // Deshabilitar todas las opciones de la misma pregunta
                    preguntaContainer.querySelectorAll('.opcion').forEach(op => {
                        op.style.pointerEvents = "none"; // Evita más clics
                        op.style.opacity = "0.6"; // Reduce la visibilidad de las opciones no seleccionadas
                    });
                });
            });
        }
        

    completarBtn.addEventListener('click', () => {
        if (!currentModuleId) {
            alert("⚠️ Selecciona un módulo primero.");
            return;
        }

        fetch('/Modulos', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ usuario_id: userId, modulo_id: currentModuleId })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert("✅ ¡Módulo completado! Revisa tus logros.");
            } else {
                alert("⚠️ Hubo un problema al completar el módulo.");
            }
        })
        .catch(error => console.error("❌ Error al completar módulo:", error));
    });

    closeBtn.addEventListener('click', () => {
        moduleDetails.style.display = 'none';
        moduleTitle.textContent = "Selecciona un módulo para profundizar";
        moduleDescription.textContent = "Explora contenido detallado y recursos interactivos";
    });

    // Aplicar animaciones a los módulos al pasar el mouse
    function applyModuleAnimations() {
        const moduleCards = document.querySelectorAll('.module-card');
        moduleCards.forEach(card => {
            card.addEventListener('mouseenter', () => card.classList.add('hover-effect'));
            card.addEventListener('mouseleave', () => card.classList.remove('hover-effect'));
        });
    }

    // Configurar navegación entre secciones
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

    console.log("✅ `principal1.js` cargado correctamente.");
});
