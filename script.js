var s1Button = document.getElementById("s1");
var s2Button = document.getElementById("s2");

s1Button.addEventListener("click", stateChange1);
s2Button.addEventListener("click", stateChange2);

function stateChange1() {
    document.body.style.backgroundColor = "rgb(0, 0, 0)";
}

function stateChange2() {
    document.body.style.color = "rgb(0, 0, 0)";
}
