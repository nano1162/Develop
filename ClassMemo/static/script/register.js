let id = document.querySelector("#id");
let password = document.querySelector("#password");
let rePassword = document.querySelector("#re-password");
let button = document.querySelector("form button")

function check() {
    if (id.value && password.value && rePassword.value) {
        if (password.value == rePassword.value) {
            button.disabled = false;
        }
        else {
            button.disabled = true;
        }
    }
    else {
        button.disabled = true;
    }
}