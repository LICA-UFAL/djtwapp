const btn_vote = document.querySelector("#vote");  
const btn_bot = document.querySelector("#bot");
const btn_not_bot = document.querySelector("#not_bot");
const cform = document.querySelector("#cform")
const check_box_div = document.querySelector("#check_box_div")

btn_vote.addEventListener('click', (event) => {
    /*btn.remove();
    let btn1 = document.createElement('button');
    let btn2 = document.createElement('button');
    let card = document.querySelector('.card-body.bg-dark')

    btn1.innerText = 'É bot';
    btn2.innerText = 'Não é bot';
    btn1.className = "btn btn-primary"
    btn2.className = "btn btn-primary"
    

    btn1.style.color = 'red';
    card.appendChild(btn1);
    card.appendChild(btn2);*/

    btn_vote.setAttribute("hidden","");
    cform.removeAttribute("hidden");
    
});

btn_bot.addEventListener("click", (event) => {
    btn_bot.setAttribute("hidden","")
    btn_not_bot.setAttribute("hidden","")
    
    check_box_div.removeAttribute("hidden")
});


function validate_cform(){
    const choices = document.getElementsByName("reasons");
    var cont_choices = 0
    for(var i=0; i< choices.length; i++){
        if(choices[i].checked){
            cont_choices+=1;
        }
    }
    
    if(cont_choices == 0){
        const label_error = document.querySelector("#bot_choices_error")
        label_error.removeAttribute("hidden")
        return false
    }
}