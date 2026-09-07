# Importamos dataclass para definir clases contenedoras de datos de forma concisa.
from dataclasses import dataclass

# El decorador @dataclass crea automáticamente __init__, __repr__ y __eq__.
@dataclass
class Cancion:
    # Atributos e indicación de tipos (type hints)
    id: int             # Identificador inmutable del tema
    titulo: str         # Cadena inmutable con el título
    artista: str        # Cadena inmutable con el nombre del artista
    album: str          # Cadena inmutable con el álbum
    genero: str         # Cadena inmutable con el género
    anio: int           # Entero inmutable con el año
    duracion_seg: int   # Entero con la duración en segundos

    def formatear_duracion(self) -> str:
        """Convierte los segundos a formato MM:SS."""
        minutos = self.duracion_seg // 60
        segundos = self.duracion_seg % 60
        return f"{minutos}:{segundos:02d}"

    def mostrar_ficha_detalle(self) -> str:
        """Retorna la ficha de la canción dentro de un marco de consola."""
        duracion_fmt = self.formatear_duracion()
        return (
            f"┌────────────────────────────────────────┐\n"
            f"│  N° {self.id:<3} - {self.titulo:<26} │\n"
            f"├────────────────────────────────────────┤\n"
            f"│  Artista  : {self.artista:<26} │\n"
            f"│  Álbum    : {self.album:<26} │\n"
            f"│  Género   : {self.genero:<26} │\n"
            f"│  Año      : {self.anio:<26} │\n"
            f"│  Duración : {duracion_fmt + ' min':<26} │\n"
            f"└────────────────────────────────────────┘"
        )
