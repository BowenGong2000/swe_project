gsap.registerPlugin(ScrollTrigger);

gsap.to(".square", {
    x: 0,
    duration: 8,
    scrollTrigger: {
        trigger: ".square_2",
        start: "top 50%",
        end: "top 20%",
        scrub: 4,
        toggleActions: "restart reverse         none           none",
        //             onEnter onLeave       onEnterback    onleaveBack
        markers: {
            startColor: "purple",
            endColor: "fuchsia",
        },
    }
})


gsap.to(".square_2", {
    x: 100,
    duration: 8,
    scrollTrigger: {
        trigger: ".square_2",
        start: "top 50%",
        end: "top 20%",
        scrub: 4,
        toggleActions: "restart reverse         none           none",
        //             onEnter onLeave       onEnterback    onleaveBack
        // markers: {
        //     startColor: "green",
        //     endColor: "black",
        // },
    }
})


gsap.to(".square_3", {
    x: 0,
    duration: 8,
    scrollTrigger: {
        trigger: ".square_2",
        start: "top 50%",
        end: "top 20%",
        scrub: 4,
        toggleActions: "restart reverse         none           none",
        //             onEnter onLeave       onEnterback    onleaveBack
        // markers: {
        //     startColor: "gold",
        //     endColor: "white",
        // },
    }
})


gsap.to(".square_4", {
    x: 100,
    duration: 8,
    scrollTrigger: {
        trigger: ".square_2",
        start: "top 50%",
        end: "top 20%",
        scrub: 4,
        toggleActions: "restart reverse         none           none",
        //             onEnter onLeave       onEnterback    onleaveBack
        // markers: {
        //     startColor: "yellow",
        //     endColor: "purple",
        // },
    }
})



function openNav() {
    document.getElementById("mySidepanel").style.width = '50%';
}

/* Set the width of the sidebar to 0 (hide it) */
function closeNav() {
    document.getElementById("mySidepanel").style.width = "0";
}


function openNav_2() {
    document.getElementById("mySidepanel_2").style.width = '50%';
}

/* Set the width of the sidebar to 0 (hide it) */
function closeNav_2() {
    document.getElementById("mySidepanel_2").style.width = "0";
}


function openNav_3() {
    document.getElementById("mySidepanel_3").style.width = '50%';
}

/* Set the width of the sidebar to 0 (hide it) */
function closeNav_3() {
    document.getElementById("mySidepanel_3").style.width = "0";
}


function openNav_4() {
    document.getElementById("mySidepanel_4").style.width = '50%';
}

/* Set the width of the sidebar to 0 (hide it) */
function closeNav_4() {
    document.getElementById("mySidepanel_4").style.width = "0";
}


function openNav_5() {
    document.getElementById("mySidepanel_5").style.width = '50%';
}

/* Set the width of the sidebar to 0 (hide it) */
function closeNav_5() {
    document.getElementById("mySidepanel_5").style.width = "0";
}