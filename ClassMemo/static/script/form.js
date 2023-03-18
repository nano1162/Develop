let title = document.querySelector(".writeTitle");
let context = document.querySelector(".writeInput");
let button = document.querySelector(".writeBtn")

function check() {
    if (title.value && context.value ){
        button.disabled = false;
    } else {
        button.disabled = true;
    }
}