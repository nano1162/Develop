
function inc() {
    let mainNum = document.querySelector('#mainNumber').textContent;
    let intMainNum = parseInt(mainNum);
    intMainNum = intMainNum + 1;
    document.querySelector('#mainNumber').textContent = intMainNum;
    if (intMainNum >= 1) {
        document.querySelector('#mainNumber').style.color = "green";
    }
    else if (intMainNum == 0){
        document.querySelector('#mainNumber').style.color = "gray";
    }
}

function dec() {
    let mainNum = document.querySelector('#mainNumber').textContent;
    let intMainNum = parseInt(mainNum);
    intMainNum = intMainNum - 1;
    document.querySelector('#mainNumber').textContent = intMainNum;
    if (intMainNum <= -1) {
        document.querySelector('#mainNumber').style.color = "red";
    }
    else if (intMainNum == 0){
        document.querySelector('#mainNumber').style.color = "gray";
    }
}

function res() {
    document.querySelector('#mainNumber').textContent = 0;
    document.querySelector('#mainNumber').style.color = "gray";
}