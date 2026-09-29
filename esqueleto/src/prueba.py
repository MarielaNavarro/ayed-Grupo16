from src.tads.lista_enlazada import ListaEnlazada
from src.tads.pila import Pila
from src.tads.cola import Cola
from src.dominio.biblioteca import Biblioteca
from src.excepciones import ColeccionLlenaError, PilaVaciaError, ColaVaciaError

def probar_todo():
    print("=== 1. Probando ListaEnlazada e Iterador ===")
    lista = ListaEnlazada()
    lista.insertar_al_final("Song A")
    lista.insertar_al_final("Song B")
    lista.insertar_al_final("Song C")
    
    # Probar recorrido con for (usa __iter__)
    elementos = [item for item in lista]
    assert elementos == ["Song A", "Song B", "Song C"], "Error en ListaEnlazada o Iterador"
    print("✓ ListaEnlazada y __iter__ funcionan correctamente.")

    print("\n=== 2. Probando Pila (Historial) ===")
    pila = Pila()
    pila.apilar("Cancion 1")
    pila.apilar("Cancion 2")
    assert pila.desapilar() == "Cancion 2"
    assert pila.desapilar() == "Cancion 1"
    
    # Probar excepción de pila vacía
    try:
        pila.desapilar()
        print("✗ ERROR: Debería lanzar PilaVaciaError")
    except PilaVaciaError:
        print("✓ PilaVaciaError capturada correctamente.")

    print("\n=== 3. Probando Cola (Cola de Reproducción) ===")
    cola = Cola()
    cola.encolar("Tema X")
    cola.encolar("Tema Y")
    assert cola.desencolar() == "Tema X"
    assert cola.desencolar() == "Tema Y"
    
    # Probar excepción de cola vacía
    try:
        cola.desencolar()
        print("✗ ERROR: Debería lanzar ColaVaciaError")
    except ColaVaciaError:
        print("✓ ColaVaciaError capturada correctamente.")

    print("\n=== 4. Probando Biblioteca con Tope (Capacidad Máxima) ===")
    biblioteca = Biblioteca(tope=2)
    biblioteca.agregar("Cancion A")
    biblioteca.agregar("Cancion B")
    
    # Probar excepción de colección llena al agregar la 3ra
    try:
        biblioteca.agregar("Cancion C")
        print("✗ ERROR: Debería lanzar ColeccionLlenaError")
    except ColeccionLlenaError:
        print("✓ ColeccionLlenaError capturada correctamente al superar el tope.")

    print("\n🎉 ¡TODAS LAS PRUEBAS PASARON CON ÉXITO!")

if __name__ == "__main__":
    probar_todo()
