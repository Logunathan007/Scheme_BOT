const bot_icon = document.querySelector(".bot_icon")
const msg_box = document.querySelector(".msg_box")
const suggestionlist = document.querySelector(".suggestionlist");
const inputstr = document.querySelector(".inputstr");

var list = ["Java", "Python", "C", "SQL","c++"]
list.sort();

bot_icon.addEventListener("click",()=>{
    if(msg_box.classList.contains("on")){
        msg_box.classList.add("off")
        msg_box.classList.remove("on")
    }else{
        msg_box.classList.add("on")
        msg_box.classList.remove("off")
    }
});


inputstr.addEventListener("input",(eve)=>{
    var val = (eve.target.value);
    list = list.filter((ele)=>{
        return ((ele.toLowerCase()).indexOf(String(val).toLowerCase()) != -1)
    }
    )
    suggestionlist.innerHTML = "";
    list.forEach((ele)=>{
        suggestionlist.innerHTML+=`<div class="sug">${ele}</div>`
    })
})

list.forEach((ele)=>{
    suggestionlist.innerHTML+=`<div class="sug">${ele}</div>`
})



