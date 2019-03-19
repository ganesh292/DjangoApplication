var myVideo = document.getElementById("myVideo");
var slider = document.getElementById("myRange");
var output = document.getElementById("demo");
var playButton=document.getElementById("playBtn");
var selVideo = document.getElementsByClassName("selectingVideo");
var submitButton=document.getElementById("submitBtn");
var a=document.getElementById("scorelink");
var vidId = document.getElementById("videoid")
const param=new URLSearchParams(location.search);
console.log(objs);

var i=0;
var score=0;
var score_preference="Preferred Video Name"

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

var data_preference = {
  'csrfmiddlewaretoken': csrftoken,
  'score': score_preference
}


var files={};
//Selecting Videos
function readFiles(event) {
  files=document.getElementById("file").files;
  data['fileName']=files[i].name;
  data_preference['video1']=files[i].name;
  data_preference['video2']=files[i+1].name
  loadAsUrl(files[i]);
}



//Generating csrf token for POST operation

//Data to POST

//Function called after viewing all videos
//Single Score
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

//Preference Score
function updateScore_preference() {
  $.ajax({
    url: "/videoplay/temp/",
    type: "POST",
    //dataType: "json",
    data: data_preference,
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
  //data_preference['score'] = files[i].name;
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
updateScore_preference();
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
//Series of events after video ends for single score
// myVideo.addEventListener('ended', enableDisablebuttons,false);
// function enableDisablebuttons(e) {
//        slider.style.opacity=0.8;
//        slider.disabled=false;
//        slider.hidden=false;
//        myVideo.style.display = "none";
//        playButton.style.display="none";
//        selVideo[0].style.display="none";
//        submitButton.hidden=false;
//        i++;
//        document.getElementById("scoreDisp").hidden=false;
//        document.exitFullscreen();
// }

function dummy(){
  myVideo.play();
  
}
//Series of events after video ends for preference score
myVideo.addEventListener('ended', enableDisablebuttons, false);
function enableDisablebuttons(e) {
  i++;
  if(i!=files.length){
    loadAsUrl(files[i])
    myVideo.autoplay=true;
    window.setTimeout(dummy,5000)
    
  }
  else{
       slider.style.opacity=0.8;
       slider.disabled=false;
       slider.hidden=false;
       myVideo.style.display = "none";
       playButton.style.display="none";
       selVideo[0].style.display="none";
       submitButton.hidden=false;
       document.getElementById("scoreDisp").hidden=false;
       document.exitFullscreen();
  }
}

function sendScore(){
  updateScore_preference();
  window.location.href = "/videoplay/temp/"
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
// if(i==files.length){
//     window.location.href="/videoplay/temp/"
//   }

    // if(i>0){
    //   //data['score'] = JSON.stringify(data['score'])
    //   //data_preference['video1'] = files[i-1].name;
    //   //data_preference['video2'] = files[i].name;
    //   //updateScore_preference();
    //   submitButton.hidden = true;
    //   slider.hidden = true;
    //   slider.style.opacity = 0.2;
    //   slider.disabled = true;
    //   myVideo.autoplay=true;
    // }

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
   