var myVideo = document.getElementById("myVideo");
var slider = document.getElementById("myRange");
var output = document.getElementById("demo");
var playButton=document.getElementById("playBtn");
var selVideo = document.getElementsByClassName("selectingVideo");
var submitButton=document.getElementById("submitBtn");
var a=document.getElementById("scorelink");
//location.search;
//var userscore=document.getElementById("userscore");
// var videoid=document.getElementById("videoid");
//const url = new URL("http://127.0.0.1:8000/videoplay/videos/?score=");
//console.log(url.has('score'));
const param=new URLSearchParams(location.search)
// console.log(param.get('score'));
// param.set('score','10')
// console.log(param.get('score'));
var fileList;
var i=0;
var score=0;
function readFiles(event) {
    fileList = event.target.files;
    loadAsUrl(fileList[i]);
    console.log(fileList[0]);
}


slider.oninput = function() {
  output.innerHTML = this.value;
  score=this.value;
  // userscore.value=score;
}


function nextVid(){
  if(i==3){
    i=0;
  }
  //i++;
  //loadAsUrl(fileList[i]);
  slider.value=50;
  output.innerHTML=50;
  disableScroll();
  //setting url pattern
  a.setAttribute('href', "?score="+score+"&videoID="+fileList[i].name);
  // let url = new URL("http://127.0.0.1:8000/videoplay/videos/?");
  // let params = new URLSearchParams(url.search.slice(1));

  // //Add a second foo parameter.
  // params.append('foo', 4);
}

function disableScroll(){
  slider.style.opacity=0.2;
  slider.disabled=true;
}

myVideo.addEventListener('ended', enableDisablebuttons,false);
function enableDisablebuttons(e) {
       slider.style.opacity=0.8;
       slider.disabled=false;
       slider.hidden=false;
       myVideo.style.display = "none";
       playButton.style.display="none";
       selVideo[0].style.display="none";
       submitButton.hidden=false;
      //  videoid.value=myVideo.src;
       document.getElementById("scoreDisp").hidden=false;
       document.exitFullscreen();
}

function loadAsUrl(theFile) {
    var reader = new FileReader();

    reader.onload = function(loadedEvent) {
        myVideo.setAttribute("src", loadedEvent.target.result);
    }

    reader.readAsDataURL(theFile);
}

function playVid(){
    //vid.requestFullscreen();
    myVideo.play();
    //i++;

  }

function toggleFullscreen() {

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

  // if (!document.fullscreenElement) {
  //   myVideo.requestFullscreen().then({}).catch(err => {
  //     alert(`Error attempting to enable full-screen mode: ${err.message} (${err.name})`);
  //   });
  //   myVideo.msRequestFullScreen().then({}).catch(err => {
  //     alert(`Error attempting to enable full-screen mode: ${err.message} (${err.name})`);
  //   });
  //   myVideo.webkitRequestFullScreen().then({}).catch(err => {
  //     alert(`Error attempting to enable full-screen mode: ${err.message} (${err.name})`);
  //   });
  //   myVideo.mozRequestFullscreen().then({}).catch(err => {
  //     alert(`Error attempting to enable full-screen mode: ${err.message} (${err.name})`);
  //   });
   else {
    document.exitFullscreen();
  }
  //if (i > 0) { nextVid();}  
  
    playVid();
    myVideo.style.display="block";
}


function pauseVid() {
myVideo.pause();
}

console.log("Hello! Static Cnnected");



   