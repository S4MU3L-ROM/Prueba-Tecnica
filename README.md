# Documentación prueba tecnica desarrollador junior

Este proyecto se realiza para la presentación de la prueba técnica para la empresa Verticcal, las librerias utilizadas en el código son: 
- FastApi: Creación de api
- httpx: Consumo de api
- pydantic: Validación de datos 
- json: lectura de json
## Tabla de Contenidos

- [Instalación](#instalación)
  - [Requisitos Previos](#requisitos-previos)
  - [Clonar el Repositorio](#clonar-el-repositorio)
  - [Entorno Virtual](#entorno-virtual)
- [Uso](#uso)
- [Ejercicio extra](#Ejercicio-extra)

## Instalación

A continuación, se detallan los pasos para configurar el entorno y ejecutar el proyecto.

### Requisitos Previos

Asegúrate de tener instalado:

- **Python 3.8+**: Puedes descargarlo desde [Python.org](https://www.python.org/downloads/).
- **Git**: Necesario para clonar el repositorio. Puedes descargarlo desde [Git](https://git-scm.com/).

### Clonar el Repositorio

Primero, clona el repositorio del proyecto desde GitHub. Puedes hacerlo ejecutando el siguiente comando en tu terminal:

```sh
git clone [https://github.com/usuario/nombre-del-proyecto.git](https://github.com/S4MU3L-ROM/Prueba-Tecnica.git)
```

Despues de clonar el repositorio, navegas a la carpeta donde clonaste el repositorio
```sh
cd ubicacion/del/proyecto
```
### Entorno Virtual
1. Dentro de la ubicación de la carpeta, creamos un entorno virtual
   ```sh
    python -m venv venv
   ```
2. Activamos el entorno virtual
   ```sh
    venv\Scripts\activate
   ```
3. Instalamos las dependencias
   ```sh
    pip install -r requirements.txt
   ```
### Uso
1. Para poder poner a trabaja la api con FastApi, ejecutaremos el siguiente comando
   ```sh
    uvicorn api.main:app --reload
   ```
2. Para poder utilizar la api en local se recomienda el uso de postman o de thunder esta ultima es una extensión en visual studio code.
3. Las siguientes urls son los get y post del codigo
#### Get
  *Endpoint GET que devuelve todos los animes más populares*
  ```sh
  http://127.0.0.1:8000/top-anime
  ```
  *Endpoint GET que devuelve solo los títulos de los animes*
   ```sh
    http://127.0.0.1:8000/top-anime-title
   ```
  *Endpoint GET que devuelve la información de paginación*
  ```sh
   http://127.0.0.1:8000/top-anime-pagination
  ```
  #### Post
  *Endpoint POST que permite buscar un anime por su título*
   ```sh
    http://127.0.0.1:8000/search-title
   ```
  Para el post vamos al apartado Body
  ![image](https://github.com/user-attachments/assets/8950990d-2f93-45b5-892d-fde6b043e94f)

  Uno vez dentro de las llaves que aprecen vamos a poner
   ```sh
      "title" : "nombre del anime"
   ```
   Dentro de las opciones de los animes tenemos las siguientes
   - Gintama: The Final
   - Look Back
   - Code Geass: Hangyaku no Lelouch R2
   - Hunter x Hunter (2011)
   - Clannad: After Story
   - Kusuriya no Hitorigoto
   - One Piece Fan Letter
  ### Ejercicio extra
  Para la entrega del ejercicio extra se hizo un archivo llamado datos.py donde se ejecuta el archivo normalmente con el       boton run
