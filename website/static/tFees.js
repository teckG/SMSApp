function feeCal() {
    var x = parseInt(document.getElementById('admfees').value);
    var y = parseInt(document.getElementById('fees').value);
    var res = x + y;
    document.getElementById("Tfees").value = res;
}