const popup = document.querySelector('.chat-popup');
const chatBtn = document.querySelector('.chat-btn');  

chatBtn.addEventListener('click',()=>{
    popup.classList.toggle('show');
})

function convertPDF_text(){
    var popup = document.getElementById("PDFtoText");
    popup.classList.toggle('showpopup')
}

