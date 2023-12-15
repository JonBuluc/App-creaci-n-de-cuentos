
# Cuentos para toodos

## Descripción

La aplicacion usa inteligencia artificial para poder crear cuentos segun las necesidades que se tengan esta enfocado en niños pero no le hacemos el feo a los adultos que lo usen

## Características Principales

- Creacion de usuarios (pendiente)
- Ver todas las historias creadas
- Ver las historias populares y busqueda por etiqueta (pendiente)
- uso de ia para generar los cuentos

## Requisitos Previos

- Se necesita una api key de open ia cuestan a partir de 5 dolares pero no consume practicamente nada

## Instalación

Si tienes abierta la carpeta del repositorio desde donde ejecutes el programa usa el siguiente comando es recomendable tener un entorno virtual

```bash
pip install -r requirements.txt
```
en caso de que quieras usarlo en tu instalacion local de python puedes usar el siguiente comando

```bash
pip install --no-deps -r requirements.txt
```

## Configuración

Para poder usar la aplicacion debes de ejecutar run.py y abrir tu navegador en tu direccion ip en el puerto 5000 ademas de eso debes de poner tu apy key en el archivo accionesChatGPT.py en la siguiente linea
```python
def generar_cuento(titulo, categoria, duracion, modelo="gpt-3.5-turbo"):
    client = OpenAI(api_key="")
```

tambien en este archivo puedes modificar la respuesta de chat gpt
## Uso

Para empezar a usar la app unicamente tienes que darle click al boton crear historia y en la nueva pagina llenar todos los campos


<span>![</span><span>creacion de un cuento</span><span>]</span><span>(</span><span>https://github.com/JonBuluc/App-creaci-n-de-cuentos/blob/main/foto1.png</span><span>)</span>


se tarda un poco en lo que hace la solicitud a open ia una vez que se realice podras ver el boton para regresar al index


<span>![</span><span>vista de los cuentos</span><span>]</span><span>(</span><span>https://github.com/JonBuluc/App-creaci-n-de-cuentos/blob/main/foto2.png</span><span>)</span>

## Estructura del Proyecto

Descripción de la estructura de archivos y carpetas en el proyecto.

```
.
├── app
│   ├── __init__.py
│   ├── accionesChatGPT.py
│   ├── eliminar.py
│   ├── models.py
│   ├── routes.py
│   ├── static
│   │   ├── css
│   │   │   └── estilos.css
│   │   └── js
│   │       └── script.js
│   └── templates
│       ├── crear-ia.html
│       └── index.html
├── instance
│   └── datos.db
├── .gitignore
├── requerimientos.txt
└── run.py
```

## Por si perdura

La creacion de la app tuvo muchos conocimientos interesantes en caso de que el repositorio sobreviviera y tienes duda o necesitas ayuda en algo puedes mandar mensaje sin problema



---

