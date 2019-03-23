var doublescorepage=document.getElementById("main")
var myVideo_d = document.getElementById("myVideo_d");
var playButton_d = document.getElementById("playBtn");
var selVideo_d = document.getElementsByClassName("selectingVideo");
// var submitButton = document.getElementById("submitBtn");
var a_d = document.getElementById("scorelink");
var vidId_d = document.getElementById("videoid")
var start = 0;
var vid_pair_num = 0;
var name_list = [['1_fps25.mp4', '3_fps24.mp4'], ['2_fps24.mp4', '4_fps25.mp4']]
console.log(name_list.length)
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      console.log(cookie)
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
}

var radiob1 = document.getElementsByName("optradio1");
// for (var i = 0, length = radiob1.length; i < length; i++) {
//   console.log(radiob1[i]);
// }
// function preference() {
//   // var b1 = document.getElementById('radio1');
//   // var b2 = document.getElementById('radio2');
//   console.log("Inside func peference");

//   //console.log("length is ",radiob1.length);
//   if (document.getElementById('radio1').checked) {
//     //Male radio button is checked
//     console.log(radiob1[0].value);
//   } else if (document.getElementById('radio2').checked) {
//     //Female radio button is checked
//     console.log(radiob1[1].value);
//   }
// }


var files_d = {};
//Selecting Videos
function readFiles_d(event) {
  console.log("Inside ReadFile Function")
  files_d = document.getElementById("file").files;
  data['fileName'] = files_d[i].name;
  console.log(files_d.length)

}

//Generating csrf token for POST operation
//Data to POST
//Function called after viewing all videos
function updateScore() {
  $.ajax({
    url: "/videoplay/videos2/",
    type: "POST",
    //dataType: "json",
    data: data,
    success: function (json) {
      toggleFullscreen_d();
    },
    error: function (xhr, errmsg, err) {
      alert("Could not send URL to Django. Error: " + xhr.status + ": " + xhr.responseText);
    }
  });
}
var vid_num = 1;
//Series of events after video ends
myVideo_d.addEventListener('ended', videoloop, false);
/////////////////////////////////////////////////////////
function enableDisablebuttons_d() {
  doublescorepage.hidden=false;
  myVideo_d.style.display = "none";
  playButton_d.style.display = "none";
  selVideo_d[0].style.display = "none";
  // submitButton.hidden = true;
  //i++;
  document.exitFullscreen();
}
//Loading the video files
function loadAsUrl_d(theFile) {
  var reader_d = new FileReader();
  reader_d.onload = function (loadedEvent) {
    myVideo_d.setAttribute("src", loadedEvent.target.result);

  }
  reader_d.readAsDataURL(theFile);
}

function toggleFullscreen_d() {
  console.log("Toggle Screen");
  doublescorepage.hidden=true;
  if (myVideo_d.paused) {
    console.log("Video is Paused")
    if (myVideo_d.requestFullscreen) {
      myVideo_d.requestFullscreen();
    }
    else if (myVideo_d.mozRequestFullScreen) {
      myVideo_d.mozRequestFullScreen();
    }
    else if (myVideo_d.webkitRequestFullScreen) {
      myVideo_d.webkitRequestFullScreen();
    }
    else if (myVideo_d.msRequestFullscreen) {
      myVideo_d.msRequestFullscreen();
    }
    doublestimulus(name_list);
  }
  else {
    console.log("Video is not Pause")
    document.exitFullscreen();
  }
  myVideo_d.style.display = "block";
  console.log(i);

}
//Pause Video
function pauseVid() {
  myVideo_d.pause();
}
///////////////////////////////////////////////////
function getuploadedpath(vid_name) {
  for (var i = 0; i < files_d.length; i++) {
    if (files_d[i].name == vid_name) {
      return files_d[i];
    }
  }
}
///////////////////////////////////////////////////////
function playVid2() {
  console.log("Inside playVid2")

  myVideo_d.autoplay = true;
  myVideo_d.style.display = "block";
  playButton_d.style.display = "none";
  const playPromise = myVideo_d.play();
  if (playPromise !== null) {
    playPromise.catch(() => { myVideo_d.play(); })
  }
  console.log("finished playing video")
  return;
}
var pair_end = 0;
function delay()
{
  k=0
  
  while(k<350)
  {
    console.log(k)
    j=0
    while(j<1000000)
    {
      j++
    }
    k++
  }
}

function doublestimulus(name_list) {
  console.log("Inside Double Stimulus function")
  // debugger;
  if (vid_pair_num < name_list.length) {
    if (vid_num == 1) {
      console.log("Gonna Play Vid1")
      console.log(name_list[vid_pair_num][0])
      path1 = getuploadedpath(name_list[vid_pair_num][0])
      console.log('path1\n', path1)
      loadAsUrl_d(path1)
      playVid2();
      vid_num = 2
    }
    else {
      console.log("Gonna Play Vid2")
      console.log(name_list[vid_pair_num][1])
      path2 = getuploadedpath(name_list[vid_pair_num][1])
      console.log('path2\n', path2)
      loadAsUrl_d(path2)

      console.log('gonna sleep for 3 sec')
      delay()
      playVid2();
      // const playPromise = myVideo_d.play();
      // if (playPromise !== null) {
      //   playPromise.catch(() => { myVideo_d.play(); })
      // }

      vid_num = 1
      vid_pair_num += 1;
      pair_end = 1;

    }

  }
  else {
    window.location.href = "/videoplay/temp/"
  }

  return;
}
function videoloop(e) {
  console.log("Inside Videoloop")
  // doublestimulus(name_list);
  if (pair_end == 1) {
    document.exitFullscreen();
    enableDisablebuttons_d();
    pair_end = 0;
  }
  else {
    doublestimulus(name_list);
  }
}


function nextpair() {
  //enableDisablebuttons_d()
  //myVideo_d.style.display="none"
  if (document.getElementById('radio1').checked) {
    //Male radio button is checked
    data['preference']=radiob1[0].value;
  } else if (document.getElementById('radio2').checked) {
    //Female radio button is checked
    data['preference'] = radiob1[1].value;
  }
  
  //var preference = prompt("Enter 1 if first video was better else enter 2!");
  data['preference'] = JSON.stringify(data['preference'])
  data['vid_name1'] = name_list[vid_pair_num - 1][0]
  data['vid_name2'] = name_list[vid_pair_num - 1][1]
  updateScore();
}
//Just to make sure static files are connected, see this message in console
console.log("Hello! Static Cnnected");
   