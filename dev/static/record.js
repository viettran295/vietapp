let mic, recorder, soundFile;
let state = 0;

function setup() {
  let cnv = createCanvas(250, 30);
  cnv.position(30, 210, 'absolute');
  background(150);
  fill(0);
  text('Enable microphone and click here to record', 10, 20);

  mic = new p5.AudioIn();
  mic.start();

  recorder = new p5.SoundRecorder();
  recorder.setInput(mic);
  soundFile = new p5.SoundFile();
}

function mousePressed() {
  if (state === 0 && mic.enabled) {
    // Tell recorder to record to a p5.SoundFile which we will use for playback
    recorder.record(soundFile);
    background(255, 0, 0);
    text('Recording now... click here to stop.', 20, 20);
    state++;

  } else if (state === 1) {
    recorder.stop(); // stop recorder, and send the result to soundFile
    background(0, 255, 0);
    text('Recording stopped!!!', 20, 20);
    
    let URL = "http://127.0.0.1:5000/upload";
    let soundBlob = soundFile.getBlob();
    let formData = new FormData();
    formData.append('audio_file', soundBlob, 'audio_file.wav');
    fetch(URL, {
            method: "POST",
            cache: "no-cache",
            body: formData
          }).then(resp => {
            if(resp.status !== 200) {
              console.error("Error:", resp)
            }
          })
    state = 0;
  }
}