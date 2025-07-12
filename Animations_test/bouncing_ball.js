let bouncing_ball = document.getElementById("bouncing_ball");
let alture = 0
state = 0;

function animateBouncingBall() {
    state = true
    console.log("Bouncing ball animation started");
}

function fall() {
    if (alture < 300) {
        alture++;
        bouncing_ball.style.left = alture - "px";
        requestAnimationFrame(fall);
    } else {
        alture = 0; // Reset position after reaching the bottom
        bouncing_ball.style.left = alture - "px";
    }
    console.log(alture);
}

// if (state) {
fall();
// }