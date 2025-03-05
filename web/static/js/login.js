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
        loginForm.addEventListener("submit", function(event) {
            event.preventDefault(); // Evitar recarga de la página

            const username = document.getElementById("username").value;
            const password = document.getElementById("password").value;

            fetch("/Login", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ username, password })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert(`✅ ¡Bienvenido, ${data.user_name}!`);

                    // Guardamos el nombre y ID en el localStorage (opcional)
                    localStorage.setItem("user_id", data.user_id);
                    localStorage.setItem("user_name", data.user_name);

                    // Redirigir a la vista de módulos
                    window.location.href = "/ModulosVista";
                } else {
                    alert("❌ " + data.error);
                }
            })
            .catch(error => console.error("❌ Error en login:", error));
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
