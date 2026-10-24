"""Ilustraciones SVG en línea del sitio, en grafito y verde de la marca antesismo."""

G = "#263036"
V = "#297e7a"
S = "#f3f6f7"
B = "#d9e1e3"

# Iconos de un solo color, trazo grueso y extremos rectos como el isotipo
ICONO_PLANOS = """<svg class="icono" viewBox="0 0 48 48" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="3" stroke-linejoin="round">
<path d="M10 5h20l8 8v30H10z"/><path d="M30 5v8h8"/><path d="M16 19h16M16 19v18M24 19v10M16 29h8M32 19v18M16 37h16" stroke-width="2.6"/></svg>"""

ICONO_FIRMA = """<svg class="icono" viewBox="0 0 48 48" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
<path d="M10 5h20l8 8v16"/><path d="M30 5v8h8"/><path d="M10 5v38h14"/><path d="M16 17h12M16 24h14"/>
<path d="M17 35c2-3 4-3 5 0s3 2 5-1"/><path d="M31 43l2-6 9-9 4 4-9 9z"/></svg>"""

ICONO_DANO = """<svg class="icono" viewBox="0 0 48 48" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
<path d="M12 40V12l12-5v33M24 14l12 5v21"/><path d="M17 18l3 5-3 4 3 5" stroke-width="2.4"/>
<path d="M3 44h6l3-4 4 7 4-7 4 4 4-4 4 7 4-7 3 4h6" stroke-width="2.4"/></svg>"""

ICONO_CONECTA = """<svg class="icono" viewBox="0 0 48 48" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
<path d="M16 10c-4 0-5 2-5 5v4c0 3-2 5-5 5 3 0 5 2 5 5v4c0 3 1 5 5 5M32 10c4 0 5 2 5 5v4c0 3 2 5 5 5-3 0-5 2-5 5v4c0 3-1 5-5 5"/>
<circle cx="24" cy="20" r="4"/><path d="M24 24v4M20 32h8"/></svg>"""

ICONO_TERREMOTO = """<svg class="icono" viewBox="0 0 48 48" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
<path d="M3 24h8l4-10 6 22 6-28 5 22 3-6h10"/></svg>"""

ICONO_TRANSPARENTE = """<svg class="icono" viewBox="0 0 48 48" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="3" stroke-linejoin="round" stroke-linecap="round">
<circle cx="21" cy="21" r="12"/><path d="M30 30l12 12"/><path d="M15 21h12M21 15v12" stroke-width="2.4"/></svg>"""

# Escena principal: edificios sobre un registro sísmico, con la hoja del informe y el semáforo
ESCENA = f"""<svg viewBox="0 0 560 380" role="img" aria-labelledby="esc-t">
<title id="esc-t">Ilustración: edificios de muros sobre un registro sísmico, con la hoja del informe y su semáforo de indicadores</title>
<rect x="0" y="0" width="560" height="380" rx="16" fill="{S}"/>
<g fill="none" stroke="{B}" stroke-width="1">
<path d="M40 60h480M40 110h480M40 160h480M40 210h480M40 260h480"/></g>
<path d="M20 318h70l10-14 12 28 12-40 12 54 12-62 12 50 10-30 10 18 8-8h340" fill="none" stroke="{V}" stroke-width="4" stroke-linejoin="round" stroke-linecap="square"/>
<g fill="none" stroke="{G}" stroke-width="11" stroke-linejoin="miter" stroke-linecap="square">
<path d="M70 300V170l46-20v150"/><path d="M116 150l52 22v128" stroke="{V}"/><path d="M190 300V214l30 14v72" stroke="{V}"/>
<path d="M58 300h190"/></g>
<g fill="{G}" opacity=".9"><rect x="84" y="186" width="18" height="12"/><rect x="84" y="214" width="18" height="12"/><rect x="84" y="242" width="18" height="12"/><rect x="84" y="270" width="18" height="12"/></g>
<g transform="translate(300 52)">
<path d="M0 0h150l40 40v220H0z" fill="#fff" stroke="{G}" stroke-width="8" stroke-linejoin="round"/>
<path d="M150 0v40h40z" fill="{V}"/>
<g font-family="Inter, Arial, sans-serif" font-size="13" fill="{G}"><text x="20" y="34" font-weight="700">Informe</text><text x="20" y="52" fill="#5f6e75" font-size="11">21 indicadores, X e Y</text></g>
<g>
<rect x="20" y="68" width="150" height="10" rx="3" fill="#d3eadb"/><circle cx="74" cy="73" r="6" fill="{G}"/>
<rect x="20" y="90" width="150" height="10" rx="3" fill="#d3eadb"/><circle cx="58" cy="95" r="6" fill="{G}"/>
<rect x="20" y="112" width="150" height="10" rx="3" fill="#f6e5ae"/><circle cx="118" cy="117" r="6" fill="{G}"/>
<rect x="20" y="134" width="150" height="10" rx="3" fill="#d3eadb"/><circle cx="88" cy="139" r="6" fill="{G}"/>
<rect x="20" y="156" width="150" height="10" rx="3" fill="#f4cbc4"/><circle cx="146" cy="161" r="6" fill="{G}"/>
</g>
<path d="M20 214c10-12 18-12 22 0s14 8 22-4" fill="none" stroke="{G}" stroke-width="3" stroke-linecap="round"/>
<path d="M20 232h110" stroke="{B}" stroke-width="3"/>
<text x="20" y="250" font-family="Inter, Arial, sans-serif" font-size="11" fill="#5f6e75">Firma del ingeniero civil</text>
</g>
</svg>"""

# Cadena: del expediente municipal al informe firmado
def _paso(x, titulo, linea2, dibujo):
    return f"""<g transform="translate({x} 0)">
<rect x="0" y="20" width="150" height="150" rx="14" fill="#fff" stroke="{B}" stroke-width="2"/>
{dibujo}
<text x="75" y="200" text-anchor="middle" font-family="Inter, Arial, sans-serif" font-size="15" font-weight="700" fill="{G}">{titulo}</text>
<text x="75" y="220" text-anchor="middle" font-family="Inter, Arial, sans-serif" font-size="12.5" fill="#5f6e75">{linea2}</text>
</g>"""

_D1 = f"""<path d="M40 42h56l18 18v92H40z" fill="{S}" stroke="{G}" stroke-width="6" stroke-linejoin="round"/><path d="M96 42v18h18" fill="none" stroke="{G}" stroke-width="5"/>
<path d="M54 74h44M54 74v56M76 74v30M54 104h22M98 74v56M54 130h44" fill="none" stroke="{G}" stroke-width="3.5" opacity=".55"/>"""
_D2 = f"""<rect x="34" y="40" width="82" height="112" fill="{S}" stroke="{B}" stroke-width="2"/>
<path d="M42 50h66M42 50v40M42 90h32M108 50v92M42 112v30M42 142h66M76 70v42" fill="none" stroke="{G}" stroke-width="5"/>
<path d="M76 70v42" stroke="{V}" stroke-width="7"/><path d="M118 112l-10 14 4 1-3 9 4 2 4-9 4 3z" fill="{V}"/>"""
_D3 = f"""<g fill="none" stroke="{G}" stroke-width="6" stroke-linejoin="round"><path d="M50 150V62l26-12 26 12v88"/><path d="M50 84h52M50 106h52M50 128h52" stroke-width="3" opacity=".5"/></g>
<path d="M112 62c10 8 10 24 0 32M118 52c16 14 16 40 0 54" fill="none" stroke="{V}" stroke-width="4" stroke-linecap="round"/>
<path d="M40 150h72" stroke="{G}" stroke-width="6"/>"""
_D4 = f"""<g><rect x="32" y="50" width="86" height="12" rx="3" fill="#d3eadb"/><rect x="32" y="76" width="86" height="12" rx="3" fill="#d3eadb"/>
<rect x="32" y="102" width="86" height="12" rx="3" fill="#f6e5ae"/><rect x="32" y="128" width="86" height="12" rx="3" fill="#d3eadb"/>
<circle cx="66" cy="56" r="7" fill="{G}"/><circle cx="52" cy="82" r="7" fill="{G}"/><circle cx="96" cy="108" r="7" fill="{G}"/><circle cx="74" cy="134" r="7" fill="{G}"/></g>"""
_D5 = f"""<path d="M42 40h50l18 18v96H42z" fill="#fff" stroke="{G}" stroke-width="6" stroke-linejoin="round"/><path d="M92 40v18h18z" fill="{V}"/>
<path d="M54 72h36M54 88h44M54 104h30" stroke="{B}" stroke-width="5"/>
<path d="M54 132c6-8 11-8 13 0s9 5 14-3" fill="none" stroke="{G}" stroke-width="3.5" stroke-linecap="round"/>"""

def _flecha(x):
    return f"""<path d="M{x} 95h22m-8-8 8 8-8 8" fill="none" stroke="{V}" stroke-width="4" stroke-linecap="square"/>"""

CADENA = f"""<svg viewBox="0 0 870 236" role="img" aria-labelledby="cad-t">
<title id="cad-t">Cadena de trabajo: expediente municipal, inventario de muros, modelo de piso rígido, perfil de 21 indicadores e informe firmado</title>
{_paso(0, "Expediente", "planos municipales", _D1)}{_flecha(156)}
{_paso(180, "Inventario", "muros por piso", _D2)}{_flecha(336)}
{_paso(360, "Modelo", "piso rígido y modos", _D3)}{_flecha(516)}
{_paso(540, "Perfil", "21 indicadores y daño", _D4)}{_flecha(696)}
{_paso(720, "Informe", "revisado y firmado", _D5)}
</svg>"""

# Tres capas: método público, datos que no son públicos, producto
CAPAS = f"""<svg viewBox="0 0 420 300" role="img" aria-labelledby="cap-t">
<title id="cap-t">Tres capas apiladas: el método público abajo, la cadena desde planos municipales al medio y la firma con el daño esperado arriba</title>
<g font-family="Inter, Arial, sans-serif" font-size="14" font-weight="700">
<path d="M210 196l170 50-170 50-170-50z" fill="#c9d3d6"/><path d="M40 246v-10l170-50 170 50v10l-170-50z" fill="#b2bfc3"/>
<text x="210" y="252" text-anchor="middle" fill="{G}">1. Método público</text>
<path d="M210 118l170 50-170 50-170-50z" fill="{G}"/>
<text x="210" y="174" text-anchor="middle" fill="#fff">2. Planos a perfil</text>
<path d="M210 40l170 50-170 50-170-50z" fill="{V}"/>
<text x="210" y="96" text-anchor="middle" fill="#fff">3. Firma, daño, conector</text>
</g></svg>"""

# Conector: dirección, llamada, campo en la tasación
CONECTOR = f"""<svg viewBox="0 0 520 200" role="img" aria-labelledby="con-t">
<title id="con-t">Una dirección entra al conector y vuelve como un campo de riesgo sísmico dentro de la ficha de tasación</title>
<rect width="520" height="200" rx="14" fill="{S}"/>
<g transform="translate(30 40)"><path d="M40 0c22 0 38 16 38 37 0 28-38 70-38 70S2 65 2 37C2 16 18 0 40 0z" fill="#fff" stroke="{G}" stroke-width="6"/><circle cx="40" cy="37" r="12" fill="{V}"/>
<text x="40" y="140" text-anchor="middle" font-family="Inter, Arial, sans-serif" font-size="13" fill="{G}" font-weight="600">Dirección</text></g>
<path d="M130 92h70m-10-10 10 10-10 10" fill="none" stroke="{V}" stroke-width="4"/>
<g transform="translate(212 46)"><rect width="100" height="92" rx="12" fill="{G}"/><text x="50" y="42" text-anchor="middle" font-family="ui-monospace, Consolas, monospace" font-size="20" fill="#fff">{{ }}</text>
<text x="50" y="68" text-anchor="middle" font-family="Inter, Arial, sans-serif" font-size="12" fill="#cfe0de">API</text>
<text x="50" y="126" text-anchor="middle" font-family="Inter, Arial, sans-serif" font-size="13" fill="{G}" font-weight="600">Conector</text></g>
<path d="M324 92h50m-10-10 10 10-10 10" fill="none" stroke="{V}" stroke-width="4"/>
<g transform="translate(386 30)"><rect width="110" height="124" rx="10" fill="#fff" stroke="{B}" stroke-width="2"/>
<rect x="12" y="14" width="60" height="8" rx="3" fill="{B}"/><rect x="12" y="30" width="86" height="8" rx="3" fill="{B}"/>
<rect x="12" y="52" width="86" height="26" rx="6" fill="#d3eadb"/><text x="55" y="70" text-anchor="middle" font-family="Inter, Arial, sans-serif" font-size="11" fill="#1d5634" font-weight="700">riesgo sísmico</text>
<rect x="12" y="88" width="70" height="8" rx="3" fill="{B}"/><rect x="12" y="102" width="50" height="8" rx="3" fill="{B}"/>
<text x="55" y="146" text-anchor="middle" font-family="Inter, Arial, sans-serif" font-size="13" fill="{G}" font-weight="600">Tu tasación</text></g>
</svg>"""

NO_ENCONTRADA = f"""<svg viewBox="0 0 320 200" role="img" aria-label="Ilustración: un edificio sobre un registro sísmico plano">
<path d="M20 170h280" stroke="{V}" stroke-width="4"/>
<g fill="none" stroke="{G}" stroke-width="10" stroke-linecap="square"><path d="M110 170V70l40-18v118"/><path d="M150 52l46 20v98" stroke="{V}"/></g>
</svg>"""
