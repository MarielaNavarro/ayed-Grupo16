import csv
import os
from typing import List
from src.dominio.modelos import Cancion

class ManejadorCSV:
    @staticmethod
    def cargar_catalogo(ruta_csv: str) -> List[Cancion]:
        """Lee un archivo CSV y devuelve una lista de objetos Cancion."""
        if not os.path.exists(ruta_csv):
            raise FileNotFoundError(f"El archivo {ruta_csv} no existe.")

        catalogo = []
        with open(ruta_csv, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                # Convertir la columna de versiones (separada por ';') en una lista de enteros
                versiones_raw = fila.get("versiones", "")
                versiones_list = (
                    [int(v) for v in versiones_raw.split(";") if v.strip().isdigit()]
                    if versiones_raw else []
                )

                # Crear la instancia de Cancion
                cancion = Cancion(
                    id=int(fila["id"]),
                    titulo=fila["titulo"],
                    artista=fila["artista"],
                    album=fila["album"],
                    genero=fila["genero"],
                    duracion_segundos=int(fila["duracion_segundos"]),
                    anio=int(fila["anio"]),
                    versiones=versiones_list
                )
                catalogo.append(cancion)

        return catalogo

    @staticmethod
    def guardar_catalogo(ruta_csv: str, catalogo: List[Cancion]) -> None:
        """Guarda la lista de canciones en un archivo CSV."""
        with open(ruta_csv, mode="w", encoding="utf-8", newline="") as archivo:
            campos = ["id", "titulo", "artista", "album", "genero", "duracion_segundos", "anio", "versiones"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            
            escritor.writeheader()
            for cancion in catalogo:
                versiones_str = ";".join(map(str, cancion.versiones))
                escritor.writerow({
                    "id": cancion.id,
                    "titulo": cancion.titulo,
                    "artista": cancion.artista,
                    "album": cancion.album,
                    "genero": cancion.genero,
                    "duracion_segundos": cancion.duracion_segundos,
                    "anio": cancion.anio,
                    "versiones": versiones_str
                })
