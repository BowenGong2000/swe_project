var canvas;
let video;
let poseNet;
let noseX = 0;
let noseY = 0;
let eyelX = 0;
let eyelY = 0;



function setup() {
    createCanvas(windowWidth, windowHeight);
    video = createCapture(VIDEO);
    video.hide();
    poseNet = ml5.poseNet(video, modelReady);
    poseNet.on('pose', gotPoses);

}

function gotPoses(poses) {
    // console.log(poses);
    if (poses.length > 0) {
        let nX = poses[0].pose.keypoints[10].position.x;
        let nY = poses[0].pose.keypoints[10].position.y;
        let eX = poses[0].pose.keypoints[9].position.x;
        let eY = poses[0].pose.keypoints[9].position.y;
        noseX = lerp(noseX, nX, 0.7);
        noseY = lerp(noseY, nY, 0.7);
        eyelX = lerp(eyelX, eX, 0.7);
        eyelY = lerp(eyelY, eY, 0.7);
    }
}

function modelReady() {
    console.log('model ready');
}



function draw() {

    background(220);
    image(video, 0, 0);


    push()
    fill(255, 0, 0);
    ellipse(noseX, noseY, 20);
    pop()

    push()
    fill(255, 0, 0);
    ellipse(eyelX, eyelY, 20);
    pop()
}






