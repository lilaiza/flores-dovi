document.addEventListener("DOMContentLoaded", () => {
    const flores = document.querySelectorAll(".flor");
    const brillos = document.querySelectorAll(".brillo");
    const mensaje = document.querySelector(".mensaje");

    // Efecto al hacer hover sobre las flores
    flores.forEach(flor => {
        flor.addEventListener("mouseover", () => {
            flor.style.filter = "drop-shadow(0 0 15px rgba(255, 105, 180, 0.8))";
        });

        flor.addEventListener("mouseout", () => {
            flor.style.filter = "";
        });

        // Efecto al hacer click en flores individuales
        flor.addEventListener("click", (e) => {
            e.stopPropagation();
            const randomRotation = Math.random() * 360;
            flor.style.transform = `scale(1.3) rotate(${randomRotation}deg)`;
            setTimeout(() => {
                flor.style.transform = "";
            }, 1000);
        });
    });

    // Efecto especial al hacer click en el mensaje
    mensaje.addEventListener("click", () => {
        mensaje.style.transform = "translateX(-50%) scale(1.2)";
        mensaje.style.color = "#ff0080";
        
        setTimeout(() => {
            mensaje.style.transform = "translateX(-50%)";
            mensaje.style.color = "#ff1493";
        }, 500);
    });

    // Animación aleatoria periódica
    setInterval(() => {
        const randomFlor = flores[Math.floor(Math.random() * flores.length)];
        randomFlor.style.transform = "scale(1.2)";
        setTimeout(() => {
            randomFlor.style.transform = "";
        }, 500);
    }, 3000);
});