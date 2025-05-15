// Navegación suave al hacer clic en los enlaces del menú
document.querySelectorAll('a.nav-link').forEach(link => {
    link.addEventListener('click', event => {
        event.preventDefault();
        const targetId = link.getAttribute('href').substring(1);
        const targetElement = document.getElementById(targetId);

        if (targetElement) {
            window.scrollTo({
                top: targetElement.offsetTop - 70, // Ajuste para la altura del navbar
                behavior: 'smooth'
            });
        }
    });
});

// Validación del formulario
document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("#encuesta form");
    if (form) {
        form.addEventListener("submit", event => {
            event.preventDefault();
            const nombre = document.getElementById("nombre")?.value.trim();
            const correo = document.getElementById("correo")?.value.trim();
            const experiencia = document.getElementById("experiencia")?.value;

            if (!nombre || !correo || experiencia === "Selecciona una opción") {
                alert("Por favor completa todos los campos.");
            } else {
                alert(`Gracias por responder la encuesta, ${nombre}!`);
                form.reset();
            }
        });
    }
});

// Botón "Volver arriba"
const volverArribaBtn = document.querySelector('a[href="#"]');
if (volverArribaBtn) {
    volverArribaBtn.addEventListener('click', event => {
        event.preventDefault();
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
}
