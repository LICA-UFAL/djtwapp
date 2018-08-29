const btn = document.querySelector("#btn");
const btn1 = document.querySelector("#btn1");
const cform = document.querySelector("#cform")
const cb = document.querySelector("#cb")

btn.addEventListener('click', (event) => {
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

    btn.setAttribute("hidden","");
    cform.removeAttribute("hidden");
    
});

btn1.addEventListener("click", (event) => {
    btn1.setAttribute("hidden","")
    btn2.setAttribute("hidden","")
    cb.removeAttribute("hidden")
});
