from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import PilaVaciaError

class Pila:
    """
    Estructura LIFO (Last In, First Out) implementada sobre ListaEnlazada[cite: 1].
    Las inserciones y extracciones se realizan siempre por el inicio (cabeza) en O(1)[cite: 1].
    """
    def __init__(self):
        # Se utiliza ListaEnlazada interna encapsulada[cite: 1]
        self._items = ListaEnlazada()

    def apilar(self, dato):
        """
        Agrega un nuevo elemento en el tope de la pila[cite: 1].
        Equivale a un insertado al inicio en la ListaEnlazada[cite: 1].
        """
        self._items.insertar_al_inicio(dato)

    def desapilar(self):
        """
        Remueve y retorna el elemento que se encuentra en el tope de la pila[cite: 1].
        Lanza la excepción `PilaVaciaError` si la pila no contiene elementos[cite: 1].
        """
        if self.esta_vacia():
            raise PilaVaciaError("No hay elementos en el historial para deshacer.")[cite: 1]
        
        # Obtiene el dato ubicado en el tope (primer elemento de la lista)[cite: 1]
        tope = self.ver_tope()
        # Remueve el elemento del tope de la lista interna[cite: 1]
        self._items.eliminar(tope)
        return tope

    def ver_tope(self):
        """
        Inspecciona y devuelve el elemento del tope sin quitarlo[cite: 1].
        Lanza la excepción `PilaVaciaError` si está vacía[cite: 1].
        """
        if self.esta_vacia():
            raise PilaVaciaError("La pila está vacía.")[cite: 1]
        # Retorna directamente el valor alojado en la cabeza sin modificar la lista[cite: 1]
        return self._items._cabeza.dato

    def esta_vacia(self):
        """Verifica si la pila está vacía utilizando el método propio de ListaEnlazada[cite: 1]."""
        return self._items.esta_vacia()
