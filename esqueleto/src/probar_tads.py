# probar_tads.py

# Si creaste excepciones.py, asegurate de tenerlas creadas antes de ejecutar este script
try:
    from src.tads.lista_enlazada import ListaEnlazada
    from src.tads.pila import Pila
    from src.tads.cola import Cola
    from src.excepciones import PilaVaciaError, ColaVaciaError
except ImportError:
    # Si aún no tenés excepciones.py, podés probar importando sin las excepciones
    from src.tads.lista_enlazada import ListaEnlazada
    from src.tads.pila import Pila
    from src.tads.cola import Cola


def probar_lista():
    print("--- PRUEBA LISTA ENLAZADA ---")
    lista = ListaEnlazada()
    
    lista.insertar_al_inicio("Canción B")
    lista.insertar_al_inicio("Canción A")
    lista.insertar_al_final("Canción C")

    print(f"Largo de la lista (esperado 3): {len(lista)}")
    print("Elementos en la lista:")
    for elem in lista:
        print(f" - {elem}")

    print("\nBuscando 'Canción B':", lista.buscar("Canción B"))
    
    lista.eliminar("Canción B")
    print("\nLuego de eliminar 'Canción B':")
    for elem in lista:
        print(f" - {elem}")
    print(f"Nuevo largo (esperado 2): {len(lista)}\n")


def probar_pila():
    print("--- PRUEBA PILA (LIFO) ---")
    pila = Pila()
    
    pila.apilar("Acción 1")
    pila.apilar("Acción 2")
    pila.apilar("Acción 3")

    print(f"Tope de la pila (esperado 'Acción 3'): {pila.ver_tope()}")
    print(f"Desapilado (esperado 'Acción 3'): {pila.desapilar()}")
    print(f"Nuevo tope (esperado 'Acción 2'): {pila.ver_tope()}")
    print(f"Largo actual (esperado 2): {len(pila)}\n")


def probar_cola():
    print("--- PRUEBA COLA (FIFO) ---")
    cola = Cola()
    
    cola.encolar("Cliente 1")
    cola.encolar("Cliente 2")
    cola.encolar("Cliente 3")

    print(f"Frente de la cola (esperado 'Cliente 1'): {cola.ver_frente()}")
    print(f"Desencolado (esperado 'Cliente 1'): {cola.desencolar()}")
    print(f"Nuevo frente (esperado 'Cliente 2'): {cola.ver_frente()}")
    print(f"Largo actual (esperado 2): {len(cola)}\n")

def probar_excepciones():
    print("--- PRUEBA EXCEPCIONES ---")
    pila = Pila()
    try:
        pila.desapilar()
    except PilaVaciaError as e:
        print(f"✓ Excepción PilaVaciaError capturada con éxito: {e}")

    cola = Cola()
    try:
        cola.desencolar()
    except ColaVaciaError as e:
        print(f"✓ Excepción ColaVaciaError capturada con éxito: {e}")
    print()
if __name__ == "__main__":
    probar_lista()
    probar_pila()
    probar_cola()
