const popup = document.querySelector('.chat-popup');
const chatBtn = document.querySelector('.chat-btn');  

chatBtn.addEventListener('click',()=>{
    popup.classList.toggle('show');
})