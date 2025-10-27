// const video = document.createElement('video');
// video.autoplay = true;

// navigator.mediaDevices.getUserMedia({ video: true })
//   .then(stream => {
//     video.srcObject = stream;
//     document.body.appendChild(video);
//   })
//   .catch(err => {
//     console.error("Error accessing webcam: ", err);
//   });

  const video = document.getElementById('webcam');
    const startBtn = document.getElementById('startBtn');
    const stopBtn = document.getElementById('stopBtn');
    let stream;

    startBtn.onclick = async () => {
      stream = await navigator.mediaDevices.getUserMedia({ video: true });
      video.srcObject = stream;
    };
    stopBtn.onclick = () => {
      if (stream) {
        stream.getTracks().forEach(track => track.stop());
      }
    };