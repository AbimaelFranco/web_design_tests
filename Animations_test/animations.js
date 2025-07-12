let ball = document.getElementById("ball");
let pos = 0;

function move() {
    if (pos < 300) {
        pos++;
        ball.style.left = pos + "px";
        requestAnimationFrame(move);
    }
}

function animateBox() {
    document.getElementById("box").classList.toggle("animate");
}

move();