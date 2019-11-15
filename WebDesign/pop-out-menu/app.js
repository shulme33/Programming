function animateMenu() {
  console.log("Animate Menu Clicked");
  const menuIcon = document.getElementById("fa-bars-icon");
  const menu = document.getElementById("left-menu");
  menuIcon.addEventListener("click", () => {
    if (menu.positionValue === "invisible") {
      //Need to move menu in
      moveMenuIn(menu);
    } else {
      //Need to move menu out
      moveMenuOut(menu);
    }
    menu.positionValue =
      menu.positionValue === "invisible" ? "visible" : "invisible";
  });
}

function moveMenuIn(menu) {
  console.log("Move menu in");
  menu.style.animation = "make-menu-visible 0.5s ease";
  menu.addEventListener("animationend", () => {
    menu.classList.remove("menu-inactive");
    menu.classList.add("menu-active");
    menu.style.animation = "";
  });
}

function moveMenuOut(menu) {
  console.log("Move menu out");
  menu.style.animation = "make-menu-invisible 0.5s ease";
  menu.addEventListener("animationend", () => {
    menu.classList.remove("menu-active");
    menu.classList.add("menu-inactive");
    menu.style.animation = "";
  });
}

animateMenu();
