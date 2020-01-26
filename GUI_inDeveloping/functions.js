function square(number) {
    console.log(number*number);
}

function updateDOM(question, option1, option2, option3, point1, point2, point3) {
    document.getElementById("question").innerHTML(question);
    document.getElementById("op1").innerHTML(option1);
    document.getElementById("op2").innerHTML(option2);
    document.getElementById("op3").innerHTML(option3);
    document.getElementById("op1").setAttribute("", point1);
    document.getElementById("op2").setAttribute("", point2);
    document.getElementById("op3").setAttribute("", point3);

}

function getPoint() {


}