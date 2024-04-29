const bot_icon = document.querySelector(".bot_icon")
const msg_box = document.querySelector(".msg_box")
const suggestionlist = document.querySelector(".suggestionlist");
const inputstr = document.querySelector(".inputstr");
const msg = document.querySelector(".msg");

let suggestion_list = ["Java", "Python", "C", "SQL","c++"]
suggestion_list.sort();

let msg_history = [
    {
        type : "bot",
        msg :"Hi What is your name?"
    },
    {
        type : "user",
        msg :"My name is Logunathan"
    }
]

let question_obj = {
    question_id : "qno1",
    question : "What is your name",
    suggestion : ["Ram","Sam","Gopal"],
    key : "name",
    value : "",
    category:"general",
    placeholder:"Enter your name ..."
}

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
    list = suggestion_list.filter((ele)=>{
        return ((ele.toLowerCase()).includes(String(val).toLowerCase()))
    }
    )
    display_suggestion(list);
    if(val == ""){
        suggestionlist.innerHTML = ""
        suggestion_list.forEach((ele)=>{
            suggestionlist.innerHTML+=`<div class="sug">${ele}</div>`
        })
    }
    selector()
})


function display_suggestion(suggestion_list){
    suggestionlist.innerHTML = ""
    if(suggestion_list.length == 0){
        suggestionlist.style.visibility =  "hidden";
    }else{
        suggestionlist.style.visibility =  "visible";
    }
    suggestion_list.forEach((ele)=>{
        suggestionlist.innerHTML+=`<div class="sug">${ele}</div>`
    })
    selector();
}

display_suggestion(suggestion_list)

function selector(){
    const select_sug = document.querySelectorAll(".sug");

    select_sug.forEach(ele=>{
        ele.addEventListener("click",(eve)=>{
            inputstr.value = (ele.innerText);
        })
    })
}
function display_msg(){
    msg.innerHTML = "";
    msg_history.forEach((ele)=>{
        if(ele.type == "bot"){
            msg.innerHTML += `<div class="botmsg">${ele.msg}</div>`
        }else{
            msg.innerHTML += `<div class="usermsg">${ele.msg}</div>`    
        }
    })
}
display_msg();

function savemsg(eve){
    if(inputstr.value == ""){
        return;
    }
    var obj = {
        type : "user",
        msg : `${inputstr.value}`
    }
    msg_history.push(obj);
    inputstr.value = "";
    display_msg();
    display_suggestion(suggestion_list);
}

function extract_question(){
    msg_history.push({
        type : "bot",
        msg : question_obj.question
    })
    display_msg();
    suggestion_list = question_obj.suggestion
    display_suggestion(suggestion_list)
    
}



