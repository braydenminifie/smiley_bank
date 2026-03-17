// The Create Student Modal
var create_student_modal = document.getElementById("new_student_modal_background");
var open_create_student_btn = document.getElementById("add_new_student_btn");
var leave_create_student_btn = document.getElementById("leave_button");

var create_student_btn = document.getElementById("add_button");
var student_name_input = document.getElementById("enter_name_search_input")

open_create_student_btn.onclick = function() {
    create_student_modal.style.display = "block";
}

leave_create_student_btn.onclick = function() {
    create_student_modal.style.display = "none";
}

create_student_btn.onclick = function() {
    var student_name_value = student_name_input.value;
    var bank_colour_input = document.querySelector('input[name="bank_options"]:checked');
    var bank_colour = bank_colour_input.id; 
    var data = {name: student_name_value, colour: bank_colour}

    fetch('/add_student', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        create_student_modal.style.display = "none";
        console.log('Success:', data);
    });
}

//The Delete Student Modal
var delete_student_modal = document.getElementById("delete_student_modal_background");
let selected_student_id = null;

function removeStudentModal(student_id) {
    delete_student_modal.style.display = "block";
    selected_student_id = student_id
}

function removeStudent() {
    fetch(`/remove_student/${selected_student_id}`, {
        method: 'POST'
    })
    .then(() => {
        delete_student_modal.style.display = "none";
    });
}

//Add Point
function addPoint(studentId) {
    fetch(`/add_point/${studentId}`, {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById(`smiles_${studentId}`).innerText = data.points;
    });
}

//Remove Point
function removePoint(studentId) {
    fetch(`/remove_point/${studentId}`, {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById(`smiles_${studentId}`).innerText = data.points;
    });
}