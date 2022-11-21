

var canvas;

let particles = []
let cam1, cam2;
let currentCamera;
let plus = 200;

function setup() {
    createCanvas(windowWidth, windowHeight, WEBGL);
    angleMode(DEGREES);

    cam1 = createCamera();
    cam2 = createCamera();
    cam2.setPosition(30, 0, 50);
    cam2.lookAt(0, 0, 0);
    cam2.ortho();


    currentCamera = 1;
}


class spaceship {
    constructor(x, y, z, size, direction, mass) {
        this.x = x;
        this.y = y;
        this.z = z;
        this.size = size;
        this.direction = direction;
        this.mass = mass;

    }
    draw() {

        push();



        translate(this.x - width / 2, this.y - width / 2, this.z - width / 2);


        push();
        rotateX(angle * 0.7);
        rotateY(angle * 0.7);
        fill(230, 150, 150);
        sphere(30, 24, 16);
        torus(100, 10);
        pop();

        push();

        fill(10, random(100, 200), 150);
        sphere(30, 24, 16);

        pop();

        angle += 0.07

        pop();
    }

}



function draw() {
    background(0, 0, 30);
    ellipsoid(30, 40, 40);
    cam1.lookAt(0, 0, 0);
    cam1.setPosition(200 * sin(plus), 0, 200 * cos(plus));
    plus += 1
    setCamera(cam1);


    if (random(1) > 0.97) {

        // var x = random(-100, 100);
        // var y = random(-100, 100);
        // var z = random(-100, 100);
        var pos = createVector(0, 0, 0);


        for (var i = 0; i < 100; i++) {

            // var r = map(sin(frameCount),-1,1,0,255)+random(-50,50);
            // var g = map(sin(frameCount),-1,1,255,0)+random(-50,50);
            // var b = map(sin(frameCount),-1,1,0,255)+random(-50,50);


            var p = new Particle(pos)
            particles.push(p)
        }
    }

    for (var i = particles.length - 1; i >= 0; i--) {
        if (dist(particles[i].pos.x, particles[i].pos.y, particles[i].pos.z, 0, 0, 0) < 500) {
            particles[i].update();
            particles[i].show();
        } else {
            particles.splice(i, 1)
        }
    }
}

class Particle {
    constructor(pos, c) {
        this.pos = createVector(pos.x, pos.y, pos.z);
        this.vel = p5.Vector.random3D().normalize().mult(random(4, 6))

        this.c = c;

        // this.detailX = createSlider(3, 16, 3);
        // this.detailX.position(10, height + 5);
        // this.detailX.style('width', '80px');
    }
    update() {
        this.pos.add(this.vel)
    }
    show() {
        push();
        stroke(100);
        fill(255, 255, 255, 180)
        translate(this.pos.x, this.pos.y, this.pos.z);


        // rotateX(millis() / 10);
        // rotateY(millis() / 10);
        // rotateY(millis() / 10);
        box(15, 15, 15);




        pop();
    }
}