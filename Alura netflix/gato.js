audio = document.getElementById("audiodasilva");


document.addEventListener("mouseenter", (event) => {
    if (event.target.classList.contains("gato")) {
        audio.play();
    }
}, true);

document.addEventListener("mouseout", (event) => {
    if (event.target.classList.contains("gato")) {
        audio.onpause();
    }
}, true);