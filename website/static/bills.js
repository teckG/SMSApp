function toggleText() {
    var x = document.getElementById("names");
    if (x.style.display === "none") {
        x.style.display = "block";

    } else {
        x.style.display = "none";
    }
}

function setName() {
    var x = document.getElementById('names').innerText;
    document.getElementById("stname").value = x;
}

function hid() {
    var x = document.getElementById("names").hide();;


}