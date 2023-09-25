function scrollToSection(sectionId) {
    const section = document.querySelector(sectionId);
    if (section) {
        window.scrollTo({
            behavior: 'smooth', // Desplazamiento suave
            top: section.offsetTop, // Posición superior de la sección
        });
    }
}

// Asociar la función al clic en el enlace "Nosotros"
const nosotrosLink = document.querySelector('a[href="#we"]');
if (nosotrosLink) {
    nosotrosLink.addEventListener('click', (event) => {
        event.preventDefault(); // Evita el comportamiento predeterminado del enlace
        scrollToSection('#we'); // Llama a la función de desplazamiento
    });
}



// Encuentra el enlace "Contacto" en el menú de navegación
const contactoLink = document.querySelector('nav a[href="#footer"]');

// Agrega un controlador de eventos para el clic en el enlace "Contacto"
contactoLink.addEventListener('click', (event) => {
    event.preventDefault(); // Evita el comportamiento predeterminado del enlace
    scrollToSection('#footer'); // Llama a la función para desplazar hacia abajo
});

// Función para desplazar hacia la sección objetivo sin animación
function scrollToSection(sectionId) {
    const section = document.querySelector(sectionId);
    if (section) {
        window.scrollTo({
            top: section.offsetTop, // Posición superior de la sección
            behavior: 'smooth', // Desplazamiento suave
        });
    }
}



