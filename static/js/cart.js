window.addEventListener("scroll", function(){
    const cartTopRow = document.getElementById('cartTopRow');
    cartTopRow.classList.toggle("sticky", window.scrollY > 40)
})