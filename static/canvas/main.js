const canvas = document.getElementById("canvas");
canvas.width = 500;
canvas.height = 200;


let context = canvas.getContext("2d");
context.fillStyle = "white";
context.fillRect(0, 0, canvas.width, canvas.height);


let draw_color = "black";
let draw_width = ".4";
let is_drawing = false;

let mouse_posX = [];
let mouse_posY = [];

var mouseX_min
var mouseX_max


canvas.addEventListener("touchstart", start, false);
canvas.addEventListener("touchmove", draw, false);
canvas.addEventListener("mousedown", start, false);
canvas.addEventListener("mousemove", draw, false);

canvas.addEventListener("touchend", stop, false);
canvas.addEventListener("mouseend", stop, false);
canvas.addEventListener("mouseup", stop, false);


function start(event){
  is_drawing = true;
  context.beginPath();
  context.moveTo(event.clientX - canvas.offsetLeft, event.clientY - canvas.offsetTop);
  event.preventDefault();
}


function draw(event){

  if(is_drawing){
    mouse_posX.push(event.clientX - canvas.offsetLeft);
    mouse_posY.push(event.clientY - canvas.offsetTop);
    context.lineTo(event.clientX - canvas.offsetLeft, event.clientY - canvas.offsetTop);
    context.strokeStyle = draw_color;
    context.lineWidth = draw_width;
    context.lineCap = "round";
    context.lineJoin = "round";
    context.stroke();
  }
  event.preventDefault();
}

function stop(event){
  if(is_drawing){
    context.stroke();
    is_drawing = false;
  }
  event.preventDefault();
  if (event.type != 'mouseend'){
      var img = image_create();
      var data = img;
      $.ajax({
        url:'/canvas',
        type:"POST",
        dataType:"JSON",
        contentType:"application/json",
        data:data,
        success:function(x){
          $(answer).replaceWith(x)
          $(prediction).replaceWith(x)
        },
      });
  }
}

function clear_canvas(){
  context.fillStyle = "white";
  context.clearRect(0, 0, canvas.width, canvas.height);
  context.fillRect(0, 0, canvas.width, canvas.height);
  $.ajax({
    url:'/canvas',
    type:'POST',
    dataType: 'JSON',
    contentType: 'application/json',
    data: JSON.stringify({'data':'True'}),
  })
}

function image_create() {
  var mouseX_min = Math.min.apply(Math, mouse_posX);
  var mouseX_max = Math.max.apply(Math, mouse_posX);
  var mouseY_min = Math.min.apply(Math, mouse_posY);
  var mouseY_max = Math.max.apply(Math, mouse_posY);
  var w = (mouseX_max - mouseX_min);
  var h = (mouseY_max - mouseY_min);
  var bx = Math.max(w,h)
  var newCanvas = document.createElement('canvas');
  newCanvas.width = bx;
  newCanvas.height = bx;
  var newContext = newCanvas.getContext('2d');
  newContext.drawImage(canvas, mouseX_min - 10, mouseY_min - 10, w + 20, h + 20, 0, 0, bx, bx);
  var img_last = newCanvas.toDataURL();
  mouse_posX = [];
  mouse_posY = [];
  return img_last;
}
