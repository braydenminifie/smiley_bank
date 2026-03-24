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
        addStudentToGrid(data);
        console.log('Success:', data);
    });
}

function addStudentToGrid(student) { //Dynamically add student to grid (without refreshing the page)
    const grid = document.querySelector(".piggy_bank_grid");

    const div = document.createElement("div");
    div.className = "piggy_bank_instance";

    div.style.backgroundImage = `url('../static/${student.bank_colour}.png')`;
    div.setAttribute("data-student-id", student.student_id);

    div.innerHTML = `
        <button class="delete_student_btn" onclick="removeStudentModal(${student.student_id})">
            <img src="../static/X_pig.png">
        </button>

        <div class="piggy_bank_name">${student.name}</div>

        <div class="piggy_bank_smiles" id="smiles_${student.student_id}">
            ${student.smiles}
        </div>

        <button class="add_smile_btn" onclick="addPoint(${student.student_id})">
            <img src="../static/PLUS_pig.png">
        </button>

        <button class="remove_smile_btn" onclick="removePoint(${student.student_id})">
            <img src="../static/MINUS_pig.png">
        </button>
    `;

    const addNew = document.querySelector(".new_student");
    grid.insertBefore(div, addNew);
}

//The Delete Student Modal
var delete_student_modal = document.getElementById("delete_student_modal_background");
let selected_student_id = null;
var leave_delete_student_modal_btn = document.getElementById("leave_del_student_button")

leave_delete_student_modal_btn.onclick = function() {
    delete_student_modal.style.display = "none";
}

function removeStudentModal(student_id) {
    delete_student_modal.style.display = "block";
    selected_student_id = student_id
}

function removeStudent() {
    fetch(`/remove_student/${selected_student_id}`, {
        method: 'POST'
    })
    .then(result => result.json()) 
    .then((data) => {
        removeStudentFromGrid(data)
        delete_student_modal.style.display = "none";
    });
}

function removeStudentFromGrid(student_obj) {
    const id = student_obj.student_id
    const studentCard = document.querySelector(`.piggy_bank_instance[data-student-id="${id}"]`);

    if (studentCard) {
        studentCard.remove();
    }
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

//The Store Modal
var shop_modal = document.getElementById("store_modal_background");
var open_shop_btn = document.getElementById("shop_btn")
var close_shop_btn = document.getElementById("leave_store_modal_btn")

open_shop_btn.onclick = function() {
    shop_modal.style.display = "block";
}

close_shop_btn.onclick = function() {
    shop_modal.style.display = "none";
}

function removePrize(prizeId) {
    fetch(`/remove_prize/${prizeId}`, {
        method: 'POST'
    });
}

//The 'Add Prize' Modal
var prize_modal = document.getElementById("create_prize_modal_background");
var open_add_prize_btn = document.getElementById("new_store_modal_btn");
var close_add_prize_btn = document.getElementById("leave_image_btn");


open_add_prize_btn.onclick = function() {
    prize_modal.style.display = "block";
    shop_modal.style.display = "none";
}

close_add_prize_btn.onclick = function() {
    prize_modal.style.display = "none";
    shop_modal.style.display = "block";
}

var add_prize_btn = document.getElementById("add_image_btn");
var add_prize_form = document.getElementById("create_prize_form");

add_prize_form.addEventListener("submit", function (event) {
    event.preventDefault();

    const formData = new FormData(add_prize_form);
    fetch(`/add_prize`, {
        method: 'POST',
        body: formData,
    });


});


//The History Modal
var history_modal = document.getElementById("history_modal_background");
var open_history_btn = document.getElementById("history_btn");
var leave_history_btn = document.getElementById("leave_history_btn");

open_history_btn.onclick = function() {
    history_modal.style.display = "block";
}

leave_history_btn.onclick = function() {
    history_modal.style.display = "none";
}