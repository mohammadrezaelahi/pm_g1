let menu = document.getElementById("burgermenu");
let menuOpen = document.getElementById("burgermenuopen");
let listnavbar = document.getElementById("listNavbar");
menu.addEventListener('click',()=>{
    menuOpen.style.display = "block"
    menu.style.display = "none"
    listnavbar.style.display = "flex"
    listnavbar.style.flexDirection = "column"
    listnavbar.style.gap = "0.5rem"
    listnavbar.style.position = "relative"
    listnavbar.style.top = "4px"
    listnavbar.style.right = "39px"
    menuOpen.style.zIndex = "20"
})

menuOpen.addEventListener('click',()=>{
    menuOpen.style.display = "none"
    menu.style.display = "block"
    listnavbar.style.display = "none"
    listnavbar.style.flexDirection = "row"
    listnavbar.style.gap = "1rem"
})