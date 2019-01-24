

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
            console.log('video ended')
        }
