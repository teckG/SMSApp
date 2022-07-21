function half(value) {
    x = 0.5 * value;
    document.getElementById("clswkeng50").value = x;
}

function half1(value) {
    x = 0.5 * value;
    document.getElementById("exameng50").value = x;
}


function add() {
    var x = parseInt(document.getElementById('clswkeng50').value);
    var y = parseInt(document.getElementById('exameng50').value);
    var res = x + y;
    document.getElementById("toteng").value = res;
    grade();
}



function grade() {
    var x = parseInt(document.getElementById('toteng').value);
    if (x >= 90) {
        document.getElementById("eng_grade").value = 1;
        document.getElementById('indicate').innerHTML = "Excellence"

    } else if (x >= 80) {
        document.getElementById("eng_grade").value = 2;
        document.getElementById('indicate').innerHTML = "Very Good"
    } else if (x >= 70) {
        document.getElementById("eng_grade").value = 3;
        document.getElementById('indicate').innerHTML = "Good"
    } else if (x >= 60) {
        document.getElementById("eng_grade").value = 4;
        document.getElementById('indicate').innerHTML = "Satisfactory"
    } else if (x >= 50) {
        document.getElementById("eng_grade").value = 5;
        document.getElementById('indicate').innerHTML = "Pass"

    } else if (x >= 40) {
        document.getElementById("eng_grade").value = 6;
        document.getElementById('indicate').innerHTML = "Weak Pass"
    } else if (x >= 0) {
        document.getElementById("eng_grade").value = 9;
        document.getElementById('indicate').innerHTML = "Failed"
    } else {
        document.getElementById("eng_grade").value = '';
        document.getElementById('indicate').innerHTML = "N/A"
    }
}


//Mathematics

function maths(value) {
    x = 0.5 * value;
    document.getElementById("clswkmath50").value = x;
}

function mathExams(value) {
    x = 0.5 * value;
    document.getElementById("exammath50").value = x;
}


function addMaths() {
    var x = parseInt(document.getElementById('clswkmath50').value);
    var y = parseInt(document.getElementById('exammath50').value);
    var res = x + y;
    document.getElementById("mathtot").value = res;
    gradeMaths();
}



function gradeMaths() {
    var x = parseInt(document.getElementById('mathtot').value);
    if (x >= 90) {
        document.getElementById("math_grade").value = 1;
        document.getElementById('indicatemath').innerHTML = "Excellence"

    } else if (x >= 80) {
        document.getElementById("math_grade").value = 2;
        document.getElementById('indicatemath').innerHTML = "Very Good"
    } else if (x >= 70) {
        document.getElementById("math_grade").value = 3;
        document.getElementById('indicatemath').innerHTML = "Good"
    } else if (x >= 60) {
        document.getElementById("math_grade").value = 4;
        document.getElementById('indicatemath').innerHTML = "Satisfactory"
    } else if (x >= 50) {
        document.getElementById("math_grade").value = 5;
        document.getElementById('indicatemath').innerHTML = "Pass"

    } else if (x >= 40) {
        document.getElementById("math_grade").value = 6;
        document.getElementById('indicatemath').innerHTML = "Weak Pass"
    } else if (x >= 0) {
        document.getElementById("math_grade").value = 9;
        document.getElementById('indicatemath').innerHTML = "Failed"
    } else {
        document.getElementById("math_grade").value = '';
        document.getElementById('indicatemath').innerHTML = "N/A"
    }
}



//Science

function scienceClass(value) {
    x = 0.5 * value;
    document.getElementById("clswksc50").value = x;
}

function scienceExams(value) {
    x = 0.5 * value;
    document.getElementById("examsc50").value = x;
}


function addScience() {
    var x = parseInt(document.getElementById('clswksc50').value);
    var y = parseInt(document.getElementById('examsc50').value);
    var res = x + y;
    document.getElementById("totsc").value = res;
    gradeScience();
}



function gradeScience() {
    var x = parseInt(document.getElementById('totsc').value);
    if (x >= 90) {
        document.getElementById("sc_grade").value = 1;
        document.getElementById('indicateScience').innerHTML = "Excellence"

    } else if (x >= 80) {
        document.getElementById("sc_grade").value = 2;
        document.getElementById('indicateScience').innerHTML = "Very Good"
    } else if (x >= 70) {
        document.getElementById("sc_grade").value = 3;
        document.getElementById('indicateScience').innerHTML = "Good"
    } else if (x >= 60) {
        document.getElementById("sc_grade").value = 4;
        document.getElementById('indicateScience').innerHTML = "Satisfactory"
    } else if (x >= 50) {
        document.getElementById("sc_grade").value = 5;
        document.getElementById('indicateScience').innerHTML = "Pass"

    } else if (x >= 40) {
        document.getElementById("sc_grade").value = 6;
        document.getElementById('indicateScience').innerHTML = "Weak Pass"
    } else if (x >= 0) {
        document.getElementById("sc_grade").value = 9;
        document.getElementById('indicateScience').innerHTML = "Failed"
    } else {
        document.getElementById("sc_grade").value = '';
        document.getElementById('indicateScience').innerHTML = "N/A"
    }
}


//Socail

function socialClass(value) {
    x = 0.5 * value;
    document.getElementById("clswksoc50").value = x;
}

function socialExams(value) {
    x = 0.5 * value;
    document.getElementById("examsoc50").value = x;
}


function addSocial() {
    var x = parseInt(document.getElementById('clswksoc50').value);
    var y = parseInt(document.getElementById('examsoc50').value);
    var res = x + y;
    document.getElementById("totsoc").value = res;
    gradeSocial();
}



function gradeSocial() {
    var x = parseInt(document.getElementById('totsoc').value);
    if (x >= 90) {
        document.getElementById("soc_grade").value = 1;
        document.getElementById('indicateSoc').innerHTML = "Excellence"

    } else if (x >= 80) {
        document.getElementById("soc_grade").value = 2;
        document.getElementById('indicateSoc').innerHTML = "Very Good"
    } else if (x >= 70) {
        document.getElementById("soc_grade").value = 3;
        document.getElementById('indicateSoc').innerHTML = "Good"
    } else if (x >= 60) {
        document.getElementById("soc_grade").value = 4;
        document.getElementById('indicateSoc').innerHTML = "Satisfactory"
    } else if (x >= 50) {
        document.getElementById("soc_grade").value = 5;
        document.getElementById('indicateSoc').innerHTML = "Pass"

    } else if (x >= 40) {
        document.getElementById("soc_grade").value = 6;
        document.getElementById('indicateSoc').innerHTML = "Weak Pass"
    } else if (x >= 0) {
        document.getElementById("soc_grade").value = 9;
        document.getElementById('indicateSoc').innerHTML = "Failed"
    } else {
        document.getElementById("soc_grade").value = '';
        document.getElementById('indicateSoc').innerHTML = "N/A"
    }
}

//RME

function rmeClass(value) {
    x = 0.5 * value;
    document.getElementById("clswkrme50").value = x;
}

function rmeExams(value) {
    x = 0.5 * value;
    document.getElementById("examrme50").value = x;
}


function addRme() {
    var x = parseInt(document.getElementById('clswkrme50').value);
    var y = parseInt(document.getElementById('examrme50').value);
    var res = x + y;
    document.getElementById("totrme").value = res;
    gradeRme();
}



function gradeRme() {
    var x = parseInt(document.getElementById('totrme').value);
    if (x >= 90) {
        document.getElementById("rme_grade").value = 1;
        document.getElementById('indicateRme').innerHTML = "Excellence"

    } else if (x >= 80) {
        document.getElementById("rme_grade").value = 2;
        document.getElementById('indicateRme').innerHTML = "Very Good"
    } else if (x >= 70) {
        document.getElementById("rme_grade").value = 3;
        document.getElementById('indicateRme').innerHTML = "Good"
    } else if (x >= 60) {
        document.getElementById("rme_grade").value = 4;
        document.getElementById('indicateRme').innerHTML = "Satisfactory"
    } else if (x >= 50) {
        document.getElementById("rme_grade").value = 5;
        document.getElementById('indicateRme').innerHTML = "Pass"

    } else if (x >= 40) {
        document.getElementById("rme_grade").value = 6;
        document.getElementById('indicateRme').innerHTML = "Weak Pass"
    } else if (x >= 0) {
        document.getElementById("rme_grade").value = 9;
        document.getElementById('indicateRme').innerHTML = "Failed"
    } else {
        document.getElementById("rme_grade").value = '';
        document.getElementById('indicateRme').innerHTML = "N/A"
    }
}

//BDT

function bdtClass(value) {
    x = 0.5 * value;
    document.getElementById("clswkdbt50").value = x;
}

function bdtExams(value) {
    x = 0.5 * value;
    document.getElementById("exambdt50").value = x;
}


function addBdt() {
    var x = parseInt(document.getElementById('clswkdbt50').value);
    var y = parseInt(document.getElementById('exambdt50').value);
    var res = x + y;
    document.getElementById("totbdt").value = res;
    gradeBdt();
}



function gradeBdt() {
    var x = parseInt(document.getElementById('totbdt').value);
    if (x >= 90) {
        document.getElementById("bdt_grade").value = 1;
        document.getElementById('indicatebdt').innerHTML = "Excellence"

    } else if (x >= 80) {
        document.getElementById("bdt_grade").value = 2;
        document.getElementById('indicatebdt').innerHTML = "Very Good"
    } else if (x >= 70) {
        document.getElementById("bdt_grade").value = 3;
        document.getElementById('indicatebdt').innerHTML = "Good"
    } else if (x >= 60) {
        document.getElementById("bdt_grade").value = 4;
        document.getElementById('indicatebdt').innerHTML = "Satisfactory"
    } else if (x >= 50) {
        document.getElementById("bdt_grade").value = 5;
        document.getElementById('indicatebdt').innerHTML = "Pass"

    } else if (x >= 40) {
        document.getElementById("bdt_grade").value = 6;
        document.getElementById('indicatebdt').innerHTML = "Weak Pass"
    } else if (x >= 0) {
        document.getElementById("bdt_grade").value = 9;
        document.getElementById('indicatebdt').innerHTML = "Failed"
    } else {
        document.getElementById("bdt_grade").value = '';
        document.getElementById('indicatebdt').innerHTML = "N/A"
    }
}

//ICT

function ictClass(value) {
    x = 0.5 * value;
    document.getElementById("clswkict50").value = x;
}

function ictExams(value) {
    x = 0.5 * value;
    document.getElementById("examict50").value = x;
}


function addIct() {
    var x = parseInt(document.getElementById('clswkict50').value);
    var y = parseInt(document.getElementById('examict50').value);
    var res = x + y;
    document.getElementById("totict").value = res;
    gradeIct();
}



function gradeIct() {
    var x = parseInt(document.getElementById('totict').value);
    document.getElementById("ict_grade").style.backgroundColor = "WHITE";
    if (x >= 90) {
        document.getElementById("ict_grade").value = 1;
        document.getElementById('indicateIct').innerHTML = "Excellence"

    } else if (x >= 80) {
        document.getElementById("ict_grade").value = 2;
        document.getElementById('indicateIct').innerHTML = "Very Good"
    } else if (x >= 70) {
        document.getElementById("ict_grade").value = 3;
        document.getElementById('indicateIct').innerHTML = "Good"
    } else if (x >= 60) {
        document.getElementById("ict_grade").value = 4;
        document.getElementById("ict_grade").style.border = "solid .5px cyan";
    } else if (x >= 50) {
        document.getElementById("ict_grade").value = 5;
        document.getElementById('indicateIct').innerHTML = "Pass"

    } else if (x >= 40) {
        document.getElementById("ict_grade").value = 6;
        document.getElementById('indicateIct').innerHTML = "Weak Pass"
    } else if (x >= 0) {
        document.getElementById("ict_grade").value = 9;
        document.getElementById('indicateIct').innerHTML = "Failed"
    } else {
        document.getElementById("ict_grade").value = '';
        document.getElementById('indicateIct').innerHTML = "N/A"
    }
}

//Ghanaian Language

function ghlClass(value) {
    x = 0.5 * value;
    document.getElementById("clswkghlang50").value = x;
}

function ghlExams(value) {
    x = 0.5 * value;
    document.getElementById("examghlang50").value = x;
}


function addGhl() {
    var x = parseInt(document.getElementById('clswkghlang50').value);
    var y = parseInt(document.getElementById('examghlang50').value);
    var res = x + y;
    document.getElementById("totghlang").value = res;
    gradeGhl();
}



function gradeGhl() {
    var x = parseInt(document.getElementById('totghlang').value);
    if (x >= 90) {
        document.getElementById("ghlang_grade").value = 1;
        document.getElementById('indicateGhl').innerHTML = "Excellence"
    } else if (x >= 80) {
        document.getElementById("ghlang_grade").value = 2;
        document.getElementById('indicateGhl').innerHTML = "Very Good"
    } else if (x >= 70) {
        document.getElementById("ghlang_grade").value = 3;
        document.getElementById('indicateGhl').innerHTML = "Good"
    } else if (x >= 60) {
        document.getElementById("ghlang_grade").value = 4;
        document.getElementById('indicateGhl').innerHTML = "Satisfactory"
    } else if (x >= 50) {
        document.getElementById("ghlang_grade").value = 5;
        document.getElementById('indicateGhl').innerHTML = "Pass"

    } else if (x >= 40) {
        document.getElementById("ghlang_grade").value = 6;
        document.getElementById('indicateGhl').innerHTML = "Weak Pass"
    } else if (x >= 0) {
        document.getElementById("ghlang_grade").value = 9;
        document.getElementById('indicateGhl').innerHTML = "Failed"
    } else {
        document.getElementById("ghlang_grade").value = '';
        document.getElementById('indicateGhl').innerHTML = "N/A"
    }
}


//French

function frClass(value) {
    x = 0.5 * value;
    document.getElementById("clswkfr50").value = x;
}

function frExams(value) {
    x = 0.5 * value;
    document.getElementById("examfr50").value = x;
}


function addFr() {
    var x = parseInt(document.getElementById('clswkfr50').value);
    var y = parseInt(document.getElementById('examfr50').value);
    var res = x + y;
    document.getElementById("totfr").value = res;
    gradeFr();
}



function gradeFr() {
    var x = parseInt(document.getElementById('totfr').value);
    if (x >= 90) {
        document.getElementById("fr_grade").value = 1;
        document.getElementById('indicatefr').innerHTML = "Excellence"

    } else if (x >= 80) {
        document.getElementById("fr_grade").value = 2;
        document.getElementById('indicatefr').innerHTML = "Very Good"
    } else if (x >= 70) {
        document.getElementById("fr_grade").value = 3;
        document.getElementById('indicatefr').innerHTML = "Good"
    } else if (x >= 60) {
        document.getElementById("fr_grade").value = 4;
    } else if (x >= 50) {
        document.getElementById("fr_grade").value = 5;
        document.getElementById('indicatefr').innerHTML = "Pass"

    } else if (x >= 40) {
        document.getElementById("fr_grade").value = 6;
        document.getElementById('indicatefr').innerHTML = "Weak Pass"
    } else if (x >= 0) {
        document.getElementById("fr_grade").value = 9;
        document.getElementById('indicatefr').innerHTML = "Failed"
    } else {
        document.getElementById("fr_grade").value = '';
        document.getElementById('indicatefr').innerHTML = "N/A"
    }
}