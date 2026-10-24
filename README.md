# web-antesismo

Sitio v0 de antesismo, due diligence sísmico en días, desde los planos municipales. Basado en el Perfil Bío-Sísmico 3.0 de IEC Ingeniería, con crédito abierto a sus autores.

Sitio estático publicado con Azure Static Web Apps. Cada push a `main` despliega en el entorno de prueba.

## Estructura

| Ruta | Página |
|---|---|
| `/` | Inicio |
| `/due-diligence/` | Due diligence inmobiliario |
| `/tasadoras/` | Tasadoras con IA, proptech y bancos |
| `/caso/` | Caso demostrativo, edificio de 1963 anonimizado |
| `/perfil-bio-sismico/` | Método y crédito |
| `/parametros-sismicos/` | Cómo funciona |
| `/precios/` | Precios y pre-venta |
| `/validadores/` | Validadores e inversionistas |
| `/quien-esta-detras/` | Biografía y responsabilidad del Ing. Rodney Bellido de Luna |
| `/legal/` | Términos de uso y política de privacidad (Ley 19.628 y Ley 21.719), borrador para revisión legal |

Las páginas se generan con `fuente/construir.py` (Python 3.12, sin dependencias):

```
python fuente/construir.py
```

El generador lee `fuente/datos/` (perfil de 21 indicadores y geometría del caso, sin datos que identifiquen el edificio) y escribe las páginas, `assets/js/datos-caso.js`, `sitemap.xml`, `robots.txt` y `staticwebapp.config.json`. Las figuras del caso (plantas, modelo 3D, modos, bandas y daño) se dibujan en el navegador con `assets/js/perfil.js`. Las ilustraciones están en `fuente/ilustraciones.py`.

## Versión de revisión

En `fuente/construir.py`:

- `REVISION = True` muestra el aviso de versión de revisión.
- `OCULTO = True` agrega `noindex, noai` en cada página y en la cabecera `X-Robots-Tag`, y cierra `robots.txt` a todos los rastreadores, con los de IA nombrados uno por uno. Se cambia a `False` solo cuando Rodney lo indique.
- `CORREO` es el correo de contacto del pie, de la página de quién está detrás y de los formularios.

Los formularios no envían datos a ningún servidor: abren el programa de correo del visitante con el mensaje listo. Los textos legales y la biografía están en `fuente/legal.py`.

## Marca

Recursos del kit de marca antesismo v1: `assets/marca/`, `assets/social/`, favicons y `site.webmanifest` en la raíz. Grafito `#263036`, verde `#297e7a`, Inter con Arial de respaldo.
