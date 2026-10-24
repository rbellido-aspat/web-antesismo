/* antesismo: menú móvil y formularios de la versión de revisión. */
(function () {
  "use strict";
  var boton = document.querySelector(".nav-toggle");
  var nav = document.getElementById("nav-principal");
  if (boton && nav) {
    boton.addEventListener("click", function () {
      var abierto = nav.classList.toggle("abierto");
      boton.setAttribute("aria-expanded", abierto ? "true" : "false");
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("abierto")) {
        nav.classList.remove("abierto");
        boton.setAttribute("aria-expanded", "false");
        boton.focus();
      }
    });
  }

  /* Los formularios aún no tienen destino de envío: se avisa en vez de perder datos. */
  Array.prototype.forEach.call(document.querySelectorAll("form[data-pendiente]"), function (f) {
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      var aviso = f.querySelector(".form-estado");
      if (aviso) {
        aviso.textContent = "Gracias. Esta es la versión de revisión del sitio y el envío todavía no está conectado, así que tus datos no se guardaron.";
        aviso.classList.add("visible");
        aviso.focus();
      }
    });
  });
})();
