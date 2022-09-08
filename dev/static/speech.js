const speech = document.querySelector('.speech')

window.SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = new SpeechRecognition();

function getMedia() {
  recognition.interimResult = true;
//   recognition.lang = 'de-DE';
//   const URL = '/speech_translator';
  let p = document.createElement('p');

  recognition.start();
  recognition.addEventListener('result', (e) => {
    const text = Array.from(e.results)
      .map(result => result[0])
      .map(result => result.transcript).join('');
    console.log(text);
    p.innerHTML = text;
    speech.appendChild(p);
  });
  recognition.addEventListener('end', () => {
    recognition.start();
  })
};