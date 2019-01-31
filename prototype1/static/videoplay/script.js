var vid = document.getElementById("myVideo");

function playVid() {

  vid.requestFullscreen()
  vid.play();

}

function pauseVid() {
vid.pause();

}



// var slider = document.getElementById("myRange");
// var output = document.getElementById("demo");
// var score=0;
// // var vid = document.getElementById("myVideo");
// vid.addEventListener('ended',myHandler,false);
//  function myHandler(e) {
//      slider.style.opacity=0.8
//      slider.disabled=false;
//  }
//
// output.innerHTML = slider.value;
// slider.oninput = function() {
//   output.innerHTML = this.value;
//   score=this.value;
// }
//
//
//
// function readFiles(event) {
//   var fileList = event.target.files;
//   loadAsUrl(fileList[0]);
// }
//
// function loadAsUrl(theFile) {
//   var reader = new FileReader();
//
//   reader.onload = function(loadedEvent) {
//       vid.setAttribute("src", loadedEvent.target.result);
//       reader.readAsDataURL(theFile);
// }



// vid.addEventListener('ended',myHandler,false);
// // function myHandler(e) {
// //   files = os.listdir(os.path.join(settings.STATIC_ROOT, "video/"))
// //   console.log(files);
// //   var i;
// //   for (i = 1; i < files.length; i++) {
// //     vid.src = files[i];
// //     vid.play();
// //   }
// function myHandler(e) {
//     console.log('video ended')
// }
