# ==============================================================================
# Módulo: recursion.py
# Ubicación: src/algoritmos/recursion.py
# Descripción: Algoritmo recursivo para recorrer el árbol de versiones derivadas.
# ==============================================================================

def buscar_cancion_por_id(id_cancion: int, biblioteca: list):
    """Busca linealmente y retorna el objeto Cancion correspondiente al ID especificado."""
    for cancion in biblioteca:
        if cancion.id == id_cancion:
            return cancion
    return None

def buscar_derivadas_directas(cancion_original: int, biblioteca: list) -> list:
    """Retorna todas las canciones cuya propiedad id_cancion_original coincide con el ID dado."""
    derivadas = []
    for cancion in biblioteca:
        if cancion.cancion_original == cancion_original:
            derivadas.append(cancion)
    return derivadas

def listar_versiones_recursivas(id_cancion: int, biblioteca: list, nivel: int = 0) -> int:
    """
    Recorre e imprime en pantalla el árbol jerárquico de versiones derivadas.

    Parámetros:
        id_cancion (int): ID de la canción a partir de la cual buscar derivadas.
        biblioteca (list): Lista completa de objetos Cancion.
        nivel (int): Profundidad actual en la jerarquía (usado para indentación visual).

    Retorna:
        int: Total de versiones acumuladas en la rama.
    """
    # 1. Búsqueda de derivados directos
    derivadas = buscar_derivadas_directas(id_cancion, biblioteca)

    # 2. CASO BASE EXPLÍCITO: Si no tiene derivados, se corta la recursión.
    if not derivadas:
        return 0

    # 3. CASO RECURSIVO: Si tiene derivados, procesa cada uno e ingresa recursivamente.
    total_derivadas = 0

    for derivada in derivadas:
        total_derivadas += 1
        indentacion = "  │  " * nivel + "  ├── "
        print(f"{indentacion}[ID {derivada.id}] {derivada.titulo} ({derivada.artista}, {derivada.anio})")
        
        # LLAMADA RECURSIVA: Profundiza en la subrama de la canción derivada
        total_derivadas += listar_versiones_recursivas(derivada.id, biblioteca, nivel + 1)

    return total_derivadas
