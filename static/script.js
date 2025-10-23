const video = document.createElement('video');
video.autoplay = true;

navigator.mediaDevices.getUserMedia({ video: true })
  .then(stream => {
    video.srcObject = stream;
    document.body.appendChild(video);
  })
  .catch(err => {
    console.error("Error accessing webcam: ", err);
  });