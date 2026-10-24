"""Construye el sitio estático de antesismo en la raíz del repositorio.

Uso, desde cualquier carpeta:
    python fuente/construir.py

Lee los datos anonimizados del caso demostrativo en fuente/datos/ y escribe las
páginas index.html, assets/js/datos-caso.js, sitemap.xml, robots.txt y
staticwebapp.config.json. Las páginas comparten encabezado, pie y crédito.

REVISION = True marca el sitio como versión de revisión con un aviso visible; OCULTO = True pone noindex
y robots.txt cerrado. Ponlo en False al publicar en antesismo.bdl.cl.
VERSION se agrega a los enlaces de css y js; súbela en cada cambio de estilos.
"""

from __future__ import annotations

import json
from pathlib import Path

import ilustraciones as I
import legal as L

REVISION = True
OCULTO = True   # noindex para buscadores y bloqueo de rastreadores de IA, hasta que Rodney avise
CORREO = "rbellido@bdl.cl"
ROBOTS_META = "noindex, nofollow, noarchive, nosnippet, noimageindex, noai, noimageai"
# Rastreadores de buscadores e IA bloqueados de forma explícita en robots.txt
BOTS_IA = [
    "GPTBot", "ChatGPT-User", "OAI-SearchBot", "ClaudeBot", "Claude-User", "Claude-SearchBot", "anthropic-ai",
    "Google-Extended", "GoogleOther", "Applebot-Extended", "PerplexityBot", "Perplexity-User", "CCBot",
    "Bytespider", "Amazonbot", "meta-externalagent", "FacebookBot", "cohere-ai", "Diffbot", "YouBot",
    "DuckAssistBot", "MistralAI-User", "AI2Bot", "Timpibot", "ImagesiftBot", "Omgilibot",
    "Googlebot", "Bingbot", "Applebot", "YandexBot", "Baiduspider", "DuckDuckBot",
]
VERSION = "1.1.0"
DOMINIO = "https://antesismo.bdl.cl"
RAIZ = Path(__file__).resolve().parents[1]
DATOS = Path(__file__).resolve().parent / "datos"
IEC = "https://www.iec.cl"

perfil = json.loads((DATOS / "perfil21.json").read_text(encoding="utf-8"))
geometria = json.loads((DATOS / "geometria.json").read_text(encoding="utf-8"))

# Daño esperado del caso, referencia HAZUS sin calibrar (informe del 22-10-2026)
DANO = {
    "componentes": ["Estructural", "Secundario por deriva", "Secundario por aceleración", "Contenidos"],
    "escenarios": [
        {"nombre": "Sismo de diseño, zona 2, Ao 0,30 g, suelo B", "rangos": [[3, 4], [3, 4], [30, 41], [19, 25]]},
        {"nombre": "Sismo severo, Ao 0,40 g, suelo B", "rangos": [[4, 6], [4, 6], [44, 57], [26, 32]]},
    ],
}

LECTURAS = sum(1 for it in perfil for c in (it["cx"], it["cy"]))
FUERA = [it for it in perfil if "fuera" in (it["cx"], it["cy"])]
N_FUERA = len(FUERA)
N_NORMAL = sum((it["cx"] == "normal") + (it["cy"] == "normal") for it in perfil)
N_ACEPT = sum((it["cx"] == "aceptable") + (it["cy"] == "aceptable") for it in perfil)
N_FUERA_LECT = LECTURAS - N_NORMAL - N_ACEPT


def num(v: float, dec: int = 1) -> str:
    return f"{v:.{dec}f}".replace(".", ",")


def ind(n: int) -> dict:
    return next(it for it in perfil if it["n"] == n)


# Navegación principal: (ruta, texto)
NAV = [
    ("/due-diligence/", "Due diligence"),
    ("/tasadoras/", "Tasadoras"),
    ("/caso/", "Caso"),
    ("/perfil-bio-sismico/", "Método"),
    ("/parametros-sismicos/", "Cómo funciona"),
    ("/precios/", "Precios"),
    ("/validadores/", "Validadores"),
    ("/quien-esta-detras/", "Quién firma"),
]

def cotizar(asunto: str) -> str:
    return f'mailto:{CORREO}?subject=' + asunto.replace(" ", "%20")

DESCRIPTOR = "antesismo, basado en el Perfil Bío-Sísmico 3.0 de IEC Ingeniería"
CREDITO_LARGO = (
    "Metodología: Perfil Bío-Sísmico de Edificios, creado por Tomás Guendelman (IEC Ingeniería S.A.) con Mario Guendelman "
    "y Jorge Lindenberg en 1997, ampliado en 2010 y actualizado en 2017 con Francisco Medina y Luis Figueroa. "
    "El programa original en Fortran lo facilitó Vladimir Mardones, quien trabajó con Tomás Guendelman. "
    "antesismo es una capa de uso sobre un método público y no es un sitio de IEC Ingeniería. "
    "Sus resultados no son revisión estructural ni certificación de cumplimiento normativo."
)


def cabeza(p: dict) -> str:
    url = DOMINIO + p["ruta"]
    robots = f'<meta name="robots" content="{ROBOTS_META}">\n<meta name="googlebot" content="{ROBOTS_META}">\n' if OCULTO else ""
    ld = json.dumps(p["ld"], ensure_ascii=False)
    return f"""<!doctype html>
<html lang="es-CL">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{p['titulo']}</title>
<meta name="description" content="{p['descripcion']}">
{robots}<link rel="canonical" href="{url}">
<meta name="theme-color" content="#263036">
<link rel="icon" href="/favicon.ico" sizes="16x16 24x24 32x32 48x48 64x64 128x128 256x256">
<link rel="icon" href="/favicon-48x48.png" type="image/png" sizes="48x48">
<link rel="icon" href="/favicon.svg" type="image/svg+xml" sizes="any">
<link rel="apple-touch-icon" href="/apple-touch-icon.png" sizes="180x180">
<link rel="mask-icon" href="/safari-pinned-tab.svg" color="#297e7a">
<link rel="manifest" href="/site.webmanifest">
<link rel="stylesheet" href="/assets/marca/antesismo.css">
<link rel="stylesheet" href="/assets/css/sitio.css?v={VERSION}">
<meta property="og:site_name" content="antesismo">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_CL">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{p['titulo']}">
<meta property="og:description" content="{p['descripcion']}">
<meta property="og:image" content="{DOMINIO}/assets/social/antesismo_og_1200x630.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="antesismo, evaluación sísmica de edificios desde planos de recepción municipal">
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">{ld}</script>
</head>"""


def encabezado(ruta: str) -> str:
    actual = ' aria-current="page"'
    enlaces = "\n".join(f'<a href="{r}"{actual if r == ruta else ""}>{t}</a>' for r, t in NAV)
    aviso = ('<div class="aviso-revision">Versión de revisión, oculta a buscadores y a rastreadores de IA; '
             'no es todavía el sitio público.</div>\n') if REVISION else ""
    return f"""<body>
<a class="salto" href="#contenido">Saltar al contenido</a>
{aviso}<header class="encabezado">
<div class="contenedor">
<a class="marca-logo" href="/" aria-label="antesismo, inicio"><img src="/assets/marca/antesismo_isologo_horizontal_color.svg" alt="antesismo" width="240" height="46"></a>
<button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav-principal">
<svg width="18" height="18" viewBox="0 0 18 18" aria-hidden="true"><path d="M2 4h14M2 9h14M2 14h14" stroke="currentColor" stroke-width="2"/></svg>Menú</button>
<nav class="nav" id="nav-principal" aria-label="Principal">
{enlaces}
<a class="boton" href="/due-diligence/#solicitar">Solicitar informe</a>
</nav>
</div>
</header>
<main id="contenido">"""


def pie(datos: bool) -> str:
    enlaces = "\n".join(f'<a href="{r}">{t}</a>' for r, t in [("/", "Inicio")] + NAV
                        + [("/legal/#terminos", "Términos de uso"), ("/legal/#privacidad", "Política de privacidad")])
    scripts = f'<script src="/assets/js/datos-caso.js?v={VERSION}"></script>\n<script src="/assets/js/perfil.js?v={VERSION}"></script>\n' if datos else ""
    return f"""</main>
<section class="credito" aria-labelledby="credito-t">
<div class="contenedor">
<h2 id="credito-t">Crédito y atribución</h2>
<p class="descriptor">{DESCRIPTOR}.</p>
<p class="mb-0">{CREDITO_LARGO} <a href="/perfil-bio-sismico/">Lee el método y su crédito completo</a>.</p>
</div>
</section>
<footer class="pie">
<div class="contenedor">
<div>
<img src="/assets/marca/antesismo_isologo_horizontal_blanco.svg" alt="antesismo" width="220" height="42">
<p>Due diligence sísmico en días, desde los planos municipales.</p>
<p>Ing. Rodney Bellido de Luna<br><a href="mailto:{CORREO}">{CORREO}</a></p>
</div>
<nav aria-label="Pie de página">
{enlaces}
</nav>
<p class="final">antesismo.bdl.cl · Proyecto de Rodney Bellido de Luna, ingeniero civil en obras civiles · <a href="mailto:{CORREO}">{CORREO}</a> · Cada resultado lleva la leyenda: no es revisión estructural ni certificación de cumplimiento normativo.</p>
</div>
</footer>
<script src="/assets/js/sitio.js?v={VERSION}"></script>
{scripts}</body>
</html>
"""


def formulario(ident: str, titulo: str, campos: str, boton: str) -> str:
    return f"""<form class="formulario panel-blanco" id="{ident}-form" data-correo="{CORREO}" data-asunto="{titulo}" aria-labelledby="{ident}-t" novalidate>
<h3 id="{ident}-t" class="mt-0">{titulo}</h3>
{campos}
<button class="boton" type="submit">{boton}</button>
<p class="nota mb-0">Sin pago y sin compromiso. Al enviar se abre tu programa de correo con el mensaje listo para {CORREO}; este sitio no guarda tus datos. Lee la <a href="/legal/#privacidad">política de privacidad</a>.</p>
<div class="form-estado" role="status" tabindex="-1"></div>
</form>"""


def campo(nombre: str, etiqueta: str, tipo: str = "text", extra: str = "") -> str:
    if tipo == "textarea":
        return f'<label>{etiqueta}<textarea name="{nombre}" {extra}></textarea></label>'
    return f'<label>{etiqueta}<input type="{tipo}" name="{nombre}" {extra}></label>'


def ld_servicio(nombre: str, desc: str, ruta: str) -> dict:
    return {
        "@context": "https://schema.org", "@type": "Service", "name": nombre, "description": desc,
        "url": DOMINIO + ruta, "areaServed": {"@type": "Country", "name": "Chile"},
        "provider": {"@type": "Organization", "name": "antesismo", "url": DOMINIO + "/"},
    }


def ld_articulo(titulo: str, desc: str, ruta: str) -> dict:
    return {
        "@context": "https://schema.org", "@type": "Article", "headline": titulo, "description": desc,
        "inLanguage": "es-CL", "url": DOMINIO + ruta, "dateModified": "2026-10-24",
        "author": {"@type": "Person", "name": "Rodney Bellido de Luna"},
        "publisher": {"@type": "Organization", "name": "antesismo"},
    }


LEYENDA = '<p class="leyenda">Cada resultado de antesismo lleva esta leyenda: no es revisión estructural ni certificación de cumplimiento normativo. El perfil mide la estructuración del edificio y la compara con edificios chilenos que funcionaron bien en terremotos reales.</p>'

# Valores del caso usados en varias páginas
i7, i17, i21 = ind(7), ind(17), ind(21)
T1, T2, T3 = (m["T"] for m in geometria["modos"])
FUERA_TXT = "; ".join(
    f"indicador {it['n']}, {it['nombre'].split(',')[-1].strip()}, en "
    + ("X e Y" if it["cx"] == it["cy"] == "fuera" else ("X" if it["cx"] == "fuera" else "Y"))
    for it in FUERA
)

FILAS_DANO = "".join(
    f"<tr><td>{e['nombre']}</td>" + "".join(f'<td class="num">{a} a {b} %</td>' for a, b in e["rangos"]) + "</tr>"
    for e in DANO["escenarios"]
)
TABLA_DANO = f"""<div class="tabla-envoltura"><table>
<caption class="visual-oculto">Daño esperado como fracción del valor de cada componente</caption>
<thead><tr><th>Escenario</th><th class="num">Estructural</th><th class="num">Secundario por deriva</th><th class="num">Secundario por aceleración</th><th class="num">Contenidos</th></tr></thead>
<tbody>{FILAS_DANO}</tbody></table></div>"""

paginas: list[dict] = []

# ---------------------------------------------------------------- Inicio
paginas.append({
    "ruta": "/",
    "titulo": "antesismo, due diligence sísmico en días, desde los planos municipales",
    "descripcion": "Con los planos de recepción municipal obtienes los 21 indicadores del perfil bío-sísmico, el daño esperado para el próximo terremoto y un informe firmado por un ingeniero civil. Sin modelo de cálculo.",
    "ld": ld_servicio("Due diligence sísmico de edificios", "Perfil bío-sísmico, daño esperado e informe firmado desde los planos municipales.", "/"),
    "datos": True,
    "cuerpo": f"""
<section class="heroe">
<div class="contenedor rejilla">
<div>
<span class="etiqueta">antesismo, due diligence sísmico en días, desde los planos municipales</span>
<h1>¿La estructuración de tu edificio está dentro de lo que ha funcionado bien en terremotos reales?</h1>
<p class="intro">Con la dirección o el expediente municipal, que es público, obtienes los 21 indicadores del perfil bío-sísmico con semáforo, el daño esperado para el próximo terremoto y un informe firmado por un ingeniero civil. Sin modelo de cálculo y sin pedirle nada al dueño.</p>
<div class="botones">
<a class="boton" href="/due-diligence/">Pide un informe firmado</a>
<a class="boton-sec" href="/tasadoras/">Conecta tu plataforma de tasación</a>
<a class="boton-sec" href="/precios/#piloto">Piloto para aseguradoras</a>
</div>
<ul class="segmentos" aria-label="Para quién">
<li>Due diligence inmobiliario</li><li>Tasadoras con IA y proptech</li><li>Aseguradoras</li><li>Fondos y bancos</li>
</ul>
</div>
<div>
<div data-figura="semaforo"><p class="pequeño">El semáforo de 21 indicadores necesita JavaScript. <a href="/caso/">Ver el caso demostrativo</a>.</p></div>
<p class="pequeño" style="margin-top:10px">Edificio de 1963, 5 pisos, Providencia, calculado desde los planos municipales. <a href="/caso/">Ver caso demostrativo</a>.</p>
</div>
</div>
</section>

<section class="seccion">
<div class="contenedor">
<div class="seccion-cabeza">
<h2>Lo que no encontrarás en una planilla del perfil</h2>
<p>El método es público y cualquiera lo puede calcular si tiene el modelo del edificio. Lo que tú necesitas es aplicarlo a un edificio del que nadie tiene el modelo, con una firma que responde.</p>
</div>
<div class="rejilla-4">
<div class="tarjeta">{I.ICONO_PLANOS}<h3>Planos municipales públicos</h3><p>Los expedientes de permisos de edificación son públicos (CPLT, Oficio 16622, julio de 2025). Transcribimos los muros con vista asistida y calculamos sin modelo de análisis.</p></div>
<div class="tarjeta">{I.ICONO_FIRMA}<h3>Informe firmado</h3><p>Un ingeniero civil revisa, firma y responde. El informe separa los controles globales del detallamiento de obra nueva, que no es retroactivo.</p></div>
<div class="tarjeta">{I.ICONO_DANO}<h3>Daño esperado para el próximo terremoto</h3><p>Estructural, secundario y contenidos, para el sismo de diseño y uno severo. Hoy es referencia HAZUS; se calibra con siniestros reales.</p></div>
<div class="tarjeta">{I.ICONO_CONECTA}<h3>Conecta y usa</h3><p>Para tasadoras y proptech, una llamada por dirección y el riesgo sísmico entra como un campo más de la tasación. Hoy en lista de espera.</p></div>
</div>
</div>
</section>

<section class="seccion suave">
<div class="contenedor">
<div class="seccion-cabeza"><h2>Cómo funciona</h2><p>Del expediente al informe en cuatro a siete días.</p></div>
<ol class="pasos">
<li><h3>Entrega la dirección</h3><p>Subes el expediente municipal o lo pedimos por transparencia con tu mandato.</p></li>
<li><h3>Transcribimos los muros</h3><p>Sobre el plano escaneado, con ayuda de IA y validación de una persona, piso por piso.</p></li>
<li><h3>Calculamos</h3><p>Modelo de piso rígido, 21 indicadores, controles globales de norma y daño esperado.</p></li>
<li><h3>Revisión y firma</h3><p>El ingeniero revisa, firma y te entrega el informe en Word y PDF.</p></li>
</ol>
<p style="margin-top:20px"><a href="/parametros-sismicos/">Cómo se obtienen los parámetros sísmicos desde los planos</a></p>
</div>
</section>

<section class="seccion">
<div class="contenedor dos-col">
<div>
<span class="etiqueta gris">Caso demostrativo</span>
<h2>Antes de firmar, sabe cómo se comportará el edificio en el próximo sismo</h2>
<p class="intro">En el edificio de 1963 del caso demostrativo, el daño estructural esperado es bajo incluso para un sismo severo. El riesgo económico está en los elementos secundarios y los contenidos, que sufren las aceleraciones altas de un edificio rígido.</p>
<p>Ese es el tipo de lectura que necesita quien compra, tasa o asegura: no solo si la estructura es sana, también dónde está la pérdida.</p>
<a class="boton-sec" href="/caso/">Ver el caso completo</a>
</div>
<div data-figura="dano">{TABLA_DANO}</div>
</div>
</section>

<section class="seccion oscura">
<div class="contenedor dos-col">
<div>
<h2>Quién está detrás</h2>
<p>antesismo lo desarrolla y lo firma el Ing. Rodney Bellido de Luna, ingeniero civil en obras civiles de la Universidad Central de Chile. Revisa cada inventario de muros, cada supuesto y cada resultado, y responde por su trabajo profesional.</p>
<p class="mb-0"><a href="/quien-esta-detras/">Biografía y responsabilidad</a> · <a href="mailto:{CORREO}">{CORREO}</a></p>
</div>
<div>
<h3>Crédito abierto</h3>
<p class="mb-0">El método es el Perfil Bío-Sísmico de Edificios de Tomás Guendelman e IEC Ingeniería. antesismo lo aplica con crédito directo a sus autores, desde los planos municipales.</p>
</div>
</div>
</section>

<section class="seccion suave">
<div class="contenedor">
<div class="seccion-cabeza"><h2>Para quién es</h2></div>
<div class="rejilla-2">
<div class="tarjeta"><h3>Due diligence inmobiliario</h3><p>Abogados, fondos y compradores de edificios. Antes de comprar, sabe cuánto daño esperar en el próximo sismo.</p><p style="margin-top:14px"><a href="/due-diligence/">Ver el servicio</a></p></div>
<div class="tarjeta"><h3>Tasadoras con IA, proptech y bancos</h3><p>Agrega el riesgo sísmico del edificio a cada tasación, con una llamada.</p><p style="margin-top:14px"><a href="/tasadoras/">Ver el conector</a></p></div>
<div class="tarjeta"><h3>Aseguradoras y reaseguro</h3><p>Un dato de riesgo por edificio para suscripción, con un piloto que calibra el daño con tus siniestros.</p><p style="margin-top:14px"><a href="/precios/#piloto">Conversar un piloto</a></p></div>
<div class="tarjeta"><h3>Oficinas de cálculo y academia</h3><p>Reproduce el caso, revisa el método y dinos si algo no cuadra. Las discrepancias se publican con su respuesta.</p><p style="margin-top:14px"><a href="/validadores/">Ir a validadores</a></p></div>
</div>
{LEYENDA}
</div>
</section>
""",
})

# ---------------------------------------------------------------- Due diligence
CAMPOS_INFORME = (
    '<div class="doble">' + campo("nombre", "Nombre", extra='autocomplete="name" required') + campo("correo", "Correo", "email", 'autocomplete="email" required') + "</div>"
    + '<div class="doble">' + campo("empresa", "Empresa o estudio", extra='autocomplete="organization"')
    + '<label>Tipo de operación<select name="operacion"><option>Compra de un edificio</option><option>Due diligence de cartera</option><option>Financiamiento o garantía</option><option>Otra</option></select></label></div>'
    + campo("direccion", "Dirección y comuna del edificio", extra='required')
    + campo("mensaje", "Plazo y lo que necesitas saber", "textarea")
)
paginas.append({
    "ruta": "/due-diligence/",
    "titulo": "Due diligence sísmico de edificios desde los planos municipales | antesismo",
    "descripcion": "Antes de comprar, sabe cuánto daño esperar en el próximo sismo. Informe firmado en días con los 21 indicadores del perfil bío-sísmico y daño esperado, desde el expediente municipal.",
    "ld": ld_servicio("Due diligence sísmico de edificios", "Informe firmado con perfil bío-sísmico y daño esperado, desde los planos municipales.", "/due-diligence/"),
    "datos": False,
    "cuerpo": f"""
<section class="heroe">
<div class="contenedor rejilla">
<div>
<span class="etiqueta">Abogados, fondos inmobiliarios y compradores de edificios</span>
<h1>Antes de comprar, sabe cuánto daño esperar en el próximo sismo</h1>
<p class="intro">El due diligence sísmico de un edificio, hecho con solo los planos del expediente municipal y sin acceso al modelo de cálculo del proyecto original. Recibes un informe de salud estructural con firma profesional, en días y a una fracción del costo de una revisión de consultora.</p>
<div class="botones"><a class="boton" href="#solicitar">Solicitar informe de due diligence</a><a class="boton-sec" href="/caso/">Ver un caso</a></div>
</div>
<div class="ilustracion">{I.ESCENA}</div>
</div>
</section>

<section class="seccion">
<div class="contenedor dos-col">
<div>
<h2>Qué recibes</h2>
<ul class="lista-check">
<li>Los 21 indicadores del perfil bío-sísmico con semáforo, comparados con 4.105 edificios chilenos.</li>
<li>Controles globales de la NCh433 separados del detallamiento de obra nueva, que no es retroactivo.</li>
<li>Daño esperado para el próximo terremoto: estructural, secundario y contenidos. Es referencia y su calibración está en curso.</li>
<li>Plantas, modelo 3D y formas modales del edificio, para que veas lo que se calculó.</li>
<li>Firma del Ing. Rodney Bellido de Luna, ingeniero civil en obras civiles.</li>
<li>Informe en Word y PDF, con el crédito a los creadores del método.</li>
</ul>
</div>
<div class="panel">
<h3 class="mt-0">Flujo del servicio</h3>
<ol class="linea">
<li><span class="dia">Día 0</span><p>Envías el expediente municipal, o lo pedimos por transparencia con tu mandato.</p></li>
<li><span class="dia">Día 1 a 3</span><p>Transcripción asistida de muros por piso. Te mostramos el inventario para validar.</p></li>
<li><span class="dia">Día 3</span><p>Cálculo: modelo de piso rígido, 21 indicadores, controles de norma y factores de daño de referencia.</p></li>
<li><span class="dia">Día 4 a 7</span><p>Revisión y firma del ingeniero, informe final con daño esperado y reunión de lectura de 30 minutos.</p></li>
</ol>
<p class="pequeño mb-0" style="margin-top:12px">Precio por edificio y operación: <a href="{cotizar('Cotización informe de due diligence')}">Enviar email por cotizar</a>.</p>
</div>
</div>
</section>

<section class="seccion suave">
<div class="contenedor">
<div class="seccion-cabeza"><h2>Preguntas que nos hacen</h2></div>
<div class="preguntas">
<details open><summary>¿Quién firma?</summary><div><p>El Ing. Rodney Bellido de Luna, ingeniero civil en obras civiles de la Universidad Central de Chile. Revisa el inventario de muros y el resultado, y firma el informe bajo su responsabilidad profesional. <a href="/quien-esta-detras/">Conoce quién está detrás de antesismo</a>.</p></div></details>
<details><summary>¿Es un certificado de cumplimiento?</summary><div><p>No. Es un informe de salud estructural. Un edificio de 1963 puede cumplir con holgura los controles globales y no cumplir el detallamiento exigido hoy a la obra nueva, y el informe lo dice así. La norma no es retroactiva y el perfil mide la estructuración, no el cumplimiento.</p></div></details>
<details><summary>¿Necesito el modelo de cálculo del proyecto?</summary><div><p>No. Basta el expediente municipal, que es público. Si tienes el modelo de cálculo, el trabajo es más rápido.</p></div></details>
<details><summary>¿Qué edificios pueden evaluarse?</summary><div><p>Los rangos del perfil están calibrados con edificios chilenos de hormigón armado, en especial los estructurados con muros. Para otras tipologías, cuéntanos el caso antes de reservar.</p></div></details>
<details><summary>¿Qué pasa con los datos del propietario?</summary><div><p>El perfil es del edificio, no de la persona. No cruzamos rol ni póliza, y los planos se borran después de un plazo definido salvo que pidas conservar el proyecto.</p></div></details>
</div>
</div>
</section>

<section class="seccion" id="solicitar">
<div class="contenedor dos-col">
<div>
<h2>Solicita un informe</h2>
<p class="intro">Cuéntanos qué edificio y para qué operación. Te respondemos con el alcance, el plazo y si el expediente disponible alcanza.</p>
{LEYENDA}
</div>
{formulario("informe", "Datos del edificio", CAMPOS_INFORME, "Solicitar informe")}
</div>
</section>
""",
})

# ---------------------------------------------------------------- Tasadoras
filas_ficha = "".join(
    f"<tr><td>{e['nombre'].split(',')[0]}</td>" + "".join(f'<td class="num">{a} a {b} %</td>' for a, b in e["rangos"]) + "</tr>"
    for e in DANO["escenarios"]
)
CAMPOS_ESPERA = (
    '<div class="doble">' + campo("nombre", "Nombre", extra='autocomplete="name" required') + campo("correo", "Correo", "email", 'autocomplete="email" required') + "</div>"
    + '<div class="doble">' + campo("empresa", "Empresa o plataforma", extra='autocomplete="organization" required')
    + campo("volumen", "Direcciones al mes, aproximado", "number", 'min="0" inputmode="numeric"') + "</div>"
    + campo("comunas", "Comunas o ciudades por las que te interesa partir")
    + campo("mensaje", "Cómo usarías el dato", "textarea")
)
paginas.append({
    "ruta": "/tasadoras/",
    "titulo": "Riesgo sísmico en la tasación, conector para tasadoras y proptech | antesismo",
    "descripcion": "Agrega el riesgo sísmico del edificio a cada tasación, con una llamada. Perfil bío-sísmico y daño esperado por dirección, para tasadoras con IA, proptech y bancos.",
    "ld": ld_servicio("Conector de riesgo sísmico para tasación", "Perfil bío-sísmico y daño esperado por dirección, por API.", "/tasadoras/"),
    "datos": False,
    "cuerpo": f"""
<section class="heroe">
<div class="contenedor rejilla">
<div>
<span class="etiqueta">Tasadoras con IA, proptech y bancos hipotecarios</span>
<h1>Agrega el riesgo sísmico del edificio a cada tasación, con una llamada</h1>
<p class="intro">Hoy el valor de un departamento no sabe nada del edificio que lo sostiene. Con la dirección, el conector devuelve el perfil sísmico del edificio y el daño esperado para el próximo terremoto, como un campo más de tu tasación o de tu ficha de propiedad.</p>
<div class="botones"><a class="boton" href="#lista">Unirse a la lista de espera</a><a class="boton-sec" href="#conecta">Cómo se conecta</a></div>
</div>
<div class="ilustracion">{I.CONECTOR}</div>
</div>
</section>

<section class="seccion">
<div class="contenedor dos-col">
<div>
<h2>Qué devuelve el conector</h2>
<ul class="lista-check">
<li>Los 21 indicadores del perfil bío-sísmico por dirección, con su calificación.</li>
<li>Daño esperado para el sismo de diseño y para un sismo severo: estructural, secundario y contenidos, como rango y no como cifra exacta.</li>
<li>Año, pisos, sistema estructural y material, leídos del expediente municipal.</li>
<li>Trazabilidad: qué plano se usó, quién validó el inventario y qué versión de rangos se aplicó.</li>
<li>PDF firmado opcional por edificio, para el expediente del crédito o la venta.</li>
</ul>
<h3 style="margin-top:28px">Cobertura, dicho claro</h3>
<p class="pequeño" style="font-size:.95rem">Hoy cada dirección nueva se evalúa bajo pedido, en días, porque la transcripción de muros la asiste una persona. Las direcciones ya evaluadas responden al instante. La cobertura masiva llega con la transcripción automática; si tasas miles de direcciones, entra a la lista de espera y define con nosotros las comunas por las que partimos.</p>
</div>
<div class="panel">
<p class="pequeño mt-0" style="margin-bottom:10px">Así se vería dentro de tu tasación</p>
<div class="ficha">
<div class="meta">Informe de tasación · Depto. de ejemplo · Caso demostrativo</div>
<h3>Riesgo sísmico del edificio <span class="etiqueta gris" style="margin:0">{N_FUERA} de 21 indicadores con lectura fuera de rango</span></h3>
<p class="sub">Edificio de 1963 · 5 pisos · muros de hormigón armado · Providencia</p>
<p style="font-size:.86rem;font-weight:600;margin-bottom:6px">Daño esperado, fracción del valor de cada componente</p>
<div class="tabla-envoltura"><table>
<thead><tr><th>Escenario</th><th class="num">Estructural</th><th class="num">Secund. deriva</th><th class="num">Secund. aceleración</th><th class="num">Contenidos</th></tr></thead>
<tbody>{filas_ficha}</tbody></table></div>
<p class="pequeño" style="margin:10px 0 6px">Referencia HAZUS sin calibrar con siniestros chilenos, calibración en curso. Lectura: estructura rígida con daño estructural bajo; el riesgo económico está en los elementos secundarios y los contenidos.</p>
<p class="pequeño" style="margin:0 0 6px">Fuera de rango: {FUERA_TXT}.</p>
<p class="pequeño mb-0">Fuente: expediente municipal, cuatro planos. {DESCRIPTOR}. No es revisión estructural ni certificación.</p>
</div>
</div>
</div>
</section>

<section class="seccion suave" id="conecta">
<div class="contenedor">
<div class="seccion-cabeza"><h2>Cómo se conecta</h2><p>El conector está en piloto. El formato de la respuesta se acuerda con los primeros clientes; este es el borrador.</p></div>
<ol class="pasos">
<li><h3>Llave de API</h3><p>Una llave por cliente y un entorno de prueba con el caso demostrativo.</p></li>
<li><h3>Una llamada por dirección</h3><p>Envías dirección o rol; recibes el perfil, el daño esperado y el estado: listo, en evaluación o sin expediente.</p></li>
<li><h3>Muestra el resultado</h3><p>Un campo en tu tasación o tu ficha, con el crédito al método y la leyenda de no certificación.</p></li>
<li><h3>PDF firmado cuando haga falta</h3><p>Para el expediente del crédito o la venta, pides el informe firmado del edificio.</p></li>
</ol>
<pre class="codigo" style="margin-top:20px" aria-label="Ejemplo ilustrativo de llamada al conector"><span class="c"># Borrador ilustrativo, el contrato final se define en el piloto</span>
<span class="k">GET</span> /v1/edificios?direccion=<span class="s">"..."</span>

{{
  <span class="s">"estado"</span>: <span class="s">"listo"</span>,
  <span class="s">"indicadores"</span>: [ ... 21 por dirección X e Y ... ],
  <span class="s">"fuera_de_rango"</span>: {N_FUERA},
  <span class="s">"dano_esperado"</span>: {{ <span class="s">"diseno"</span>: {{ ... rangos ... }}, <span class="s">"severo"</span>: {{ ... }} }},
  <span class="s">"fuente"</span>: {{ <span class="s">"planos"</span>: 4, <span class="s">"inventario_validado_por"</span>: <span class="s">"..."</span> }},
  <span class="s">"pdf_firmado_url"</span>: <span class="k">null</span>
}}</pre>
</div>
</section>

<section class="seccion" id="lista">
<div class="contenedor dos-col">
<div>
<h2>Únete a la lista de espera</h2>
<p class="intro">Dinos cuántas direcciones tasas al mes y en qué comunas. Con eso armamos la cobertura del piloto.</p>
{LEYENDA}
</div>
{formulario("espera", "Lista de espera del conector", CAMPOS_ESPERA, "Unirme a la lista de espera")}
</div>
</section>
""",
})

# ---------------------------------------------------------------- Caso demostrativo
paginas.append({
    "ruta": "/caso/",
    "titulo": "Caso demostrativo: parámetros sísmicos de un edificio de 1963 desde los planos municipales | antesismo",
    "descripcion": "Edificio de 1963, 5 pisos, muros de hormigón armado, Providencia: 21 indicadores del perfil bío-sísmico, modos y daño esperado, calculados desde cuatro planos escaneados del expediente municipal.",
    "ld": ld_articulo("Caso demostrativo: edificio de 1963 desde los planos municipales", "Perfil bío-sísmico de 21 indicadores y daño esperado de un edificio de muros de hormigón armado.", "/caso/"),
    "datos": True,
    "cuerpo": f"""
<section class="heroe">
<div class="contenedor">
<span class="etiqueta">Caso demostrativo, datos del edificio anonimizados</span>
<h1>Edificio de 1963, 5 pisos, muros de hormigón armado, Providencia</h1>
<p class="intro">Calculado de punta a punta desde cuatro planos escaneados del expediente municipal: inventario de muros, modelo de piso rígido, 21 indicadores del perfil bío-sísmico, controles globales de norma y factores de daño de referencia. Sin modelo de cálculo original.</p>
<div class="rejilla-4" style="margin-top:28px">
<div class="tarjeta"><p class="pequeño mt-0" style="margin-bottom:4px">Períodos de los tres primeros modos</p><h3 class="mb-0">{num(T1, 3)} · {num(T2, 3)} · {num(T3, 3)} s</h3></div>
<div class="tarjeta"><p class="pequeño mt-0" style="margin-bottom:4px">Desplazamiento agrietado de techo</p><h3 class="mb-0">{num(i7['X'])} y {num(i7['Y'])} por mil</h3><p style="font-size:.82rem">X e Y; normal hasta 10 por mil</p></div>
<div class="tarjeta"><p class="pequeño mt-0" style="margin-bottom:4px">Densidad de muros, corte</p><h3 class="mb-0">{num(i21['X'])} y {num(i21['Y'])} %</h3><p style="font-size:.82rem">X e Y, peor piso; mínimo 2 %</p></div>
<div class="tarjeta"><p class="pequeño mt-0" style="margin-bottom:4px">Lecturas del perfil</p><h3 class="mb-0">{N_NORMAL} normal · {N_ACEPT} aceptable · {N_FUERA_LECT} fuera</h3><p style="font-size:.82rem">de {LECTURAS}, 21 indicadores en X e Y</p></div>
</div>
</div>
</section>

<section class="seccion">
<div class="contenedor">
<div class="seccion-cabeza"><h2>1. Plantas transcritas desde el plano</h2><p>Los muros se leyeron de las cotas del plano cuando existían y se estimaron sobre el dibujo a escala cuando no. La incertidumbre estimada es de más o menos 15 % en el largo total por dirección.</p></div>
<div data-figura="plantas"><p class="pequeño">Las plantas se dibujan con JavaScript.</p></div>
</div>
</section>

<section class="seccion suave">
<div class="contenedor dos-col">
<div>
<h2>2. Modelo de muros y diafragmas</h2>
<p>Cada muro trabaja como un voladizo de flexión y corte, y cada losa como un diafragma rígido con tres grados de libertad por piso. El solver de piso rígido coincide con OpenSees a 1e-6 en las pruebas.</p>
<ul class="lista-check">
<li>Hormigón con módulo de 17.000 MPa, desde la resistencia indicada en el plano.</li>
<li>Eje B de hormigón en los pisos 1 a 3 y de albañilería en los pisos 4 y 5, según nota del plano.</li>
<li>Masas desde losas, muros, terminaciones y 25 % de la sobrecarga habitacional.</li>
</ul>
</div>
<div data-figura="iso"></div>
</div>
</section>

<section class="seccion">
<div class="contenedor">
<div class="seccion-cabeza"><h2>3. Formas modales y períodos</h2></div>
<div data-figura="modos"></div>
</div>
</section>

<section class="seccion suave">
<div class="contenedor">
<div class="seccion-cabeza">
<h2>4. Perfil bío-sísmico, 21 indicadores con sus bandas</h2>
<p>Cada fila muestra las bandas de la versión 3.0 del perfil y la posición del edificio en X y en Y. Pasa el cursor o el foco por cada marca para ver el valor.</p>
</div>
<div class="panel-blanco"><div data-figura="bandas"><p class="pequeño">El gráfico de bandas necesita JavaScript; abajo está la tabla completa.</p></div></div>
<details style="margin-top:18px"><summary style="cursor:pointer;font-weight:600">Ver los 21 indicadores en tabla</summary><div style="margin-top:12px" data-figura="tabla"></div></details>
</div>
</section>

<section class="seccion">
<div class="contenedor dos-col">
<div>
<h2>5. Daño esperado</h2>
<p>Factores de daño como fracción del valor de cada componente. El rango de cada celda va de la dirección menos a la más exigida. Con la incertidumbre del inventario, el daño estructural de diseño se mueve entre 0,5 y 5,3 %.</p>
{TABLA_DANO}
</div>
<div data-figura="dano"></div>
</div>
</section>

<section class="seccion suave">
<div class="contenedor dos-col">
<div class="panel-blanco">
<h2 class="mt-0">Lectura del resultado</h2>
<p>Es el edificio chileno de muros típico de los años sesenta: rígido, con densidades de muros altas, deriva baja y daño estructural esperado pequeño incluso para un sismo severo.</p>
<p>Su debilidad es la torsión en la dirección corta, por la fachada abierta frente a un muro posterior corrido. Fuera de rango: {FUERA_TXT}. Esa lectura se mantiene al variar los largos de muro en más o menos 15 %: es una propiedad de la planta, no del error de lectura.</p>
<p class="mb-0">El riesgo económico relevante no está en la estructura sino en los elementos secundarios y los contenidos.</p>
</div>
<div>
<h2>Supuestos del caso</h2>
<ul class="lista-no">
<li>Sismo de diseño NCh433 Of96 mod. 2009 más DS61, zona 2 con Ao 0,30 g y suelo tipo B, ambos supuestos; Ro 11, categoría II.</li>
<li>Quinto piso igual al cuarto, porque su planta de armaduras no está en el expediente.</li>
<li>Sin torsión accidental en los desplazamientos de puntos extremos.</li>
<li>Factores de daño de referencia HAZUS, sin calibrar con siniestros chilenos.</li>
</ul>
<h3 style="margin-top:24px">Para validadores</h3>
<p>El paquete para reproducir el cálculo, con la entrada del motor, los resultados y la tabla de 13 frente a 21 indicadores, está en preparación con los datos anonimizados.</p>
<a class="boton-sec" href="/validadores/#contacto">Pedir el paquete del caso</a>
</div>
</div>
<div class="contenedor"><p class="leyenda">Este caso demostrativo no es revisión estructural ni certificación. El edificio y sus propietarios no se identifican.</p></div>
</section>
""",
})

# ---------------------------------------------------------------- Método y crédito
filas_metodo = "".join(
    f"<tr><td>{it['n']}</td><td>{it['nombre']}{' [' + it['unidad'] + ']' if it['unidad'] else ''}</td><td>{it['grupo']}</td></tr>"
    for it in perfil
)
paginas.append({
    "ruta": "/perfil-bio-sismico/",
    "titulo": "Perfil bío-sísmico de edificios: qué es, sus 21 indicadores y su crédito | antesismo",
    "descripcion": "El perfil bío-sísmico de edificios compara la estructuración de un edificio con la de edificios chilenos que funcionaron bien en terremotos reales. Qué es, sus versiones, sus 21 indicadores y el crédito a sus autores.",
    "ld": ld_articulo("Perfil bío-sísmico de edificios: qué es, sus 21 indicadores y su crédito", "Explicación del método de Tomás Guendelman y IEC Ingeniería, sus versiones y sus indicadores.", "/perfil-bio-sismico/"),
    "datos": False,
    "cuerpo": f"""
<section class="heroe">
<div class="contenedor dos-col">
<div>
<span class="etiqueta">Método y crédito</span>
<h1>Perfil bío-sísmico de edificios</h1>
<p class="intro">El perfil bío-sísmico de edificios es un conjunto de indicadores que compara la rigidez, el acoplamiento torsional, la redundancia y la densidad de muros de un edificio con los de edificios chilenos que se comportaron bien en terremotos reales. Lo creó Tomás Guendelman, de IEC Ingeniería, y es un método público.</p>
<p>antesismo lo usa con crédito abierto y directo a sus autores, y lo lleva a edificios de los que nadie tiene el modelo de cálculo, desde los planos municipales.</p>
<div class="botones"><a class="boton-sec" href="{IEC}" rel="noopener">Leer el documento del perfil en iec.cl</a></div>
</div>
<div class="panel-blanco">
<h3 class="mt-0">La promesa, en una frase</h3>
<p class="mb-0">Con los planos de recepción municipal le decimos si la estructura de su edificio está armada con lo que ha funcionado bien en terremotos reales, qué controles globales de la NCh433:2026 cumple y cuánto daño esperar en el próximo terremoto. Sin modelo de cálculo.</p>
<p class="pequeño" style="margin:12px 0 0">Las tablas de la NCh433:2026 se incorporan al motor antes de que sea exigible, en febrero de 2027. El caso demostrativo usa la NCh433 Of96 mod. 2009 más DS61.</p>
</div>
</div>
</section>

<section class="seccion">
<div class="contenedor">
<div class="seccion-cabeza"><h2>Tres versiones del método</h2><p>Los rangos se calibraron con edificios chilenos y con el desempeño observado en los terremotos de 1985 y 2010.</p></div>
<div class="rejilla-3">
<div class="tarjeta"><span class="etiqueta gris">1997</span><h3>Versión original</h3><p>Tomás Guendelman con Mario Guendelman y Jorge Lindenberg. 13 indicadores calibrados con 585 edificios chilenos.</p></div>
<div class="tarjeta"><span class="etiqueta gris">2010</span><h3>Ampliación</h3><p>El método se amplía sobre la base de la versión original.</p></div>
<div class="tarjeta"><span class="etiqueta gris">2017</span><h3>Versión 3.0</h3><p>Con Francisco Medina y Luis Figueroa. 21 indicadores calibrados con 4.105 edificios y rangos recalibrados. Es la referencia vigente y la que usa antesismo.</p></div>
</div>
</div>
</section>

<section class="seccion suave">
<div class="contenedor">
<div class="seccion-cabeza"><h2>Los 21 indicadores</h2><p>Agrupados en rigidez, acoplamiento, redundancia y ductilidad, y densidad de muros. Cada uno se calcula en las dos direcciones del edificio y se califica como normal, aceptable o fuera de rango. Las bandas están en el documento original y en el <a href="/caso/">caso demostrativo</a>.</p></div>
<div class="tabla-envoltura"><table><caption class="visual-oculto">Indicadores del perfil bío-sísmico versión 3.0</caption>
<thead><tr><th>N.º</th><th>Indicador</th><th>Grupo</th></tr></thead><tbody>{filas_metodo}</tbody></table></div>
</div>
</section>

<section class="seccion">
<div class="contenedor dos-col">
<div>
<h2>Lo que esta capa interpreta por su cuenta</h2>
<p>Donde el documento 3.0 no explicita un cálculo, antesismo documenta su criterio para que cualquiera lo revise:</p>
<ul class="lista-check">
<li>Indicador 11: el período traslacional acoplado se toma como el período dominante de la dirección ortogonal.</li>
<li>Indicador 17: la excentricidad dinámica se divide por la altura total, como indica el documento 3.0.</li>
<li>Indicadores 2, 3, 6 y 7: usan la altura sobre el nivel del suelo; sin subterráneos es igual a la altura total.</li>
<li>Indicadores 20 y 21: solo cuentan los muros de hormigón armado y se reporta el peor piso.</li>
</ul>
</div>
<div>
<h2>Lo que el perfil no es</h2>
<ul class="lista-no">
<li>No es revisión estructural ni reemplaza el cálculo de un proyecto.</li>
<li>No certifica cumplimiento normativo de un edificio existente: la norma no es retroactiva y el perfil mide estructuración.</li>
<li>No es un modelo de catástrofe para reaseguro.</li>
<li>No es un producto de IEC Ingeniería ni está avalado por sus autores.</li>
</ul>
</div>
</div>
</section>

<section class="seccion oscura">
<div class="contenedor">
<h2>Crédito completo</h2>
<p style="max-width:860px">La metodología es el Perfil Bío-Sísmico de Edificios, creado por Tomás Guendelman (IEC Ingeniería S.A.) con Mario Guendelman y Jorge Lindenberg en 1997, ampliado en 2010 y actualizado en 2017 con Francisco Medina y Luis Figueroa. El programa original en Fortran lo facilitó Vladimir Mardones, quien trabajó con Tomás Guendelman.</p>
<p style="max-width:860px">Rodney Bellido de Luna no es autor del método. Su labor es llevar una metodología pública a una capa de uso, con un motor que facilita aplicarla desde planos públicos de las municipalidades o desde modelos BIM privados, y un modelador de código abierto.</p>
<p class="mb-0"><a href="{IEC}" rel="noopener">IEC Ingeniería, iec.cl</a></p>
</div>
</section>
""",
})

# ---------------------------------------------------------------- Cómo funciona / parámetros sísmicos
paginas.append({
    "ruta": "/parametros-sismicos/",
    "titulo": "Parámetros sísmicos de un edificio, desde los planos municipales | antesismo",
    "descripcion": "Cómo se obtienen los parámetros sísmicos de un edificio sin su modelo de cálculo: del expediente municipal al inventario de muros, el modelo de piso rígido, los 21 indicadores del perfil bío-sísmico y el informe firmado.",
    "ld": ld_articulo("Parámetros sísmicos de un edificio, desde los planos municipales", "La cadena del expediente municipal al perfil bío-sísmico y el daño esperado.", "/parametros-sismicos/"),
    "datos": False,
    "cuerpo": f"""
<section class="heroe">
<div class="contenedor">
<span class="etiqueta">Cómo funciona</span>
<h1>Parámetros sísmicos de un edificio, desde los planos municipales</h1>
<p class="intro">Los parámetros sísmicos de un edificio, en el sentido del perfil bío-sísmico, son 21 indicadores que salen de sus períodos, formas modales, masas y desplazamientos. Normalmente solo los tiene quien tiene el modelo de cálculo. antesismo los obtiene del expediente municipal, que es público.</p>
<div class="figura" style="margin-top:28px">{I.CADENA}</div>
</div>
</section>

<section class="seccion">
<div class="contenedor">
<div class="seccion-cabeza"><h2>La cadena, paso a paso</h2></div>
<ol class="pasos">
<li><h3>Expediente municipal</h3><p>Los expedientes de permiso de edificación son públicos por resolución del Consejo para la Transparencia (Oficio 16622, julio de 2025). Con tu mandato los pedimos por transparencia.</p></li>
<li><h3>Inventario de muros</h3><p>Sobre el plano escaneado se marcan los muros piso por piso, con propuestas de IA que valida una persona. Es el paso que concentra la incertidumbre y por eso se muestra para validar.</p></li>
<li><h3>Modelo y cálculo</h3><p>Un solver de piso rígido arma el modelo, calcula los modos y alimenta el motor de indicadores, que reproduce el programa original del método.</p></li>
<li><h3>Perfil, daño e informe</h3><p>21 indicadores con semáforo, controles globales de norma, daño esperado de referencia, y revisión y firma del ingeniero.</p></li>
</ol>
</div>
</section>

<section class="seccion suave">
<div class="contenedor dos-col">
<div>
<h2>¿Puede cualquiera calcular estos parámetros?</h2>
<p>El cálculo sí. El método y sus rangos son públicos, y quien tiene el modelo de un edificio puede calcular el perfil en una planilla. Lo que no es público es lo que el método necesita y lo que convierte el número en una decisión.</p>
<div class="capa publica"><span class="num">1</span><div><h3>El método y sus rangos</h3><p>Públicos, publicados por IEC Ingeniería. Se usan con crédito abierto.</p></div></div>
<div class="capa"><span class="num">2</span><div><h3>Del plano al modelo</h3><p>Inventario de muros desde planos escaneados, solver de piso rígido y motor validados. Un abogado, una tasadora o un banco no tienen el modelo de cálculo y no pueden pedirlo.</p></div></div>
<div class="capa propia"><span class="num">3</span><div><h3>Firma, daño y conector</h3><p>Responsabilidad profesional, daño esperado por edificio, trazabilidad de cada inventario e integración por API en el flujo de una tasadora.</p></div></div>
</div>
<div class="ilustracion">{I.CAPAS}</div>
</div>
</section>

<section class="seccion">
<div class="contenedor">
<div class="seccion-cabeza"><h2>Qué está validado hoy</h2></div>
<div class="rejilla-3">
<div class="tarjeta">{I.ICONO_TRANSPARENTE}<h3>Motor de indicadores</h3><p>Reproduce cuatro corridas históricas del programa original con error relativo menor a 1e-4.</p></div>
<div class="tarjeta">{I.ICONO_TERREMOTO}<h3>Solver de piso rígido</h3><p>Coincide con OpenSees a 1e-6 en las pruebas. Falta contrastarlo con modelos de cáscaras de un software comercial.</p></div>
<div class="tarjeta">{I.ICONO_PLANOS}<h3>Planos a perfil</h3><p>Probado de punta a punta en un edificio de 1963 desde cuatro planos escaneados. <a href="/caso/">Ver el caso</a>.</p></div>
</div>
</div>
</section>

<section class="seccion suave">
<div class="contenedor dos-col">
<div>
<h2>Controles globales y detallamiento</h2>
<p>Un edificio existente se diseñó con la norma de su época. El informe separa los controles globales que se pueden verificar desde los planos, como deriva, corte basal y densidad de muros, del detallamiento que la norma exige hoy a la obra nueva. La norma no es retroactiva, y el informe no dice que un edificio cumple o no cumple la NCh433:2026.</p>
</div>
<div>
<h2>Normativa</h2>
<p>El motor trabaja hoy con la NCh433 Of96 mod. 2009 más DS61. La NCh433:2026, aprobada en 2026 y exigible desde febrero de 2027, se incorpora antes de esa fecha. Perú, Colombia y otros países se abren con un socio local de calibración y firma.</p>
</div>
</div>
</section>
""",
})

# ---------------------------------------------------------------- Precios
CAMPOS_RESERVA = (
    '<div class="doble">' + campo("nombre", "Nombre", extra='autocomplete="name" required') + campo("correo", "Correo", "email", 'autocomplete="email" required') + "</div>"
    + '<div class="doble">' + campo("empresa", "Empresa", extra='autocomplete="organization"')
    + '<label>Qué quieres reservar<select name="oferta"><option>Informe firmado de due diligence</option><option>Conector para tasadoras y proptech</option><option>Piloto para aseguradoras</option></select></label></div>'
    + campo("mensaje", "Cuéntanos el edificio, la cartera o el volumen", "textarea")
)
paginas.append({
    "ruta": "/precios/",
    "titulo": "Precios y pre-venta | antesismo",
    "descripcion": "Informe firmado de due diligence sísmico, conector de riesgo sísmico para tasadoras y piloto para aseguradoras. Reserva sin pago.",
    "ld": ld_servicio("Precios y pre-venta antesismo", "Informe firmado, conector para tasadoras y piloto para aseguradoras.", "/precios/"),
    "datos": False,
    "cuerpo": f"""
<section class="heroe">
<div class="contenedor">
<span class="etiqueta">Pre-venta</span>
<h1>Precios y pre-venta</h1>
<p class="intro">Tres formas de usar antesismo. Cada una se cotiza según el edificio, la cartera o el volumen. Escríbenos y te respondemos con la cotización; pedirla no tiene costo ni compromiso.</p>
<p><a class="boton" href="{cotizar('Cotización antesismo')}">Enviar email por cotizar</a></p>
</div>
</section>

<section class="seccion" style="padding-top:8px">
<div class="contenedor">
<div class="rejilla-3">
<div class="tarjeta oferta destacada">
<span class="etiqueta">Due diligence</span>
<h3>Informe firmado</h3>
<p>Para abogados, fondos y compradores de un edificio.</p>
<div class="precio">Por edificio y operación<small><a href="{cotizar('Cotización informe de due diligence')}">Enviar email por cotizar</a></small></div>
<ul class="lista-check"><li>21 indicadores con semáforo</li><li>Controles globales separados del detallamiento</li><li>Daño esperado de referencia</li><li>Firma de ingeniero civil, en cuatro a siete días</li></ul>
<a class="boton" href="#reserva">Reservar informe de prueba</a>
</div>
<div class="tarjeta oferta">
<span class="etiqueta">Tasadoras y proptech</span>
<h3>Conector por dirección</h3>
<p>Para tasadoras con IA, proptech y bancos hipotecarios.</p>
<div class="precio">Por llamada a la API<small><a href="{cotizar('Cotización conector para tasadoras')}">Enviar email por cotizar</a></small></div>
<ul class="lista-check"><li>Perfil y daño esperado por dirección</li><li>Trazabilidad de cada resultado</li><li>PDF firmado opcional</li><li>Cobertura por comunas acordadas</li></ul>
<a class="boton-sec" href="/tasadoras/#lista">Unirse a la lista de espera</a>
</div>
<div class="tarjeta oferta" id="piloto">
<span class="etiqueta">Aseguradoras y reaseguro</span>
<h3>Piloto cofinanciado</h3>
<p>Un dato de riesgo por edificio para suscripción y selección de riesgos.</p>
<div class="precio">De 10 a 150 edificios<small><a href="{cotizar('Cotización piloto para aseguradoras')}">Enviar email por cotizar</a></small></div>
<ul class="lista-check"><li>Calibración del daño con tus siniestros de 2010 y 2015</li><li>Exclusividad temporal</li><li>Informe por edificio y resumen de cartera</li></ul>
<a class="boton-sec" href="#reserva">Conversar un piloto</a>
</div>
</div>
<p class="pequeño" style="margin-top:16px">Fondos y bancos con cartera: evaluación por lote con informe firmado por edificio y descuento por volumen.</p>
</div>
</section>

<section class="seccion suave" id="reserva">
<div class="contenedor dos-col">
<div>
<h2>Reserva sin pago</h2>
<p class="intro">Dinos qué te interesa. Te contactamos para acordar el alcance y el precio antes de cualquier compromiso.</p>
{LEYENDA}
</div>
{formulario("reserva", "Reserva", CAMPOS_RESERVA, "Reservar")}
</div>
</section>
""",
})

# ---------------------------------------------------------------- Validadores e inversionistas
CAMPOS_VALID = (
    '<div class="doble">' + campo("nombre", "Nombre", extra='autocomplete="name" required') + campo("correo", "Correo", "email", 'autocomplete="email" required') + "</div>"
    + '<div class="doble">' + campo("institucion", "Oficina, universidad o fondo", extra='autocomplete="organization"')
    + '<label>Qué quieres<select name="interes"><option>Paquete del caso para reproducir</option><option>Reportar una discrepancia</option><option>Acceso a la sala de datos</option><option>Otra</option></select></label></div>'
    + campo("mensaje", "Mensaje", "textarea")
)
paginas.append({
    "ruta": "/validadores/",
    "titulo": "Validadores e inversionistas: estado real del proyecto | antesismo",
    "descripcion": "Lo que existe, lo que está validado y lo que falta en antesismo, sin adornos. Casos para reproducir y contacto para validadores e inversionistas.",
    "ld": ld_articulo("Validadores e inversionistas: estado real del proyecto", "Estado del motor, el solver, el perfil 3.0 y lo que falta.", "/validadores/"),
    "datos": False,
    "cuerpo": f"""
<section class="heroe">
<div class="contenedor">
<span class="etiqueta">Validadores e inversionistas</span>
<h1>Estado real del proyecto</h1>
<p class="intro">Esta página muestra lo que existe, lo que está validado y lo que falta, sin adornos. Las cifras financieras del proyecto son hipótesis y no se publican aquí.</p>
</div>
</section>

<section class="seccion" style="padding-top:8px">
<div class="contenedor">
<div class="estado-proyecto">
<div class="col"><h3><span class="estado verde">Verde</span> Existe y está validado</h3><ul>
<li>Motor: cuatro corridas históricas reproducidas con error relativo menor a 1e-4.</li>
<li>Solver de piso rígido, coincide con OpenSees a 1e-6.</li>
<li>Perfil 3.0 con 21 indicadores y la tabla completa de Cd.</li>
<li>Caso desde planos municipales de punta a punta, con daño esperado.</li></ul></div>
<div class="col"><h3><span class="estado amarillo">Amarillo</span> Existe y falta validar</h3><ul>
<li>Lector de tablas de modelos comerciales con una exportación real.</li>
<li>Tablas de la NCh433:2026, exigible desde febrero de 2027.</li>
<li>Solver frente a modelos de cáscaras.</li>
<li>Seguro de responsabilidad profesional para la firma.</li></ul></div>
<div class="col"><h3><span class="estado rojo">Rojo</span> No existe todavía</h3><ul>
<li>Transcripción automática de planos.</li>
<li>Calibración de los factores de daño con siniestros.</li>
<li>Cuentas, pagos y API en producción.</li>
<li>Conector por dirección; hoy es lista de espera.</li></ul></div>
</div>
</div>
</section>

<section class="seccion suave">
<div class="contenedor dos-col">
<div>
<h2>Para validadores</h2>
<p>Oficinas de cálculo, revisores y academia: el método es público y aquí se usa con crédito abierto. Te invitamos a reproducir el caso de 1963 y los cuatro casos históricos, y a reportar discrepancias. Las discrepancias se publican con su respuesta.</p>
<p>El paquete de descarga, con la entrada del motor, los resultados y la tabla de 13 frente a 21 indicadores, está en preparación con los datos anonimizados. Pídelo y te avisamos cuando esté.</p>
<h2 style="margin-top:32px">Para inversionistas</h2>
<p>Modelo de negocio, validación y modelo financiero se comparten en una sala de datos con registro y acuerdo de confidencialidad, en la próxima versión del sitio.</p>
<h3 style="margin-top:24px">Próximos 90 días</h3>
<ol class="linea">
<li><span class="dia">Días 1 a 30</span><p>Sitio con pre-venta, entrevistas con abogados de due diligence, tasadoras y proptech, y medición de horas de transcripción en cinco planos.</p></li>
<li><span class="dia">Días 31 a 60</span><p>Vista de marcado de muros y primer informe firmado pagado.</p></li>
<li><span class="dia">Días 61 a 90</span><p>Piloto con una tasadora o proptech sobre direcciones acordadas y conversaciones con aseguradoras.</p></li>
</ol>
</div>
<div id="contacto">
{formulario("validadores", "Contacto para validadores e inversionistas", CAMPOS_VALID, "Enviar")}
</div>
</div>
</section>
""",
})

# ---------------------------------------------------------------- Legal
paginas.append({
    "ruta": "/legal/",
    "titulo": "Términos de uso y política de privacidad | antesismo",
    "descripcion": "Términos de uso de antesismo y política de privacidad conforme a la Ley 19.628 y la Ley 21.719 de protección de datos personales de Chile.",
    "ld": ld_articulo("Términos de uso y política de privacidad", "Términos de uso y política de privacidad de antesismo.", "/legal/"),
    "datos": False,
    "cuerpo": L.legal(CORREO),
})

# ---------------------------------------------------------------- Quién está detrás
paginas.append({
    "ruta": "/quien-esta-detras/",
    "titulo": "Quién está detrás de antesismo: Ing. Rodney Bellido de Luna | antesismo",
    "descripcion": "Ing. Rodney Bellido de Luna, ingeniero civil en obras civiles de la Universidad Central de Chile, desarrolla antesismo y firma cada informe. Biografía y responsabilidad profesional.",
    "ld": {
        "@context": "https://schema.org", "@type": "ProfilePage", "url": DOMINIO + "/quien-esta-detras/",
        "mainEntity": {
            "@type": "Person", "name": "Rodney Bellido de Luna", "honorificPrefix": "Ing.",
            "jobTitle": "Ingeniero civil en obras civiles", "email": "mailto:" + CORREO,
            "alumniOf": {"@type": "CollegeOrUniversity", "name": "Universidad Central de Chile"},
            "sameAs": ["https://www.linkedin.com/in/rbellido/"],
        },
    },
    "datos": False,
    "cuerpo": L.quien(CORREO, I.FIRMA),
})


def escribir(p: dict) -> None:
    html = cabeza(p) + "\n" + encabezado(p["ruta"]) + p["cuerpo"] + pie(p["datos"])
    assert "—" not in html and "–" not in html, "guion largo en " + p["ruta"]
    destino = RAIZ / p["ruta"].strip("/") / "index.html" if p["ruta"] != "/" else RAIZ / "index.html"
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(html, encoding="utf-8")


def no_encontrada() -> None:
    p = {"ruta": "/404.html", "titulo": "Página no encontrada | antesismo", "descripcion": "La página que buscas no existe.",
         "ld": {"@context": "https://schema.org", "@type": "WebPage", "name": "Página no encontrada"}}
    cuerpo = f"""
<section class="seccion"><div class="contenedor centro" style="max-width:640px">
<div style="max-width:280px;margin:0 auto 20px">{I.NO_ENCONTRADA}</div>
<h1>No encontramos esta página</h1>
<p class="intro" style="margin:0 auto 20px">Puede que la dirección haya cambiado. Vuelve al inicio o mira el caso demostrativo.</p>
<div class="botones" style="justify-content:center"><a class="boton" href="/">Ir al inicio</a><a class="boton-sec" href="/caso/">Ver el caso</a></div>
</div></section>
"""
    html = cabeza(p).replace('<link rel="canonical" href="https://antesismo.bdl.cl/404.html">\n', "") + "\n" + encabezado("") + cuerpo + pie(False)
    (RAIZ / "404.html").write_text(html, encoding="utf-8")


def datos_js() -> None:
    datos = {"perfil": perfil, "geometria": {k: geometria[k] for k in ("LX", "LY", "alturas", "muros", "cm")},
             "modos": geometria["modos"], "dano": DANO}
    js = "/* Caso demostrativo anonimizado, generado por fuente/construir.py. */\nwindow.ANTESISMO_CASO = " + json.dumps(datos, ensure_ascii=False, separators=(",", ":")) + ";\n"
    (RAIZ / "assets" / "js" / "datos-caso.js").write_text(js, encoding="utf-8")


def complementos() -> None:
    urls = "\n".join(f"  <url><loc>{DOMINIO}{p['ruta']}</loc><lastmod>2026-10-24</lastmod></url>" for p in paginas)
    (RAIZ / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n', encoding="utf-8")
    if OCULTO:
        robots = ("# Sitio en revisión: cerrado a buscadores y a rastreadores de IA.\n"
                  + "".join(f"User-agent: {b}\n" for b in BOTS_IA) + "Disallow: /\n\nUser-agent: *\nDisallow: /\n")
    else:
        robots = f"User-agent: *\nAllow: /\nSitemap: {DOMINIO}/sitemap.xml\n"
    (RAIZ / "robots.txt").write_text(robots, encoding="utf-8")
    config = {
        "trailingSlash": "auto",
        "routes": [{"route": "/fuente/*", "statusCode": 404}, {"route": "/README.md", "statusCode": 404}],
        "responseOverrides": {"404": {"rewrite": "/404.html", "statusCode": 404}},
        "globalHeaders": {"X-Content-Type-Options": "nosniff", "Referrer-Policy": "strict-origin-when-cross-origin"},
        "mimeTypes": {".webmanifest": "application/manifest+json"},
    }
    if OCULTO:
        config["globalHeaders"]["X-Robots-Tag"] = ROBOTS_META
    (RAIZ / "staticwebapp.config.json").write_text(json.dumps(config, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    for p in paginas:
        escribir(p)
    no_encontrada()
    datos_js()
    complementos()
    print(f"{len(paginas)} páginas, 404, datos y configuración escritos en {RAIZ}")
    print(f"Lecturas: {N_NORMAL} normal, {N_ACEPT} aceptable, {N_FUERA_LECT} fuera; indicadores con alguna lectura fuera: {N_FUERA}")
