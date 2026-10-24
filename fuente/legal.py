"""Textos de la página de quién está detrás y de la página legal de antesismo.

Borrador preparado para revisión legal. Base: Ley 19.628 vigente y Ley 21.719,
que entra en vigencia el 1 de diciembre de 2026 (el Boletín 18.623-07 propone
postergarla un año y no está aprobado al 24 de octubre de 2026).
"""

FECHA = "24 de octubre de 2026"
VERSION_LEGAL = "0.9, borrador para revisión legal"


def quien(correo: str, ilustracion: str) -> str:
    return f"""
<section class="heroe">
<div class="contenedor dos-col">
<div>
<span class="etiqueta">Quién está detrás de antesismo</span>
<h1>Ing. Rodney Bellido de Luna</h1>
<p class="intro">Ingeniero civil en obras civiles de la Universidad Central de Chile. Es quien desarrolla antesismo, quien revisa cada inventario de muros y quien firma cada informe.</p>
<div class="botones">
<a class="boton" href="mailto:{correo}">Escribir a {correo}</a>
<a class="boton-sec" href="https://www.linkedin.com/in/rbellido/" rel="noopener">Perfil en LinkedIn</a>
</div>
</div>
<div class="ilustracion">{ilustracion}</div>
</div>
</section>

<section class="seccion">
<div class="contenedor dos-col">
<div>
<h2>Biografía</h2>
<p>Rodney Bellido de Luna es ingeniero civil en obras civiles, titulado en la Universidad Central de Chile, y trabaja en la evaluación de estructuras de hormigón armado.</p>
<p>Su vínculo con el perfil bío-sísmico empezó entre 2009 y 2012. A partir del programa original en Fortran que le facilitó Vladimir Mardones, quien trabajó con Tomás Guendelman, desarrolló una versión propia del cálculo en MATLAB, una librería para Excel y una macro de reporte, y la aplicó a edificios chilenos reales.</p>
<p>En 2026 reescribió ese motor en Python y lo validó contra cuatro corridas históricas del programa original, con error relativo menor a 1e-4. Le agregó los 21 indicadores de la versión 3.0 del perfil, un solver de piso rígido validado contra OpenSees y la cadena que permite obtener el perfil desde los planos del expediente municipal, sin el modelo de cálculo del edificio. Esa cadena se probó de punta a punta en el <a href="/caso/">caso demostrativo</a>, un edificio de 1963.</p>
<p>En Chile también presta servicios de diagnóstico estructural con ensayos no destructivos en hormigón armado, junto al Ing. José Bellido de Luna, en <a href="https://servicios.bdl.cl" rel="noopener">BDL</a>.</p>
</div>
<div class="panel">
<h3 class="mt-0">Lo que aporta y lo que no</h3>
<ul class="lista-check">
<li>Lleva una metodología pública a una capa de uso para quien no tiene el modelo de cálculo: compradores, abogados, tasadoras, bancos y aseguradoras.</li>
<li>Construyó y mantiene el motor, el solver y la lectura de planos, con código y casos que se pueden reproducir.</li>
<li>Da crédito abierto y directo a los creadores del método en cada página y en cada informe.</li>
</ul>
<ul class="lista-no">
<li>No es autor del Perfil Bío-Sísmico de Edificios. El método es de Tomás Guendelman e IEC Ingeniería, con Mario Guendelman, Jorge Lindenberg, Francisco Medina y Luis Figueroa.</li>
<li>antesismo no es un sitio de IEC Ingeniería ni está avalado por sus autores.</li>
</ul>
</div>
</div>
</section>

<section class="seccion suave">
<div class="contenedor">
<div class="seccion-cabeza"><h2>Su responsabilidad en cada informe</h2><p>Quién firma tiene que poder explicar cada número. Esto es lo que asume Rodney en cada encargo, y lo que queda fuera.</p></div>
<div class="rejilla-3">
<div class="tarjeta">{_icono_firma()}<h3>Lo que revisa y firma</h3><p>Revisa personalmente el inventario de muros transcrito desde el plano, los supuestos del modelo, los 21 indicadores y la lectura del daño esperado. Firma el informe como ingeniero civil y responde por su trabajo profesional dentro del alcance contratado.</p></div>
<div class="tarjeta"><svg class="icono" viewBox="0 0 48 48" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"><path d="M24 4l16 6v12c0 10-7 18-16 22C15 40 8 32 8 22V10z"/><path d="M17 24l5 5 9-10"/></svg><h3>Cómo lo hace</h3><p>Declara en cada informe la fuente documental, los supuestos de zona y suelo, la incertidumbre del inventario y la versión de rangos aplicada. El seguro de responsabilidad profesional está en contratación y estará vigente antes del primer informe pagado.</p></div>
<div class="tarjeta"><svg class="icono" viewBox="0 0 48 48" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"><circle cx="24" cy="24" r="18"/><path d="M12 12l24 24"/></svg><h3>Lo que no hace</h3><p>No hace la revisión del proyecto de cálculo estructural que exige la normativa de urbanismo y construcciones, no certifica cumplimiento normativo de edificios existentes y no reemplaza una inspección en terreno ni el cálculo de un proyecto.</p></div>
</div>
<p class="leyenda">Cada resultado de antesismo lleva esta leyenda: no es revisión estructural ni certificación de cumplimiento normativo.</p>
</div>
</section>

<section class="seccion">
<div class="contenedor centro" style="max-width:720px">
<h2>Conversemos tu edificio</h2>
<p class="intro" style="margin:0 auto 20px">Cuéntale a Rodney qué edificio, qué operación y qué plazo tienes.</p>
<a class="boton" href="mailto:{correo}?subject=Consulta%20antesismo">Escribir a {correo}</a>
</div>
</section>
"""


def _icono_firma() -> str:
    return """<svg class="icono" viewBox="0 0 48 48" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
<path d="M10 5h20l8 8v16"/><path d="M30 5v8h8"/><path d="M10 5v38h14"/><path d="M16 17h12M16 24h14"/>
<path d="M17 35c2-3 4-3 5 0s3 2 5-1"/><path d="M31 43l2-6 9-9 4 4-9 9z"/></svg>"""


def legal(correo: str) -> str:
    return f"""
<section class="heroe">
<div class="contenedor">
<span class="etiqueta">Legal</span>
<h1>Términos de uso y política de privacidad</h1>
<p class="intro">Aquí está lo que puedes esperar de antesismo, lo que no, y cómo tratamos tus datos personales. Está escrito para que se entienda sin abogado.</p>
<p class="pequeño">Versión {VERSION_LEGAL}, {FECHA}. Esta versión es un borrador y requiere revisión de un abogado antes de regir para clientes.</p>
<nav class="indice" aria-label="Contenido de la página">
<a href="#terminos">Términos de uso</a><a href="#privacidad">Política de privacidad</a><a href="#derechos">Tus derechos</a><a href="#contacto-legal">Contacto</a>
</nav>
</div>
</section>

<section class="seccion" id="terminos">
<div class="contenedor documento">
<h2>Términos de uso</h2>

<h3>1. Quién presta el servicio</h3>
<p>antesismo es un servicio del Ing. Rodney Bellido de Luna, ingeniero civil en obras civiles, persona natural con domicilio en Chile. Contacto: <a href="mailto:{correo}">{correo}</a>. En estos términos, "antesismo", "nosotros" o "el prestador" se refieren a él; "tú" o "el cliente" se refiere a quien usa el sitio o contrata el servicio.</p>

<h3>2. Qué es este sitio</h3>
<p>El sitio informa sobre el servicio de evaluación sísmica de edificios desde los planos de recepción municipal y permite pedir una cotización. Publicar información en el sitio no es una oferta de contrato: cada encargo se acepta por escrito.</p>

<h3>3. Qué entrega antesismo y qué no</h3>
<p>antesismo entrega un informe de salud estructural de un edificio existente, basado en el Perfil Bío-Sísmico de Edificios de IEC Ingeniería, con controles globales de norma y daño esperado de referencia. En concreto:</p>
<ul>
<li>El informe mide la estructuración del edificio y la compara con edificios chilenos que se comportaron bien en terremotos reales. No garantiza el comportamiento del edificio en un sismo futuro, que puede superar el sismo de diseño.</li>
<li>No es la revisión del proyecto de cálculo estructural que exige la normativa de urbanismo y construcciones, ni una certificación de cumplimiento de la NCh433 u otra norma para edificios existentes.</li>
<li>No reemplaza una inspección en terreno, ensayos de materiales ni el cálculo estructural de un proyecto.</li>
<li>El daño esperado es una referencia basada en funciones de daño publicadas (HAZUS), sin calibrar con siniestros chilenos. Se entrega como rango y no como cifra exacta, y no es una tasación ni un modelo de catástrofe para seguros.</li>
<li>La calidad del resultado depende de la calidad y completitud de los planos disponibles. Cada informe declara sus supuestos y su incertidumbre.</li>
</ul>

<h3>4. Cómo se contrata</h3>
<p>Cada servicio se cotiza por correo. La cotización aceptada por escrito fija el edificio, el alcance, el plazo, el precio, la forma de pago y los entregables, y prevalece sobre estos términos en lo que regule de forma distinta. Pedir una cotización, reservar o unirse a una lista de espera no obliga a contratar ni a pagar.</p>

<h3>5. Lo que nos entregas</h3>
<p>Si nos entregas planos, expedientes u otros documentos, declaras que los obtuviste de forma legítima y que puedes usarlos para este fin. Los expedientes de permisos de edificación son públicos por resolución del Consejo para la Transparencia; si nos das mandato, podemos pedirlos por transparencia a tu nombre. Eres responsable de que la información que entregas sea correcta.</p>

<h3>6. Responsabilidad</h3>
<p>El Ing. Rodney Bellido de Luna responde por su trabajo profesional con la diligencia propia de un ingeniero civil y dentro del alcance contratado. No responde por el uso del informe para fines distintos de los indicados en la cotización, por decisiones de terceros basadas en él, ni por resultados que se deban a información incompleta o incorrecta entregada por el cliente. La cotización aceptada puede fijar límites adicionales en la medida que la ley lo permita. Nada de lo anterior limita los derechos irrenunciables que te da la Ley 19.496 si contratas como consumidor.</p>

<h3>7. Propiedad intelectual y crédito</h3>
<p>El Perfil Bío-Sísmico de Edificios es obra de Tomás Guendelman e IEC Ingeniería; antesismo lo usa con crédito abierto y no reclama derechos sobre el método. Los textos, ilustraciones, software, figuras y diseño de este sitio y de los informes son del prestador, salvo las marcas y obras de terceros que se citan. El cliente recibe una licencia para usar su informe en la operación para la que lo contrató y compartirlo con sus asesores, financistas, aseguradores y contrapartes de esa operación, sin alterarlo y manteniendo el crédito y la leyenda.</p>

<h3>8. Uso del sitio</h3>
<p>Puedes leer y compartir los contenidos del sitio citando la fuente. No se autoriza la extracción automatizada de contenidos ni su uso para entrenar o alimentar modelos de inteligencia artificial sin autorización escrita. Los enlaces a sitios de terceros, como iec.cl o LinkedIn, se ofrecen por conveniencia y no los controlamos.</p>

<h3>9. Cambios, ley aplicable y controversias</h3>
<p>Podemos actualizar estos términos; la versión y la fecha vigentes se indican al inicio de esta página, y los encargos ya aceptados se rigen por la versión vigente al aceptarlos. Estos términos se rigen por la ley chilena. Las controversias se someten a los tribunales ordinarios de justicia de Santiago, sin perjuicio de los derechos del consumidor a recurrir al tribunal de su domicilio.</p>
</div>
</section>

<section class="seccion suave" id="privacidad">
<div class="contenedor documento">
<h2>Política de privacidad</h2>
<p>Esta política se ajusta a la Ley 19.628 sobre protección de la vida privada y a la Ley 21.719, que la modifica y crea la Agencia de Protección de Datos Personales, cuya entrada en vigencia está fijada para el 1 de diciembre de 2026. La aplicamos desde ya con los principios de la Ley 21.719: licitud, finalidad, proporcionalidad, calidad, responsabilidad, seguridad, transparencia y confidencialidad.</p>

<h3>1. Responsable del tratamiento</h3>
<p>Ing. Rodney Bellido de Luna, persona natural con domicilio en Chile. Correo para todo lo relativo a datos personales: <a href="mailto:{correo}?subject=Datos%20personales">{correo}</a>.</p>

<h3>2. Qué datos tratamos</h3>
<div class="tabla-envoltura"><table>
<thead><tr><th>Cuándo</th><th>Qué datos</th><th>Para qué</th><th>Base de licitud</th></tr></thead>
<tbody>
<tr><td>Navegas por el sitio</td><td>Datos técnicos que registra el proveedor de alojamiento: dirección IP, fecha y hora, página pedida y navegador</td><td>Entregar las páginas y proteger el sitio contra abusos</td><td>Interés legítimo en la seguridad del servicio</td></tr>
<tr><td>Nos escribes o usas un formulario</td><td>Nombre, correo, empresa, dirección del edificio y lo que cuentes en el mensaje</td><td>Responderte y preparar una cotización</td><td>Tu solicitud y las medidas precontractuales que pides</td></tr>
<tr><td>Contratas un informe</td><td>Datos de contacto y facturación, planos y documentos del edificio</td><td>Ejecutar el encargo, emitir el informe y facturar</td><td>Ejecución del contrato y cumplimiento de obligaciones legales, como las tributarias</td></tr>
<tr><td>Te unes a una lista de espera</td><td>Nombre, correo, empresa, volumen y comunas de interés</td><td>Avisarte cuando el servicio esté disponible y diseñar el piloto</td><td>Tu consentimiento, que puedes retirar cuando quieras</td></tr>
</tbody></table></div>
<p style="margin-top:14px">El sitio no usa cookies, ni herramientas de analítica, ni píxeles publicitarios, ni fuentes o servicios de terceros que reciban tus datos al navegar. No tratamos datos sensibles ni datos de niños, niñas o adolescentes, y te pedimos no incluirlos en tus mensajes.</p>

<h3>3. Planos y datos de terceros</h3>
<p>Los planos y expedientes municipales pueden incluir nombres de propietarios, arquitectos, calculistas u otras personas. Los usamos solo para obtener la geometría del edificio. El perfil es del edificio, no de las personas: no cruzamos el edificio con rol, póliza, tasación ni ningún dato de sus propietarios u ocupantes, y los casos que publicamos se anonimizan.</p>

<h3>4. Cómo funcionan los formularios</h3>
<p>Los formularios de este sitio no envían nada a un servidor. Al enviarlos se abre tu programa de correo con el mensaje listo para {correo}; tú decides si lo envías. Desde ahí el mensaje viaja por tu proveedor de correo y el del dominio bdl.cl.</p>

<h3>5. Con quién compartimos datos</h3>
<p>No vendemos ni cedemos tus datos, no los usamos para publicidad y no tomamos decisiones automatizadas con efectos sobre ti. Solo intervienen proveedores que actúan como encargados del tratamiento, bajo sus condiciones de confidencialidad y seguridad:</p>
<ul>
<li>Microsoft, por Azure Static Web Apps, que aloja el sitio.</li>
<li>El proveedor de correo del dominio bdl.cl, que recibe los mensajes.</li>
<li>Los servicios de almacenamiento y ofimática con que se preparan los informes, que se indican en la cotización.</li>
</ul>
<p>Algunos de estos proveedores pueden tratar datos en servidores fuera de Chile. Cuando ocurre, la transferencia internacional se hace con proveedores que ofrecen garantías contractuales de protección adecuadas, conforme a la ley.</p>

<h3>6. Cuánto tiempo los guardamos</h3>
<ul>
<li>Consultas que no terminan en contrato: hasta 12 meses desde el último contacto, y luego se eliminan.</li>
<li>Planos y documentos del edificio: se eliminan dentro de 90 días desde la entrega del informe, salvo que pidas por escrito conservar el proyecto.</li>
<li>Informes emitidos y respaldos de facturación: durante los plazos que exigen las leyes tributarias y para la defensa ante reclamos, y luego se eliminan.</li>
<li>Listas de espera: hasta que retires tu consentimiento o el servicio esté disponible y te hayamos avisado.</li>
</ul>

<h3>7. Seguridad</h3>
<p>El sitio funciona solo con conexión cifrada. Pedimos los datos mínimos, restringimos el acceso a los documentos a quien trabaja el encargo y eliminamos lo que ya no se necesita según los plazos de la sección anterior. Si ocurre una vulneración de seguridad que afecte tus datos, la informaremos a la Agencia de Protección de Datos Personales y a ti cuando la ley lo exija.</p>

<h3 id="derechos">8. Tus derechos</h3>
<p>Puedes ejercer en cualquier momento, de forma gratuita, estos derechos sobre tus datos:</p>
<ul>
<li><strong>Acceso:</strong> saber si tratamos tus datos, cuáles, para qué y con quién se comparten.</li>
<li><strong>Rectificación:</strong> corregir datos inexactos o incompletos.</li>
<li><strong>Supresión:</strong> pedir que eliminemos tus datos cuando ya no sean necesarios o retires tu consentimiento.</li>
<li><strong>Oposición:</strong> oponerte a un tratamiento, incluido el basado en interés legítimo.</li>
<li><strong>Portabilidad:</strong> recibir tus datos en un formato estructurado y de uso común.</li>
<li><strong>Bloqueo:</strong> pedir la suspensión temporal del tratamiento mientras se resuelve otra solicitud.</li>
<li><strong>Decisiones automatizadas:</strong> no ser objeto de decisiones basadas solo en tratamiento automatizado. antesismo no toma este tipo de decisiones sobre personas.</li>
<li><strong>Retirar el consentimiento</strong> cuando sea la base del tratamiento, sin efecto retroactivo.</li>
</ul>
<p id="contacto-legal">Para ejercerlos, escribe a <a href="mailto:{correo}?subject=Derechos%20sobre%20datos%20personales">{correo}</a> con el asunto "Derechos sobre datos personales", indicando qué derecho ejerces y un dato que nos permita verificar que eres el titular. Acusamos recibo y respondemos dentro de 30 días corridos, prorrogables por una sola vez por igual plazo si la solicitud lo requiere, avisándote antes de que venza el primero. Si no quedas conforme con la respuesta, puedes reclamar ante la Agencia de Protección de Datos Personales una vez que esté en funciones, o ante los tribunales conforme a la ley vigente.</p>

<h3>9. Cambios a esta política</h3>
<p>Si cambiamos esta política, publicaremos la nueva versión con su fecha en esta página. Si el cambio afecta de forma relevante el uso de datos que ya nos entregaste, te avisaremos por correo antes de aplicarlo.</p>
</div>
</section>
"""
