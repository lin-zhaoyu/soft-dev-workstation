// Team PurplePotatoes2 :: Zhao Yu Lin, Christopher Liu, Deven Maheshwari
// SoftDev pd0
// K31 -- canvas based JS animation
// 2022-02-15t

// model for HTML5 canvas-based animation

// SKEELTON


//access canvas and buttons via DOM
let c = document.getElementById("playground");
let dotButton = document.getElementById("buttonCircle");
let stopButton = document.getElementById("buttonStop");
//prepare to interact with canvas in 2D
let ctx = c.getContext("2d");

//set fill color to team color
ctx.fillStyle = "purple";

let requestID;  // init global let for use with animation frames

let radius = 0;
let growing = true;

let clear = (e) => {
  // growing = false;
  console.log(`clear invoked | growing status: ${growing} radius: ${radius}`);
  // console.log(`growing status: ${growing} radius: ${radius}`);
  ctx.clearRect(0, 0, c.clientWidth, c.clientHeight);
};
let clearB = (e) => {
  console.log("clear invoked!!!!");
  ctx.clearRect(0, 0, c.clientWidth, c.clientHeight);
};

stopButton.addEventListener("clear", clearB)
console.log("BIG STOP BUTTOn")



let drawDot = () => {
  console.log("drawDot invoked...")

  if (growing) {
    radius += 2;
  } else {
    radius -= 2;
  }

  clear();
  console.log("clear is called")
  ctx.beginPath;
  ctx.arc(c.clientWidth/2, c.clientHeight/2, radius, 0, 360);
  ctx.fill();

  if (radius >= 250) {
    console.log(`too big | growing status: ${growing} radius: ${radius}`);
    window.cancelAnimationFrame(requestID);
    growing = false;
    clear();
    requestID = window.requestAnimationFrame(drawDot);
  } else if (radius <= 0) {
    console.log(`too small | growing status: ${growing} radius: ${radius}`);
    window.cancelAnimationFrame(requestID);
    growing = true;
    clear();
    requestID = window.requestAnimationFrame(drawDot);
  } else {
    console.log(`just right | growing status: ${growing} radius: ${radius}`);
    requestID = window.requestAnimationFrame(drawDot);
  }


  // YOUR CODE HERE

  /*
    ...to
    Wipe the canvas,
    Repaint the circle,
    ...and somewhere (where/when is the right time?)
    Update requestID to propagate the animation.
    You will need
    window.cancelAnimationFrame()
    window.requestAnimationFrame()
   */
};


let stopIt = () => {
  console.log("stopIt invoked...")
  console.log( requestID );

  // YOUR CODE HERE
  /*
    ...to
    Stop the animation
    You will need
    window.cancelAnimationFrame()
  */
};


dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);
