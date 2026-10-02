Informe del TP
Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

1. Grupo y tema
Tema:Biblioteca musical
Por qué lo eligieron (5–8 líneas): Elegimos el tema de la Biblioteca Musical porque fue la opción propuesta por la cátedra que generó un interés unánime y entusiasmó a los tres integrantes del equipo, brindándonos una temática motivadora para trabajar en conjunto.
2. Modelo
Qué es un ítem del catálogo. Qué es mutable y qué no (E1). Cómo se relacionan catálogo, colección principal, pila y cola. Atributos Inmutables (por diseño conceptual):

Un ítem del catálogo es un objeto o entidad que representa una obra musical dentro del sistema (instancia de la clase Cancion). Encapsula todos los atributos representativos de un tema: identificador único (id), título (titulo), artista (artista), álbum (album), género (genero), año de lanzamiento (anio) y duración en segundos (duracion_seg).

Atributos Inmutables:
id: El identificador numérico de la canción no debe cambiar a lo largo del ciclo de vida del objeto, ya que garantiza la identidad única del tema en la biblioteca y en las relaciones de versiones.

titulo, artista, album, genero, anio: Propiedades descriptivas que caracterizan la obra original.

Atributos Mutables:
En una aplicación extensible, campos como duracion_seg o metadatos de estado/reproducción pueden ser susceptibles a modificaciones. Sin embargo, en el modelo de dominio inicial (Cancion), la entidad se comporta como un contenedor de datos principalmente inmutable instanciado desde el archivo CSV.

Relación entre Catálogo, Colección Principal, Pila y Cola
Catálogo / Colección Principal: Es la estructura central que almacena todas las instancias de Cancion cargadas desde la fuente de datos (canciones.csv). Representa el repertorio completo disponible. Funciona como la "fuente de verdad" sobre la cual se realizan búsquedas, listados y consultas recursivas de versiones.

Pila (LIFO - Last In, First Out): Representa un historial de reproducción o historial de navegación. Las canciones consultadas o reproducidas recientemente se apilan en la cima, permitiendo acciones como "volver a la canción anterior" (desapilar / pop).

Cola (FIFO - First In, First Out): Representa la lista de reproducción en cola (playqueue). Las canciones se encolan al final (enqueue) y se procesan/reproducen en el orden estricto de llegada desde el frente (dequeue).

```text
+-------------------------------------------------------------------+
|                            Biblioteca                             |
|                      (Catálogo / Contenedor)                      |
+-------------------------------------------------------------------+
| - canciones: list[Cancion] <-- Colección Principal                |
| - versiones_map: dict[int, list] <-- Grafo de Versiones (E2)      |
+-------------------------------------------------------------------+
| + cargar_desde_csv(ruta)                                         |
| + cargar_versiones(ruta)                                          |
| + buscar_por_id(id): Cancion                                      |
| + obtener_versiones_derivadas(id): list <-- Algoritmo Recursivo   |
+-------------------------------------------------------------------+
                                 |
                                 | 1..* contiene
                                 v
+-------------------------------------------------------------------+
|                             Cancion                               |
+-------------------------------------------------------------------+
| + id: int (Inmutable)                                             |
| + titulo: str (Inmutable)                                         |
| + artista: str (Inmutable)                                        |
| + album: str (Inmutable)                                          |
| + genero: str (Inmutable)                                         |
| + anio: int (Inmutable)                                           |
| + duracion_seg: int (Mutable / Atributo)                          |
+-------------------------------------------------------------------+
| + formatear_duracion(): str                                       |
| + mostrar_ficha_detalle(): str                                    |
+-------------------------------------------------------------------+
```


    [ Historial / Navegación ]            [ Queue de Reproducción ]
      +--------------------+                +--------------------+
      |     Pila (LIFO)    |                |     Cola (FIFO)    |
      +--------------------+                +--------------------+
      | [Cancion N] (Top)  |                | [Cancion 1] (Head) |
      | [Cancion 2]        |                | [Cancion 2]        |
      | [Cancion 1]        |                | [Cancion 3] (Tail) |
      +--------------------+                +--------------------+
3. Recursión (E2)
Función: obtener_versiones_derivadas(id_cancion)
Caso base: Ocurre cuando la canción consultada no posee versiones derivadas registradas como claves en el diccionario versiones_map (o su lista de derivadas asociadas está vacía). En este caso, la función retorna una lista vacía [].
Caso recursivo: Retorna una lista construida con las derivadas directas inmediatas más el resultado de invocar de manera recursiva a obtener_versiones_derivadas(id_derivado) para cada una de las versiones hijas.

Traza de un ejemplo real del datasetTomando los datos de data/canciones.csv (donde el ID 1 es "Bohemian Rhapsody") y data/versiones.csv (donde se encuentra el registro 62,1,live): Consulta: Buscar las versiones derivadas de "Bohemian Rhapsody" (id = 1). Llamada 1: obtener_versiones_derivadas(1)Busca directas de 1 en versiones_map: Encuentra [(62, 'live')]. Evalúa caso recursivo: [(62, 'live')] + obtener_versiones_derivadas(62). Llamada 2: obtener_versiones_derivadas(62)Busca directas de 62 en versiones_map: No encuentra ninguna derivada ([]). Alcanza el Caso base: Devuelve []. Desapilado y Resolución:Sustituye el retorno de la llamada 2 en la llamada 1: [(62, 'live')] + []. Resultado final: [(62, 'live')] (ID 62 "Bohemian Rhapsody - Live").

4. TADs (E3)
TAD	Operaciones	Invariante
ListaEnlazada		
Pila		
Cola		
Dónde se usa cada uno en el dominio.

5. Complejidad (E4)
Operación	Tiempo	Espacio	Por qué
Mediciones (time.perf_counter):

Operación	n	segundos
6. Persistencia (E5)
Layout del registro binario (campos, struct, anchos):
Header:
Cómo se actualiza un registro por posición:
7. Reparto de trabajo (E6)
Integrante	Qué hizo	Qué puede defender

# Informe de Desarrollo - Entrega 3: TADs Lineales y Excepciones

## 1. Justificación y Análisis de Complejidad Temporal

### ListaEnlazada (`src/tads/lista_enlazada.py`)
* **`insertar_al_inicio` — $O(1)$**: Crea un `Nodo` y reconecta el puntero `_cabeza`. La operación no depende de la cantidad de elementos $n$.
* **`insertar_al_final` — $O(n)$**: Recorre la lista desde `_cabeza` hasta el último nodo (`siguiente is None`) para añadir el nuevo nodo.
* **`eliminar` — $O(n)$**: En el peor caso, recorre toda la lista para encontrar el elemento a desenganchar.
* **`buscar` — $O(n)$**: Recorre los elementos uno a uno evaluando el criterio o dato solicitado.
* **`__len__` — $O(1)$**: Mantiene un contador `_cant` que se incrementa o decrementa en cada modificación.

### Pila (`src/tads/pila.py`)
* **`apilar` — $O(1)$**: Delega en `insertar_al_inicio` de `ListaEnlazada`.
* **`desapilar` — $O(1)$**: Remueve y retorna el elemento en `_cabeza`.
* **`ver_tope` — $O(1)$**: Consulta el valor contenido en `_cabeza.dato`.

### Cola (`src/tads/cola.py`)
* **`encolar` — $O(n)$**: Delega en `insertar_al_final` de `ListaEnlazada`.
* **`desencolar` — $O(1)$**: Remueve y retorna el primer elemento (`_cabeza`).
* **`ver_frente` — $O(1)$**: Consulta el valor contenido en `_cabeza.dato`.

## 2. Estrategia de Manejo de Excepciones
Se implementaron excepciones específicas (`ArchivoInvalidoError`, `ElementoNoEncontradoError`, `PilaVaciaError`, `ColaVaciaError`) heredando de `Exception`. Esto permite desacoplar los errores del dominio e impedimento de fallos catastróficos en la interfaz CLI, garantizando respuestas claras al usuario.
