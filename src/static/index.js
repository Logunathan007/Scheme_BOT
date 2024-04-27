const bot_icon = document.querySelector(".bot_icon")
const msg_box = document.querySelector(".msg_box")

bot_icon.addEventListener("click",()=>{
    if(msg_box.classList.contains("on")){
        msg_box.classList.add("off")
        msg_box.classList.remove("on")
    }else{
        msg_box.classList.add("on")
        msg_box.classList.remove("off")
    }
});
