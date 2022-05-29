const toggleb = document.getElementById("toggle");
const navbar=document.getElementsByClassName("right")[0];

toggleb.addEventListener("click", function () {
    navbar.classList.toggle('active');
})