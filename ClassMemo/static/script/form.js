let title = document.querySelector(".writeTitle");
let context = document.querySelector(".writeInput");
let dateC = document.querySelector(".dateC")

function check() {
    if (title.value && context.value ){
        button.disabled = false;
    } else {
        button.disabled = true;
    }
}