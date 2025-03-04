
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

document.getElementById('formularioRegistro').addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Recoger los valores del formulario
    const username = document.getElementById('username').value;
    const nombre = document.getElementById('nombre').value;
    const primerApellido = document.getElementById('primerApellido').value;
    const segundoApellido = document.getElementById('segundoApellido').value;
    const correo = document.getElementById('correo').value;

    // Validaciones básicas
    if (!username || !nombre || !primerApellido || !correo) {
        mostrarNotificacion('Por favor, complete todos los campos obligatorios', 'error');
        return;
    }

    // Validar formato de correo
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(correo)) {
        mostrarNotificacion('Por favor, ingrese un correo electrónico válido', 'error');
        return;
    }

    // Datos de registro
    const datosRegistro = {
        username,
        nombre,
        primerApellido,
        segundoApellido,
        correo
    };

    // Simular envío de datos (reemplazar con lógica real de backend)
    console.log('Datos de registro:', datosRegistro);

    // Mostrar notificación de éxito
    mostrarNotificacion(`¡Registro exitoso, bienvenido ${nombre}!`);

    // Limpiar formulario
    this.reset();
});