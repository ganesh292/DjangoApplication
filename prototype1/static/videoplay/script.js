
  
        var vid = document.getElementById("myVideo");

        function playVid() {

          vid.requestFullscreen()
          vid.play();
         
        }

        function pauseVid() {
        vid.pause();
        
        }

        

        vid.addEventListener('ended',myHandler,false);
        function myHandler(e) {
          files = os.listdir(os.path.join(settings.STATIC_ROOT, "videos/"))
          var i;
          for (i = 1; i < files.length; i++) { 
            vid.src = files[i];
            vid.play();
          }

          
        }
