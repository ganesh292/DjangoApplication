var myVideo = document.getElementById("myVideo");
var slider = document.getElementById("myRange");
var output = document.getElementById("demo");
var playButton=document.getElementById("playBtn");
var selVideo = document.getElementsByClassName("selectingVideo");
var submitButton=document.getElementById("submitBtn");
var a=document.getElementById("scorelink");
//var URL="{% url 'videoplay-videos' %}"
var vidId = document.getElementById("videoid")
//location.search;
//var userscore=document.getElementById("userscore");
// var videoid=document.getElementById("videoid");
//const url = new URL("http://127.0.0.1:8000/videoplay/videos/?score=");
//console.log(url.has('score'));
const param=new URLSearchParams(location.search);
// console.log(param.get('score'));
// console.log(param.has('score'))
var fileList;
var i=0;
var score=0;
function readFiles(event) {
    fileList = event.target.files;
    loadAsUrl(fileList[i]);
    console.log(fileList[0]);
  //window.localStorage.setItem("someVarKey", fileList);
}
//console.log(window.localStorage.getItem("someVarKey"));


slider.oninput = function() {
  output.innerHTML = this.value;
  score=this.value;
  // userscore.value=score;
}

function nextVid(){
if (i == 3) {
  i = 0;
}
//loadAsUrl(fileList[i]);
//i++;
//loadAsUrl(fileList[i]);
slider.value = 50;
output.innerHTML = 50;
disableScroll();

//setting url pattern
a.setAttribute('href', "?score=" + score + "&videoID=" + fileList[i-1].name);
  // let url = new URL("http://127.0.0.1:8000/videoplay/videos/?");
  // let params = new URLSearchParams(url.search.slice(1));

  // //Add a second foo parameter.
  // params.append('foo', 4);
  //toggleFullscreen()
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
       document.getElementById("mssg").hidden=false;

       // i++;
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
    console.log("Inside play vid...this is supposed to be called again and again.....value of i is..."+i)
    //loadAsUrl(fileList[i]);
    myVideo.play();
    i++;

  }
//AJAX to send data-figure it out....
// $(document).ready(function () {
//   $("#submitBtn").click(function () {
//     $.ajax({
//       url: "/play/",
//       type: "POST",
//       dataType: "json",
//       data: {
//         'csrfmiddlewaretoken': "{{ csrf_token }}",
//         'score': score
//       },
//       success: function (json) {
//         alert("Successfully sent the URL to Django");
//       },
//       error: function (xhr, errmsg, err) {
//         alert("Could not send URL to Django. Error: " + xhr.status + ": " + xhr.responseText);
//       }
//     });
//   });
// });

//Trial



function toggleFullscreen() {
  console.log("Toggle Screen");

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
  // if (i > 0) {
  //   //console.log("calling nextvideo");
  //    loadAsUrl(fileList[i]);
  //   }  
    // loadAsUrl(fileList[i]);
    //prevVideo=fileList[i].name;
    //window.location.href("{%url 'videoplay-videos'%}"+'0')
  //window.history.pushState({},"","?score="+score);
    playVid();
    myVideo.style.display="block";
  //a.setAttribute('href', "?score=" + window.localStorage.getItem("someVarKey") + "&videoID=" + fileList[0].name);
    console.log(i);
    
}

function pauseVid() {
myVideo.pause();
}

console.log("Hello! Static Cnnected");


   