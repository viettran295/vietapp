const popup = document.querySelector('.chat-popup');
const chatBtn = document.querySelector('.chat-btn');  

chatBtn.addEventListener('click',()=>{
    popup.classList.toggle('show');
})

function convertPDF_text(){
    var popup = document.getElementById("PDFtoText");
    popup.classList.toggle('showpopup')
}

async function getMedia() {
  window.SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  const recognition = new SpeechRecognition();
  recognition.interimResult = true;
  recognition.lang = 'de-DE';
  const URL = 'http://127.0.0.1:5000/speech_translator';

  recognition.addEventListener('result', (e) => {
    const text = Array.from(e.results)
      .map(result => result[0])
      .map(result => result.transcript).join('');
    console.log(text);
  
    $.post(URL, {
      data: text,
    });

  //   let formData = new FormData();
  //   formData.append('speech', text);
  //   fetch(URL, {
  //     method: 'POST',
  //     cache: 'no-cache',
  //     body: formData,
  //   }).then(resp => {
  //     if(resp.status !== 200){
  //       console.error("Error: ", resp);
  //     }
  //   }).catch(err => {
  //     console.error(err);
  //   });
  });

  recognition.start();
};

