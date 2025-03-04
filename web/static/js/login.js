// Función para mostrar notificaciones
// Función para mostrar notificaciones
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

// Esperar a que el DOM cargue completamente
document.addEventListener("DOMContentLoaded", function() {
    const loginForm = document.getElementById("formularioLogin");

    if (loginForm) {
        loginForm.addEventListener("submit", function(e) {
            e.preventDefault(); // Evita la recarga de la página
            
            // Recoger los valores del formulario
            const username = document.getElementById("username").value.trim();
            const password = document.getElementById("password").value.trim();

            // Validaciones básicas
            if (!username || !password) {
                mostrarNotificacion("Por favor, complete todos los campos", "error");
                return;
            }

            // Datos a enviar
            const datosLogin = {
                username: username,
                password: password
            };

            console.log("📡 Enviando datos al servidor:", datosLogin);

            // Enviar datos al backend con fetch()
            fetch("/Login", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(datosLogin)
            })
            .then(response => response.json())
            .then(data => {
                console.log("📡 Respuesta del servidor:", data);

                if (data.success) {
                    mostrarNotificacion(`¡Bienvenido, ${data.user}!`, "success");
                    
                    // Redirigir al usuario después de 2 segundos
                    setTimeout(() => {
                        window.location.href = "/";
                    }, 2000);
                } else {
                    mostrarNotificacion(data.error || "Credenciales incorrectas", "error");
                }
            })
            .catch(error => {
                console.error("❌ Error en la solicitud:", error);
                mostrarNotificacion("Error al conectarse con el servidor", "error");
            });
        });
    }


    // Manejadores de eventos para los enlaces adicionales
    const olvidoContrasena = document.getElementById("olvidoContrasena");
    if (olvidoContrasena) {
        olvidoContrasena.addEventListener("click", function(e) {
            e.preventDefault();
            mostrarNotificacion("Función de recuperación de contraseña próximamente", "error");
        });
    }

    const registrarse = document.getElementById("registrarse");
    if (registrarse) {
        registrarse.addEventListener("click", function(e) {
            e.preventDefault();
            mostrarNotificacion("Redirigiendo a registro", "success");
            setTimeout(() => {
                window.location.href = "/Registro";
            }, 1000);
        });
    }
});
