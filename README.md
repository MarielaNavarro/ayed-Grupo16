# TP integrador — Algoritmos y Estructuras de Datos 

## Grupo 16


### Nombre: Navarro Mariela
### usuarios de GitHub: MarielaNavarro 
### Mail: marunavarro1991@gmail.com

### Nombre: Amarilla Hernán
### usuarios de GitHub: hernanamarilla
### Mail: hernan.amarilla07@gmail.com

### Nombre: Giuliana Celeste Plasencia Cerna
### Mail: cele_1298@hotmail.com


### TEMA: Música
### URL:https://github.com/MarielaNavarro/ayed-Grupo16
 


## Informe Técnico — Entrega 1

### Tema: Biblioteca Musical

##### 1. Justificación del Dominio y Dataset

Se eligió la Biblioteca Musical como tema del catálogo. Cada registro del archivo data/canciones.csv representa una pista musical con sus metadatos principales.

Estructura del CSV

El archivo CSV contiene la siguiente cabecera:
id,titulo,artista,album,genero,anio,duracion_seg

id (int): Identificador único secuencial de la canción.

titulo (str): Título original del tema.

artista (str): Banda o solista intérprete.

album (str): Nombre del álbum.

genero (str): Género musical (Rock, Pop, Synthpop, etc.).

anio (int): Año de publicación.

duracion_seg (int): Duración en segundos.

##### 2. Análisis de Tipos de Datos: Mutabilidad e Inmutabilidad

En Python, la distinción entre tipos mutables (que pueden cambiar su contenido en memoria sin cambiar su dirección/identidad) e inmutables (cuyo valor no puede alterarse una vez creado) es fundamental para el diseño del software y el manejo de memoria.

A. Tipos Inmutables Usados (int, str, tuple)

int (id, anio, duracion_seg):

¿Por qué?: Los identificadores numéricos y los valores cuantitativos fijos no deben sufrir modificaciones accidentales por efectos secundarios (side-effects).

Justificación técnica: Un número entero en Python es inmutable. Si se realiza una operación aritmética (ej. anio + 1), Python crea un nuevo objeto en memoria en lugar de modificar el existente.

str (titulo, artista, album, genero):

¿Por qué?: Las cadenas de texto representan la identidad de los metadatos de la canción.

Justificación técnica: Al ser inmutables, se garantiza la consistencia de las búsquedas por texto y comparaciones. Ninguna función puede alterar los caracteres internos de un título existente sin generar una nueva cadena.

B. Tipos Mutables Usados (list, Cancion)

list (Catálogo / Biblioteca principal):

¿Por qué?: El catálogo en memoria necesita ser dinámico.

Justificación técnica: list es un tipo mutable en Python. Permite agregar (.append()), eliminar o reordenar elementos in-place (en la misma dirección de memoria). Esto prepara la estructura para la futura implementación de la ListaEnlazada propia exigida en la Entrega 3.

Clase Cancion (@dataclass):

¿Por qué?: Representa la entidad de dominio.

Justificación técnica: Las instancias de clases personalizadas en Python son mutables por defecto. Esto permite que en entregas futuras se puedan actualizar atributos del estado de una canción (por ejemplo, contador de reproducciones, calificación o estado de favoritos) sin necesidad de recrear el objeto completo.

#### 3. Registro de Operaciones Implementadas (E1)

Carga desde CSV: Uso de csv.DictReader con lectura robusta de rutas mediante pathlib.

Listado de Catálogo: Recorrido iterativo imprimiendo una tabla en consola con formato de columnas de ancho fijo y conversión de segundos a minutos (MM:SS).

Detalle de Ítem: Búsqueda por ID numérico o por Título de la canción, mostrando una ficha gráfica con marco unicode.

## Estructura del repositorio 

 ###### esqueleto/
###### ├── data/
###### │   └── canciones.csv          # Dataset en texto/CSV
###### ├── docs/
###### │   ├── INFORME.md             # Justificaciones técnicas y análisis de tipos
###### │   ├── DECLARACION_IA.md      # Registro de uso de herramientas de IA
###### │   ├── GUIA_PASO_A_PASO.md    # Guía didáctica explicada línea por línea
###### │   └── CHECKLIST_ENTREGA_1.md # Pasos finales para entrega
###### ├── src/
###### │   ├── dominio/
###### │   │   └── cancion.py         # Modelo de dominio de la entidad Cancion
###### │   └── main.py                # Punto de entrada y CLI
###### └── README.md                  # Presentación principal

## ¿Cómo Ejecutar la Entrega 1?

Desde la carpeta principal esqueleto/, ejecutar en consola:

