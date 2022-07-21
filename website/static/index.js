function deleteNote(noteId) {
    fetch("/delete-note", {
        method: "POST",
        body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
        window.location.href = "/";
    });
}


function half(value) {
    // body...
    x = 0.5 * value;
    document.getElementById("clswkeng50").value = x;
}



function add() {
    var x = parseInt(document.getElementById('var_x').value);
    var y = parseInt(document.getElementById('var_y').value);
    var res = x + y;
    document.getElementById("display2").value = res;
}