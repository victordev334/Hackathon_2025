        // Función para mostrar notificación
        function mostrarNotificacion(mensaje, tipo = 'success') {
            const notificacion = document.getElementById('notification');
            const mensajeElemento = notificacion.querySelector('.notification-message');
            const iconoElemento = notificacion.querySelector('.notification-icon');

            // Limpiar clases previas
            notificacion.className = '';
            
            // Establecer clase y ícono según el tipo
            notificacion.classList.add(tipo);
            iconoElemento.textContent = tipo === 'success' ? '✓' : '✗';

            // Establecer mensaje
            mensajeElemento.textContent = mensaje;

            // Mostrar notificación
            notificacion.style.display = 'block';

            // Ocultar después de 3 segundos
            setTimeout(() => {
                notificacion.style.display = 'none';
            }, 3500);
        }

        document.getElementById('formularioLogin').addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Recoger los valores del formulario
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;

            // Validaciones básicas
            if (!username || !password) {
                mostrarNotificacion('Por favor, complete todos los campos', 'error');
                return;
            }

            // Simular validación de credenciales
            // En un escenario real, esto sería una llamada a un backend
            if (username === 'usuario' && password === 'contrasena') {
                mostrarNotificacion(`¡Bienvenido, ${username}!`);
                
                // Simular redirección (en un caso real, usarías window.location)
                setTimeout(() => {
                    console.log('Redirigiendo al dashboard');
                }, 2000);
            } else {
                mostrarNotificacion('Credenciales incorrectas', 'error');
            }
        });

        // Manejadores para links adicionales
        document.getElementById('olvidoContrasena').addEventListener('click', function(e) {
            e.preventDefault();
            mostrarNotificacion('Función de recuperación de contraseña próximamente', 'error');
        });

        document.getElementById('registrarse').addEventListener('click', function(e) {
            e.preventDefault();
            mostrarNotificacion('Redirigiendo a registro', 'success');
            // En un caso real, aquí redirigirías a la página de registro
            console.log('Redirigiendo a registro');
        });