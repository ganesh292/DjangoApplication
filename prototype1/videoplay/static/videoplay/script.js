var myVideo = document.getElementById("myVideo");
var slider = document.getElementById("myRange");
var output = document.getElementById("demo");
var fileList;
var i=0;
function readFiles(event) {
    fileList = event.target.files;
    loadAsUrl(fileList[i]);
    console.log(fileList[i]);
}

slider.oninput = function() {
  output.innerHTML = this.value;
  //score=this.value;
}


function nextVid(){
    console.log('next video');
  if(i==3){
    i=0;
  }
  loadAsUrl(fileList[i]);
  slider.value=50;
  output.innerHTML=50;
  disableScroll();

}

function disableScroll(){
  slider.style.opacity=0.2;
  slider.disabled=true;
}

myVideo.addEventListener('ended',enableScroll,false);
function enableScroll(e) {
       slider.style.opacity=0.8;
       slider.disabled=false;
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
    console.log('play');
    myVideo.play();
    i++;

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
    playVid();
}


function pauseVid() {
myVideo.pause();
}

console.log("Hello! Static Cnnected");


   