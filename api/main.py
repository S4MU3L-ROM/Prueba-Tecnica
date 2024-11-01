import httpx
from fastapi import HTTPException, FastAPI
from pydantic import BaseModel


# Función que utilizamos para extraer datos de la API Jikan
async def fetch_anime_data():
    url = "https://api.jikan.moe/v4/top/anime"  # URL de la API Jikan para obtener los animes más populares
    async with httpx.AsyncClient() as client:  # Creamos un cliente HTTP asincrónico
        try:
            response = await client.get(url)  # Realizamos la solicitud GET a la URL
            response.raise_for_status()  # Verificamos si la respuesta tiene un código de estado exitoso
            return response.json()  # Retornamos el JSON de la respuesta
        except httpx.HTTPStatusError as err:
            # Manejo de errores HTTP
            return HTTPException(status_code=err.response.status_code, detail=str(err))
        except httpx.RequestError as err:
            # Manejo de errores de solicitud
            return HTTPException(status_code=400, detail="Request error")
        except httpx.TimeoutException as err:
            # Manejo de errores de tiempo de espera
            return HTTPException(status_code=408, detail="Request timed out")


# Inicializamos FastAPI
app = FastAPI()


# Endpoint GET que devuelve todos los animes más populares
@app.get("/top-anime")
async def read_top_anime():
    anime_data = (
        await fetch_anime_data()
    )  # Llamamos a la función para obtener los datos de anime
    data = anime_data["data"]  # Extraemos la lista de animes del JSON
    return data  # Devolvemos los datos extraídos


# Endpoint GET que devuelve solo los títulos de los animes
@app.get("/top-anime-title")
async def read_top_anime():
    anime_data = await fetch_anime_data()
    data = anime_data["data"]
    titles = [anime["title"] for anime in data]
    return titles  # Devolvemos los títulos


# Endpoint GET que devuelve la información de paginación
@app.get("/top-anime-pagination")
async def read_top_anime():
    anime_data = await fetch_anime_data()
    data = anime_data["pagination"]  # Extraemos los datos de paginación
    return data  # Devolvemos los datos de paginación


# Modelo de datos para la consulta de búsqueda
class Query(BaseModel):
    title: str  # Definimos un campo "title" de tipo string


# Endpoint POST que permite buscar un anime por su título
@app.post("/search-title/")
async def search(query: Query):
    anime_data = (
        await fetch_anime_data()
    )  # Llamamos a la función para obtener los datos de anime
    for anime in anime_data["data"]:  # Recorremos la lista de animes
        if (
            anime["title"].lower() == query.title.lower()
        ):  # Comparamos los títulos sin diferenciar mayúsculas y minúsculas
            # Si encontramos el anime, devolvemos la información relevante
            return {
                "message": "Anime found",
                "anime": anime["title"],
                "type": anime["type"],
                "source": anime["source"],
                "episodes": anime["episodes"],
            }
    # Si no se encuentra, lanzamos una excepción
    raise HTTPException(status_code=404, detail="Anime not found")
