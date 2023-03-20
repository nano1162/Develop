let selectTam = document.getElementById("selectTam");
let selectSub = document.getElementById("selectSub");


function ChangeValue() {
let tamValue = selectTam.options[selectTam.selectedIndex].value;
if (tamValue == "진로") {

    let didiv = document.getElementById("didiv");
    let dateC = document.querySelector(".dateC");
    let dateCYes = document.getElementById("date_c_yes");
    selectSub.replaceChildren();
    let element0 = document.createElement('option');
    let element1 = document.createElement('option');
    let element2 = document.createElement('option');
    let element3 = document.createElement('option');

    element0.textContent = "과목 선택"
    selectSub.appendChild(element0);

    element1.value = "융합과학탐구";
    element1.textContent = "융합과학탐구";
    selectSub.appendChild(element1);

    element2.value = "생활과 과학";
    element2.textContent = "생활과 과학";
    selectSub.appendChild(element2);

    element3.value = "과학사";
    element3.textContent = "과학사";
    selectSub.appendChild(element3);
    if (didiv.childElementCount == 4) {
        let a = document.createElement('input');
        a.type = "date";
        a.name = "date_b";
        a.className = "writeDate dateB";
        didiv.appendChild(a);
    }
    try{
        dateC.remove()
    } catch {
    }
    dateCYes.remove();
    
    let a = document.createElement('input');
    a.type = "text";
    a.name = "date_c_yes";
    a.id = "date_c_yes"
    a.value = "no"
    a.style.display = "none";
    didiv.appendChild(a);
}

else if (tamValue == "탐구") {
    let didiv = document.getElementById("didiv");
    selectSub.replaceChildren();
    let dateCYes = document.getElementById("date_c_yes");
    let dateC = document.querySelector(".dateC");
    let element0 = document.createElement('option');
    let element1 = document.createElement('option');
    let element2 = document.createElement('option');
    let element3 = document.createElement('option');
    let element4 = document.createElement('option');
    
    element0.textContent = "과목 선택"
    selectSub.appendChild(element0);

    element1.value = "물리학1";
    element1.textContent = "물리학1";
    selectSub.appendChild(element1);

    element2.value = "화학1";
    element2.textContent = "화학1";
    selectSub.appendChild(element2);

    element3.value = "생명과학1";
    element3.textContent = "생명과학1";
    selectSub.appendChild(element3);

    element4.value = "지구과학1";
    element4.textContent = "지구과학1";
    selectSub.appendChild(element4);

    if (didiv.childElementCount == 5) {
        let a = document.createElement('input');
        a.type = "date";
        a.name = "date_c";
        a.className = "writeDate dateC";
        didiv.appendChild(a);
    }
    else if (didiv.childElementCount == 4) {
        let a = document.createElement('input');
        let b = document.createElement('input');
        b.type = "date";
        b.name = "date_b";
        b.className = "writeDate dateB";
        didiv.appendChild(b);

        a.type = "date";
        a.name = "date_c";
        a.className = "writeDate dateC";
        didiv.appendChild(a);
    }
    dateCYes.remove();
    let a = document.createElement('input');
    a.type = "text";
    a.name = "date_c_yes";
    a.id = "date_c_yes"
    a.value = "yes"
    a.style.display = "none";
    didiv.appendChild(a);
}

else if (tamValue == "공통") {
    let didiv = document.getElementById("didiv");
    selectSub.replaceChildren();
    let dateCYes = document.getElementById("date_c_yes");
    let dateB = document.querySelector(".dateB");
    let dateC = document.querySelector(".dateC");
    let element0 = document.createElement('option');
    let element1 = document.createElement('option');
    let element2 = document.createElement('option');
    let element3 = document.createElement('option');
    let element4 = document.createElement('option');
    let element5 = document.createElement('option');
    let element6 = document.createElement('option');
    let element7 = document.createElement('option');
    
    element0.textContent = "과목 선택"
    selectSub.appendChild(element0);

    element1.value = "수학1";
    element1.textContent = "수학1";
    selectSub.appendChild(element1);

    element3.value = "확률과통계";
    element3.textContent = "확률과 통계";
    selectSub.appendChild(element3);

    element2.value = "문학";
    element2.textContent = "문학";
    selectSub.appendChild(element2);

    element4.value = "영어";
    element4.textContent = "영어";
    selectSub.appendChild(element4);

    element5.value = "미술";
    element5.textContent = "미술";
    selectSub.appendChild(element5);

    element6.value = "일본어";
    element6.textContent = "일본어";
    selectSub.appendChild(element6);

    element7.value = "중국어";
    element7.textContent = "중국어";
    selectSub.appendChild(element7);
    dateB.remove()
    try{
        dateC.remove()
    } catch {
    }
    dateCYes.remove();
    let a = document.createElement('input');
    a.type = "text";
    a.name = "date_c_yes";
    a.id = "date_c_yes"
    a.value = "one"
    a.style.display = "none";
    didiv.appendChild(a);
}
else {
    selectSub.replaceChildren();
    let element0 = document.createElement('option');
    element0.textContent = "과목 선택"
    selectSub.appendChild(element0);

}
}