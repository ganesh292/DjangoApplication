var myVideo = document.getElementById("myVideo");
var slider = document.getElementById("myRange");
var output = document.getElementById("demo");
var playButton=document.getElementById("playBtn");
var selVideo = document.getElementsByClassName("selectingVideo");
var submitButton=document.getElementById("submitBtn");
var a=document.getElementById("scorelink");
var vidId = document.getElementById("videoid")
const param=new URLSearchParams(location.search);
var i=0;
var score=0;
var files={};
//Selecting Videos
var videoafterparse;
function readFiles(event) {
<<<<<<< HEAD
  files=document.getElementById("file").files;
  console.log(files);
  loadAsUrl(files[i]);
=======
    fileList = event.target.files;
    loadAsUrl(fileList[i]);
    for(var j=0;j<3;j++){
    score[fileList[j].name]=0;
    }
    
>>>>>>> 25a311504a02a8c00e53c3f3647189abea214c19
}
  

//Generating csrf token for POST operation
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
//Data to POST
var data={
  'csrfmiddlewaretoken': csrftoken,
  'score':score
}
//Function called after viewing all videos
function updateScore(){
  $.ajax({
      url: "/videoplay/videos/",
      type: "POST",
      //dataType: "json",
      data: data,
      success: function (json) {
        console.log(files[i].name);
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
<<<<<<< HEAD
       i++;
=======
>>>>>>> 25a311504a02a8c00e53c3f3647189abea214c19
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
<<<<<<< HEAD
    if(i>0){
      data['score'] = JSON.stringify(data['score'])
      updateScore();
      submitButton.hidden = true;
      slider.hidden = true;
      slider.style.opacity = 0.2;
      slider.disabled = true;
      myVideo.autoplay=true;
    }
    if(i==3){
      i=0;
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
=======
    console.log("Inside play vid...this is supposed to be called again and again.....value of i is..."+i)
    myVideo.play();
  }
//Change to full screen
function toggleFullscreen() {
  console.log("Toggle Screen");
>>>>>>> 25a311504a02a8c00e53c3f3647189abea214c19
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
   