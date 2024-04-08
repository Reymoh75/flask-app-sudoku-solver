let $ = document
let inputs = $.querySelectorAll("input");
let resetBtn = $.querySelector("button[data-role='reset']");
let targetInput,i,j,nextTarget;

inputs.forEach(input => {
    input.addEventListener("keyup",(event) => {
        targetInput = event.target;
        if ( !/^[1-9]{1}$/.test(targetInput.value) ) {
            targetInput.value = ""
        }
        i = Number(targetInput.name.split("-")[0])
        j = Number(targetInput.name.split("-")[1])
        if (event.code == "ArrowDown") {
            nextTarget = $.querySelector(`input[name="${i}-${j+1}"]`)
            if ( nextTarget ) {
                nextTarget.select()
            }
        } else if (event.code == "ArrowUp") {
            nextTarget = $.querySelector(`input[name="${i}-${j-1}"]`)
            if ( nextTarget ) {
                nextTarget.select()
            }
        }  else if (event.code == "ArrowRight") {
            nextTarget = $.querySelector(`input[name="${i+1}-${j}"]`)
            if ( nextTarget ) {
                nextTarget.select()
            }
        }  else if (event.code == "ArrowLeft") {
            nextTarget = $.querySelector(`input[name="${i-1}-${j}"]`)
            if ( nextTarget ) {
                nextTarget.select()
            }
        }
    })
});

resetBtn.addEventListener("click",() => {
    inputs.forEach(input => {
        input.value = ""
    })
});