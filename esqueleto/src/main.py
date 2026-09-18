from pathlib import Path
from src.dominio.biblioteca import Biblioteca

def ver_arbol_versiones(biblio: Biblioteca) -> None:
    busqueda = input("\nIngrese el N° o Título de la canción a consultar: ").strip()
    cancion = biblio.buscar_por_criterio(busqueda)
    
    if not cancion:
        print("Canción no encontrada.")
        return

    derivadas = biblio.obtener_versiones_derivadas(cancion.id)
    print(f"\nVersiones derivadas de '{cancion.titulo}' (N° {cancion.id}):")
    
    if not derivadas:
        print(" -> No posee versiones derivadas (Caso base).")
    else:
        for cid, tipo in derivadas:
            c = biblio.buscar_por_id(cid)
            nombre = c.titulo if c else f"Canción ID {cid}"
            print(f" -> [ID {cid:<2}] {nombre:<25} (Tipo: {tipo})")

def main() -> None:
    raiz = Path(__file__).parent.parent
    biblio = Biblioteca()
    biblio.cargar_desde_csv(raiz / "data" / "canciones.csv")
    biblio.cargar_versiones(raiz / "data" / "versiones.csv")

    # resto del flujo de menú...
