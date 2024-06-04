const form_button = document.querySelector('.edit');
const cancel_button = document.querySelector('.cancel');
const book_info = document.querySelector('#displaybook');
const book_edit = document.querySelector('#editbook');
form_button.addEventListener("click", function (e) {
    console.log("edit");
    book_info.classList.toggle("hidden");
    book_info.classList.toggle("d-flex");
    book_edit.classList.toggle("hidden");
    book_edit.classList.toggle("d-flex");
})
cancel_button.addEventListener("click", function (e) {
    console.log("hide");
    book_info.classList.toggle("hidden");
    book_info.classList.toggle("d-flex");
    book_edit.classList.toggle("hidden");
    book_edit.classList.toggle("d-flex");
})