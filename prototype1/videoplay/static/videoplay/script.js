var myVideo = document.getElementById("myVideo");
var slider = document.getElementById("myRange");
var output = document.getElementById("demo");
var playButton=document.getElementById("playBtn");
var selVideo = document.getElementsByClassName("selectingVideo");
var submitButton=document.getElementById("submitBtn");
var a=document.getElementById("scorelink");
var vidId = document.getElementById("videoid");

const param=new URLSearchParams(location.search);
var i=0;
var score=0;

var objs = ["video1","video2"];
for(var i =0;i<objs.length;i++)
{
    console.log("hi");
    var f =  objs[i];
   console.log(f);
}

//document.getElementById('radio1').value = f;
var radiob1 = document.getElementsByName("optradio1");
for (var i = 0, length = radiob1.length; i < length; i++)
{
console.log(radiob1[i]);
}
function preference()
{
// var b1 = document.getElementById('radio1');
// var b2 = document.getElementById('radio2');
console.log("Inside func peference");

//console.log("length is ",radiob1.length);
if(document.getElementById('radio1').checked) {
  //Male radio button is checked
  console.log(radiob1[0].value);
}else if(document.getElementById('radio2').checked) {
  //Female radio button is checked
  console.log(radiob1[1].value);
}

// for (var i = 0, length = radiob1.length; i < length; i++)
// {
// console.log(radiob1[i]);
// if (radiob1[i].checked)
// {
// // do whatever you want with the checked radio
// console.log("yes");
// console.log(radiob1[i].value);
// break;

// // only one radio can be logically checked, don't check the rest

// }
// }

}
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
var csrftoken = getCookie('csrftoken');

var data = {
  'csrfmiddlewaretoken': csrftoken,
  'score': score
}
var files={};
//Selecting Videos
function readFiles(event) {
  files=document.getElementById("file").files;
  data['fileName']=files[i].name;
  loadAsUrl(files[i]);
}

// localStorage.setItem('storeObj', JSON.stringify(myObj));
// console.log(JSON.parse(localStorage.getItem('storeObj')));

//Generating csrf token for POST operation

//Data to POST

//Function called after viewing all videos
function updateScore(){
  $.ajax({
      url: "/videoplay/videos/",
      type: "POST",
      //dataType: "json",
      data: data,
      success: function (json) {
        //console.log(files[i].name);
        loadAsUrl(files[i]);
      },
      error: function (xhr, errmsg, err) {
        alert("Could not send URL to Django. Error: " + xhr.status + ": " + xhr.responseText);
      }
    });
}


//Score slider
slider.oninput = function() {
  output.innerHTML = this.value;
  score=this.value;
  data['score']=score;
}
//To go to next video:'Submit Score' button
function nextVid(){
  //i++;
  console.log(files[i]);
  console.log(i);
  
if (i == 3) {
  i=0;
  console.log(score);
  // updateScore();
}
data['score'] = JSON.stringify(data['score'])
updateScore();
// loadAsUrl(files[i]);
slider.value = 50;
output.innerHTML = 50;
disableScroll();
}

// document.addEventListener('fullscreenchange', exitHandler);
// document.addEventListener('webkitfullscreenchange', exitHandler);
// document.addEventListener('mozfullscreenchange', exitHandler);
// document.addEventListener('MSFullscreenChange', exitHandler);

// function exitHandler() {
//   if (!document.fullscreenElement && !document.webkitIsFullScreen && !document.mozFullScreen && !document.msFullscreenElement) {
//     ///fire your event
//    alert("hey");
    
//   }
// }






function disableScroll(){
  submitButton.hidden = true;
  slider.hidden = true;
  slider.style.opacity=0.2;
  slider.disabled=true;
}
//Series of events after video ends
myVideo.addEventListener('ended', enableDisablebuttons,false);
function enableDisablebuttons(e) {
       slider.style.opacity=0.8;
       slider.disabled=false;
       slider.hidden=false;
       myVideo.style.display = "none";
       playButton.style.display="none";
       selVideo[0].style.display="none";
       submitButton.hidden=false;
       i++;
       document.getElementById("scoreDisp").hidden=false;
       document.exitFullscreen();
}
//Loading the video files
function loadAsUrl(theFile) {
    var reader = new FileReader();
    reader.onload = function(loadedEvent) {
      myVideo.setAttribute("src", loadedEvent.target.result);
        
    }
    reader.readAsDataURL(theFile);
}
//Play the videos
function playVid(){
    if(i>0){
      data['score'] = JSON.stringify(data['score'])
      data['fileName'] = files[i-1].name;
      updateScore();
      submitButton.hidden = true;
      slider.hidden = true;
      slider.style.opacity = 0.2;
      slider.disabled = true;
      myVideo.autoplay=true;
    }

  if(i==files.length){
    window.location.href="/videoplay/temp/"
  }
    myVideo.style.display = "block";
    playButton.style.display = "none";
    myVideo.play();
    console.log(i);
    
  }

// //Change to full screen
function toggleFullscreen() {
  console.log("Toggle Screen");

  if(myVideo.paused)
  {
  if (myVideo.requestFullscreen) {
      myVideo.requestFullscreen();
  }
  else if (myVideo.mozRequestFullScreen) {
      myVideo.mozRequestFullScreen();
  }
  else if (myVideo.webkitRequestFullScreen) {
      myVideo.webkitRequestFullScreen();
  }
  else if (myVideo.msRequestFullscreen) {
      myVideo.msRequestFullscreen();
  }
  playVid();
}
   else {
    document.exitFullscreen();
  }
    myVideo.style.display="block";
    console.log(i);
    
}
//Pause Video
function pauseVid() {
myVideo.pause();
}
//Just to make sure static files are connected, see this message in console
console.log("Hello! Static Cnnected");
   