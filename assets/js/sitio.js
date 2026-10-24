/* antesismo: menú móvil y formularios que preparan un correo. */
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

  /* Los formularios no envían datos a ningún servidor: arman un correo y abren el programa de correo del usuario. */
  Array.prototype.forEach.call(document.querySelectorAll("form[data-correo]"), function (f) {
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      var aviso = f.querySelector(".form-estado");
      var faltan = Array.prototype.filter.call(f.querySelectorAll("[required]"), function (c) { return !c.value.trim(); });
      if (faltan.length) {
        if (aviso) { aviso.textContent = "Completa los campos obligatorios: " + faltan.map(function (c) { return c.closest("label").firstChild.textContent.trim(); }).join(", ") + "."; aviso.classList.add("visible"); }
        faltan[0].focus();
        return;
      }
      var lineas = [];
      Array.prototype.forEach.call(f.querySelectorAll("input, select, textarea"), function (c) {
        if (!c.value.trim()) return;
        var etiqueta = c.closest("label") ? c.closest("label").firstChild.textContent.trim() : c.name;
        lineas.push(etiqueta + ": " + c.value.trim());
      });
      var url = "mailto:" + f.getAttribute("data-correo") +
        "?subject=" + encodeURIComponent("antesismo, " + f.getAttribute("data-asunto")) +
        "&body=" + encodeURIComponent(lineas.join("\n\n"));
      window.location.href = url;
      if (aviso) {
        aviso.textContent = "Se abrió tu programa de correo con el mensaje listo. Si no se abrió, escribe directamente a " + f.getAttribute("data-correo") + ".";
        aviso.classList.add("visible");
      }
    });
  });
})();
