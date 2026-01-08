// Terra Retail - Main JavaScript

// Auto-hide messages after 5 seconds
document.addEventListener('DOMContentLoaded', function() {
    const messages = document.querySelectorAll('.message');
    messages.forEach(message => {
        setTimeout(() => {
            message.style.animation = 'slideOutRight 0.3s ease-out';
            setTimeout(() => message.remove(), 300);
        }, 5000);
    });
});

// Mobile menu toggle
function toggleMobileMenu() {
    const sidebar = document.getElementById('sidebar');
    sidebar.classList.toggle('-translate-x-full');
}

// Cerrar sidebar en mobile al hacer click afuera
document.addEventListener('click', function(event) {
    const sidebar = document.getElementById('sidebar');
    const menuButton = document.getElementById('mobile-menu-button');

    if (window.innerWidth < 768 &&
        sidebar &&
        !sidebar.contains(event.target) &&
        !menuButton.contains(event.target) &&
        !sidebar.classList.contains('-translate-x-full')) {
        sidebar.classList.add('-translate-x-full');
    }
});

// Slide out animation
const style = document.createElement('style');
style.textContent = `
    @keyframes slideOutRight {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// HTMX: Mostrar indicador de carga en requests
document.body.addEventListener('htmx:beforeRequest', function(evt) {
    console.log('HTMX Request iniciado:', evt.detail.path);
});

document.body.addEventListener('htmx:afterRequest', function(evt) {
    console.log('HTMX Request completado:', evt.detail.path);
});

// Utilidad: Confirmar acción
function confirmarAccion(mensaje) {
    return confirm(mensaje || '¿Está seguro de realizar esta acción?');
}

// Utilidad: Formatear números como moneda
function formatearMoneda(numero) {
    return new Intl.NumberFormat('es-AR', {
        style: 'currency',
        currency: 'ARS'
    }).format(numero);
}

// Utilidad: Formatear fecha
function formatearFecha(fecha) {
    return new Intl.DateTimeFormat('es-AR', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    }).format(new Date(fecha));
}
