/* antesismo: figuras del caso demostrativo dibujadas desde los datos del motor.
   Lee window.ANTESISMO_CASO (assets/js/datos-caso.js) y dibuja en los elementos con data-figura. */
(function () {
  "use strict";
  var D = window.ANTESISMO_CASO;
  if (!D) return;
  var NS = "http://www.w3.org/2000/svg";
  var CLASE = { normal: "normal", aceptable: "aceptable", fuera: "fuera" };
  var TEXTO_CLASE = { normal: "normal", aceptable: "aceptable", fuera: "fuera de rango" };
  var GRAFITO = "#263036", VERDE = "#297e7a", LADRILLO = "#a8672f";

  function fmt(v) {
    var a = Math.abs(v);
    var s = a >= 10 ? v.toFixed(1) : a >= 1 ? v.toFixed(2) : a >= 0.01 ? v.toFixed(3) : v.toFixed(5);
    s = s.replace(/(\.\d*?)0+$/, "$1").replace(/\.$/, "");
    return s.replace(".", ",");
  }
  function el(tag, attrs, html) {
    var e = document.createElement(tag);
    if (attrs) for (var k in attrs) e.setAttribute(k, attrs[k]);
    if (html != null) e.innerHTML = html;
    return e;
  }
  function s(tag, attrs) {
    var e = document.createElementNS(NS, tag);
    for (var k in attrs) e.setAttribute(k, attrs[k]);
    return e;
  }
  function unidad(it) { return it.unidad ? " " + it.unidad : ""; }

  /* Información emergente compartida */
  var tip = el("div", { class: "tip", role: "tooltip" });
  document.body.appendChild(tip);
  function mostrar(e, html) {
    tip.innerHTML = html; tip.classList.add("visible");
    var r = e.getBoundingClientRect();
    var x = Math.min(window.innerWidth - tip.offsetWidth - 8, Math.max(8, r.left + r.width / 2 - tip.offsetWidth / 2));
    var y = r.top - tip.offsetHeight - 10;
    if (y < 8) y = r.bottom + 10;
    tip.style.left = x + "px"; tip.style.top = y + "px";
  }
  function ocultar() { tip.classList.remove("visible"); }
  function conTip(nodo, html) {
    nodo.setAttribute("tabindex", "0");
    nodo.addEventListener("mouseenter", function () { mostrar(nodo, html); });
    nodo.addEventListener("focus", function () { mostrar(nodo, html); });
    nodo.addEventListener("mouseleave", ocultar);
    nodo.addEventListener("blur", ocultar);
  }
  window.addEventListener("scroll", ocultar, { passive: true });

  var P = D.perfil;
  var GRUPOS = ["Rigidez", "Acoplamiento", "Redundancia y ductilidad", "Densidad de muros"];
  function grupoDe(it) {
    if (it.grupo.indexOf("Redund") === 0) return "Redundancia y ductilidad";
    if (it.grupo.indexOf("Densidad") === 0) return "Densidad de muros";
    return it.grupo;
  }
  function conteo() {
    var c = { normal: 0, aceptable: 0, fuera: 0, indFuera: [] };
    P.forEach(function (it) {
      c[it.cx]++; c[it.cy]++;
      if (it.cx === "fuera" || it.cy === "fuera") c.indFuera.push(it);
    });
    return c;
  }
  function tipIndicador(it) {
    return "<strong>" + it.n + ". " + it.nombre + "</strong>" +
      "Dirección X: " + fmt(it.X) + unidad(it) + ", " + TEXTO_CLASE[it.cx] + "<br>" +
      "Dirección Y: " + fmt(it.Y) + unidad(it) + ", " + TEXTO_CLASE[it.cy];
  }

  /* 1. Semáforo compacto de 21 indicadores */
  function semaforo(cont) {
    var c = conteo();
    var caja = el("div", { class: "semaforo" });
    caja.appendChild(el("div", { class: "semaforo-cabeza" },
      "<h3>Perfil Bío-Sísmico, 21 indicadores por dirección</h3><span>Caso demostrativo, edificio de 1963</span>"));
    GRUPOS.forEach(function (g) {
      var items = P.filter(function (it) { return grupoDe(it) === g; });
      var bloque = el("div", { class: "semaforo-grupo" });
      bloque.appendChild(el("h4", null, g));
      var celdas = el("div", { class: "semaforo-celdas" });
      items.forEach(function (it) {
        var celda = el("div", { class: "celda", "aria-label": "Indicador " + it.n + ", X " + TEXTO_CLASE[it.cx] + ", Y " + TEXTO_CLASE[it.cy] },
          "<b>" + it.n + "</b><span class=\"xy\"><i class=\"" + CLASE[it.cx] + "\">X</i><i class=\"" + CLASE[it.cy] + "\">Y</i></span>");
        conTip(celda, tipIndicador(it));
        celdas.appendChild(celda);
      });
      bloque.appendChild(celdas);
      caja.appendChild(bloque);
    });
    var res = el("div", { class: "semaforo-resumen" },
      "<span class=\"estado normal\">" + c.normal + " normal</span>" +
      "<span class=\"estado aceptable\">" + c.aceptable + " aceptable</span>" +
      "<span class=\"estado fuera\">" + c.fuera + " fuera de rango</span>" +
      "<span>de 42 lecturas, 21 indicadores en X e Y</span>");
    caja.appendChild(res);
    var pie = c.indFuera.length
      ? "Fuera de rango: " + c.indFuera.map(function (it) { return "indicador " + it.n + ", " + (it.nombre.split(",")[1] || it.nombre).trim() + " en " + (it.cx === "fuera" ? (it.cy === "fuera" ? "X e Y" : "X") : "Y"); }).join("; ") + ". Pasa el cursor o el foco por cada celda para ver el valor."
      : "Pasa el cursor o el foco por cada celda para ver el valor.";
    caja.appendChild(el("p", { class: "semaforo-pie" }, pie));
    cont.appendChild(caja);
  }

  /* 2. Bandas completas de los 21 indicadores */
  function bandas(cont) {
    cont.appendChild(el("div", { class: "bandas-leyenda" },
      "<span><span class=\"muestra\" style=\"background:var(--normal-bg)\"></span>Dentro de rangos normales</span>" +
      "<span><span class=\"muestra\" style=\"background:var(--acept-bg)\"></span>Aceptable, ligeramente apartado</span>" +
      "<span><span class=\"muestra\" style=\"background:var(--fuera-bg)\"></span>Fuera de rango</span>" +
      "<span><span class=\"mk mk-x\"></span>Sismo en X</span>" +
      "<span><span class=\"mk mk-y\"></span>Sismo en Y</span>"));
    GRUPOS.forEach(function (g) {
      var items = P.filter(function (it) { return grupoDe(it) === g; });
      var bloque = el("div", { class: "bandas-grupo" });
      bloque.appendChild(el("h3", null, g));
      items.forEach(function (it) {
        var fila = el("div", { class: "fila" });
        fila.appendChild(el("div", { class: "nom" }, "<b>" + it.n + ".</b>" + it.nombre + (it.unidad ? " [" + it.unidad + "]" : "")));
        var pista = el("div", { class: "pista" });
        var b = it.bandas, ini = b[0][0], fin = b[b.length - 1][1], ancho = fin - ini;
        var tramos = el("div", { class: "tramos", "aria-hidden": "true" });
        b.forEach(function (t) {
          var w = (t[1] - t[0]) / ancho * 100;
          tramos.appendChild(el("span", { class: "t-" + t[2], style: "flex:0 0 calc(" + w.toFixed(3) + "% - 2px)" }));
        });
        pista.appendChild(tramos);
        var ticks = el("div", { class: "ticks", "aria-hidden": "true" });
        var vistos = {};
        [ini].concat(b.map(function (t) { return t[1]; })).forEach(function (v) {
          if (vistos[v]) return; vistos[v] = 1;
          ticks.appendChild(el("span", { style: "left:" + ((v - ini) / ancho * 100).toFixed(3) + "%" }, fmt(v)));
        });
        pista.appendChild(ticks);
        [["x", it.X, it.cx, "X"], ["y", it.Y, it.cy, "Y"]].forEach(function (m) {
          var pos = Math.max(0, Math.min(1, (m[1] - ini) / ancho)) * 100;
          var mk = el("span", { class: "marca " + m[0], style: "left:" + pos.toFixed(3) + "%", "aria-label": "Dirección " + m[3] + ": " + fmt(m[1]) + ", " + TEXTO_CLASE[m[2]] });
          conTip(mk, "<strong>" + it.n + ". Dirección " + m[3] + "</strong>" + fmt(m[1]) + unidad(it) + ", " + TEXTO_CLASE[m[2]]);
          pista.appendChild(mk);
        });
        fila.appendChild(pista);
        fila.appendChild(el("div", { class: "val" },
          "<span>X " + fmt(it.X) + " <span class=\"estado " + it.cx + "\">" + TEXTO_CLASE[it.cx] + "</span></span>" +
          "<span>Y " + fmt(it.Y) + " <span class=\"estado " + it.cy + "\">" + TEXTO_CLASE[it.cy] + "</span></span>"));
        bloque.appendChild(fila);
      });
      cont.appendChild(bloque);
    });
  }

  /* 3. Tabla de los 21 indicadores (vista accesible) */
  function tabla(cont) {
    var h = "<div class=\"tabla-envoltura\"><table><caption class=\"visual-oculto\">Los 21 indicadores del caso demostrativo</caption><thead><tr><th>N.º</th><th>Indicador</th><th>Grupo</th><th class=\"num\">X</th><th>Calificación X</th><th class=\"num\">Y</th><th>Calificación Y</th></tr></thead><tbody>";
    P.forEach(function (it) {
      h += "<tr><td>" + it.n + "</td><td>" + it.nombre + (it.unidad ? " [" + it.unidad + "]" : "") + "</td><td>" + grupoDe(it) + "</td><td class=\"num\">" + fmt(it.X) +
        "</td><td><span class=\"estado " + it.cx + "\">" + TEXTO_CLASE[it.cx] + "</span></td><td class=\"num\">" + fmt(it.Y) +
        "</td><td><span class=\"estado " + it.cy + "\">" + TEXTO_CLASE[it.cy] + "</span></td></tr>";
    });
    cont.innerHTML = h + "</tbody></table></div>";
  }

  /* Geometría: planta de muros en SVG */
  var G = D.geometria, M = 1.6;
  function svgPlanta(piso, opciones) {
    opciones = opciones || {};
    var W = G.LX + 2 * M, H = G.LY + 2 * M + (opciones.balcon ? 1.2 : 0);
    var svg = s("svg", { viewBox: (-M) + " " + (-M) + " " + W + " " + H, role: "img" });
    var gy = function (y) { return G.LY - y; };
    svg.appendChild(s("rect", { x: -0.1, y: -0.1, width: G.LX + 0.2, height: G.LY + 0.2, fill: "#f3f6f7", stroke: "#b9c6ca", "stroke-width": 0.04, "stroke-dasharray": "0.15 0.12" }));
    if (opciones.balcon) svg.appendChild(s("rect", { x: -0.1, y: G.LY + 0.1, width: G.LX + 0.2, height: 1.5, fill: "none", stroke: "#b9c6ca", "stroke-width": 0.04, "stroke-dasharray": "0.06 0.1" }));
    [[0, "A"], [6.05, "B"], [9.35, "C"]].forEach(function (a) {
      var t = s("text", { x: a[0], y: -0.7, "font-size": 0.55, "text-anchor": "middle", fill: "#5f6e75", "font-family": "Inter, Arial, sans-serif" });
      t.textContent = a[1]; svg.appendChild(t);
    });
    [[0, "1"], [3.2, "2"], [5.4, "3"], [8.35, "4"], [11.25, "5"], [14.2, "6"]].forEach(function (a) {
      var t = s("text", { x: -0.85, y: gy(a[0]) + 0.2, "font-size": 0.55, "text-anchor": "middle", fill: "#5f6e75", "font-family": "Inter, Arial, sans-serif" });
      t.textContent = a[1]; svg.appendChild(t);
    });
    G.muros.forEach(function (m) {
      if (m.pisos.indexOf(piso) < 0) return;
      var lad = m.mat === "LAD" || (m.mat === "HA_LAD" && piso >= 4);
      svg.appendChild(s("rect", { x: m.x, y: gy(m.y + m.h), width: m.w, height: m.h, fill: lad ? LADRILLO : GRAFITO, rx: 0.03 }));
    });
    if (opciones.cm !== false) {
      var cm = G.cm[piso - 1], cx = cm[0], cy = gy(cm[1]);
      svg.appendChild(s("circle", { cx: cx, cy: cy, r: 0.32, fill: "#fff", stroke: VERDE, "stroke-width": 0.1 }));
      svg.appendChild(s("path", { d: "M" + (cx - 0.5) + " " + cy + "h1M" + cx + " " + (cy - 0.5) + "v1", stroke: VERDE, "stroke-width": 0.1 }));
    }
    return svg;
  }

  function plantas(cont) {
    var envol = el("div", { class: "rejilla-3" });
    [[1, "Piso 1, ejes y centro de masas", true], [3, "Pisos 1 a 3, iguales", false], [4, "Pisos 4 y 5, eje B en albañilería", false]].forEach(function (p) {
      var fig = el("figure", { class: "figura" });
      var svg = svgPlanta(p[0], { balcon: true });
      svg.setAttribute("aria-label", "Planta de muros, " + p[1]);
      fig.appendChild(svg);
      fig.appendChild(el("figcaption", null, p[1]));
      envol.appendChild(fig);
    });
    cont.appendChild(envol);
    cont.appendChild(el("p", { class: "pequeño", style: "margin-top:12px" },
      "<span class=\"muestra\" style=\"display:inline-block;width:22px;height:8px;background:" + GRAFITO + ";border-radius:2px;margin-right:6px\"></span>Hormigón armado de 20 cm · " +
      "<span class=\"muestra\" style=\"display:inline-block;width:22px;height:8px;background:" + LADRILLO + ";border-radius:2px;margin:0 6px\"></span>Albañilería de ladrillo de 20 cm · " +
      "círculo verde: centro de masas · línea punteada inferior: balcones de la fachada principal"));
  }

  /* Modelo 3D en proyección isométrica */
  function iso(cont) {
    var c30 = Math.cos(Math.PI / 6), s30 = 0.5;
    var z = [0]; G.alturas.forEach(function (h) { z.push(z[z.length - 1] + h); });
    function P2(x, y, zz) { return [(x - y) * c30, -(x + y) * s30 - zz]; }
    function poly(pts) { return pts.map(function (p) { var q = P2(p[0], p[1], p[2]); return q[0].toFixed(3) + "," + q[1].toFixed(3); }).join(" "); }
    var minX = P2(0, G.LY, 0)[0] - 1, maxX = P2(G.LX, 0, 0)[0] + 1;
    var minY = P2(G.LX, G.LY, z[5])[1] - 1, maxY = P2(0, 0, 0)[1] + 1;
    var svg = s("svg", { viewBox: [minX, minY, maxX - minX, maxY - minY].join(" "), role: "img", "aria-label": "Modelo analítico 3D del edificio: muros como voladizos y losas como diafragmas rígidos, cinco pisos" });
    // Losas detrás, como contorno de cada diafragma
    for (var j = 1; j <= 5; j++) {
      svg.appendChild(s("polygon", { points: poly([[0, 0, z[j]], [G.LX, 0, z[j]], [G.LX, G.LY, z[j]], [0, G.LY, z[j]]]), fill: "rgba(41,126,122,0.06)", stroke: "#9fb4b9", "stroke-width": 0.05 }));
    }
    svg.appendChild(s("polygon", { points: poly([[0, 0, 0], [G.LX, 0, 0], [G.LX, G.LY, 0], [0, G.LY, 0]]), fill: "#eef2f3", stroke: "#b9c6ca", "stroke-width": 0.05 }));
    var muros = G.muros.slice().sort(function (a, b) { return (b.x + b.w / 2 + b.y + b.h / 2) - (a.x + a.w / 2 + a.y + a.h / 2); });
    var tonos = { HA: ["#3a474f", "#263036", "#5b6a72"], LAD: ["#b87a44", "#8f5626", "#cf9566"] };
    muros.forEach(function (m) {
      var x0 = m.x, x1 = m.x + m.w, y0 = m.y, y1 = m.y + m.h;
      for (var j = 0; j < 5; j++) {
        var piso = j + 1;
        if (m.pisos.indexOf(piso) < 0) continue;
        var t = (m.mat === "LAD" || (m.mat === "HA_LAD" && piso >= 4)) ? tonos.LAD : tonos.HA;
        var a = z[j], b = z[j + 1];
        svg.appendChild(s("polygon", { points: poly([[x0, y0, a], [x1, y0, a], [x1, y0, b], [x0, y0, b]]), fill: t[0], stroke: t[0], "stroke-width": 0.02 }));
        svg.appendChild(s("polygon", { points: poly([[x0, y0, a], [x0, y1, a], [x0, y1, b], [x0, y0, b]]), fill: t[1], stroke: t[1], "stroke-width": 0.02 }));
        if (piso === 5 || m.pisos.indexOf(piso + 1) < 0) {
          svg.appendChild(s("polygon", { points: poly([[x0, y0, b], [x1, y0, b], [x1, y1, b], [x0, y1, b]]), fill: t[2] }));
        }
      }
    });
    // Losa de techo sobre todo, translúcida
    svg.appendChild(s("polygon", { points: poly([[0, 0, z[5]], [G.LX, 0, z[5]], [G.LX, G.LY, z[5]], [0, G.LY, z[5]]]), fill: "rgba(41,126,122,0.10)", stroke: VERDE, "stroke-width": 0.06 }));
    var fig = el("figure", { class: "figura" });
    fig.appendChild(svg);
    fig.appendChild(el("figcaption", null, "Modelo analítico: cada muro es un voladizo de flexión y corte, cada losa un diafragma rígido con tres grados de libertad. Café: albañilería del eje B en los pisos 4 y 5."));
    cont.appendChild(fig);
  }

  /* Formas modales del techo */
  function modos(cont) {
    var envol = el("div", { class: "rejilla-3" });
    var cm = G.cm[4];
    D.modos.forEach(function (md, k) {
      var svg = svgPlanta(5, { cm: false });
      var esc = 0.9 / Math.max(Math.abs(md.ux), Math.abs(md.uy), Math.abs(md.rz) * 7, 1e-9);
      var pts = [[0, 0], [G.LX, 0], [G.LX, G.LY], [0, G.LY]].map(function (p) {
        var dx = esc * (md.ux - (p[1] - cm[1]) * md.rz), dy = esc * (md.uy + (p[0] - cm[0]) * md.rz);
        return (p[0] + dx).toFixed(3) + "," + (G.LY - (p[1] + dy)).toFixed(3);
      }).join(" ");
      svg.appendChild(s("polygon", { points: pts, fill: "rgba(41,126,122,0.08)", stroke: VERDE, "stroke-width": 0.12, "stroke-linejoin": "round" }));
      svg.setAttribute("aria-label", "Modo " + (k + 1) + ", período " + fmt(md.T) + " segundos");
      var fig = el("figure", { class: "figura" });
      fig.appendChild(el("p", { style: "margin:0 0 6px;font-weight:600;font-size:.92rem" }, "Modo " + (k + 1) + ": T = " + fmt(md.T) + " s"));
      fig.appendChild(el("p", { class: "pequeño", style: "margin:0 0 8px" }, "Masa participante: X " + md.px + " %, Y " + md.py + " %, rotación " + md.prz + " %"));
      fig.appendChild(svg);
      envol.appendChild(fig);
    });
    cont.appendChild(envol);
    cont.appendChild(el("p", { class: "pequeño", style: "margin-top:12px" }, "Verde: forma modal del techo, amplificada. El modo 1 es traslación en Y; los modos 2 y 3 combinan traslación en X con rotación, la firma del acoplamiento torsional en la dirección corta."));
  }

  /* Daño esperado: barras de rango por componente y escenario */
  function dano(cont) {
    var comp = D.dano.componentes, esc = D.dano.escenarios;
    var W = 640, fila = 58, top = 34, izq = 190, der = 24, maxV = 60;
    var H = top + comp.length * fila + 30;
    var svg = s("svg", { viewBox: "0 0 " + W + " " + H, role: "img", "aria-label": "Daño esperado como fracción del valor de cada componente, para el sismo de diseño y un sismo severo" });
    var xs = function (v) { return izq + v / maxV * (W - izq - der); };
    [0, 10, 20, 30, 40, 50, 60].forEach(function (v) {
      svg.appendChild(s("line", { x1: xs(v), x2: xs(v), y1: top - 8, y2: H - 26, stroke: "#e3e9eb", "stroke-width": 1 }));
      var t = s("text", { x: xs(v), y: H - 8, "font-size": 12, "text-anchor": "middle", fill: "#5f6e75" }); t.textContent = v + " %"; svg.appendChild(t);
    });
    var colores = [GRAFITO, VERDE];
    comp.forEach(function (c, i) {
      var y0 = top + i * fila;
      var t = s("text", { x: izq - 12, y: y0 + 24, "font-size": 13, "text-anchor": "end", fill: GRAFITO }); t.textContent = c; svg.appendChild(t);
      esc.forEach(function (e, j) {
        var r = e.rangos[i], yy = y0 + 8 + j * 20;
        var a = xs(r[0]), b = xs(r[1]);
        var g = s("g", {});
        g.appendChild(s("rect", { x: a, y: yy, width: Math.max(6, b - a), height: 12, rx: 4, fill: colores[j] }));
        var lab = s("text", { x: Math.max(a, b) + 8, y: yy + 10.5, "font-size": 12, fill: "#4b5a62" }); lab.textContent = r[0] + " a " + r[1] + " %";
        g.appendChild(lab);
        g.appendChild(s("rect", { x: a - 6, y: yy - 4, width: Math.max(18, b - a + 12), height: 20, fill: "transparent" }));
        conTip(g, "<strong>" + c + "</strong>" + e.nombre + ": " + r[0] + " a " + r[1] + " % del valor del componente");
        svg.appendChild(g);
      });
    });
    var ley = el("div", { class: "bandas-leyenda", style: "margin-bottom:8px" },
      esc.map(function (e, j) { return "<span><span class=\"muestra\" style=\"background:" + colores[j] + "\"></span>" + e.nombre + "</span>"; }).join(""));
    var fig = el("figure", { class: "figura" });
    fig.appendChild(ley); fig.appendChild(svg);
    fig.appendChild(el("figcaption", null, "Referencia HAZUS sin calibrar con siniestros chilenos, calibración en curso. El rango va de la dirección menos a la más exigida. La cifra por aceleración es la menos confiable."));
    cont.appendChild(fig);
  }

  var FIG = { semaforo: semaforo, bandas: bandas, tabla: tabla, plantas: plantas, iso: iso, modos: modos, dano: dano };
  Array.prototype.forEach.call(document.querySelectorAll("[data-figura]"), function (nodo) {
    var f = FIG[nodo.getAttribute("data-figura")];
    if (f) { nodo.innerHTML = ""; f(nodo); }
  });
})();
