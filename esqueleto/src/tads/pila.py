from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import PilaVaciaError

class Pila:
    """
    Estructura LIFO (Last In, First Out) implementada sobre ListaEnlazada.
    Las inserciones y extracciones se realizan siempre por el inicio (cabeza) en O(1).
    """
    def __init__(self):
        # Se utiliza ListaEnlazada interna encapsulada
        self._items = ListaEnlazada()

    def apilar(self, dato):
        """
        Agrega un nuevo elemento en el tope de la pila.
        Equivale a un insertado al inicio en la ListaEnlazada.
        """
        self._items.insertar_al_inicio(dato)

    def desapilar(self):
        """
        Remueve y retorna el elemento que se encuentra en el tope de la pila.
        Lanza la excepción PilaVaciaError si la pila no contiene elementos.
        """
        if self.esta_vacia():
            raise PilaVaciaError("No hay elementos en el historial para deshacer.")
        
        # Obtiene el dato ubicado en el tope (primer elemento de la lista)
        tope = self.ver_tope()
        # Remueve el elemento del tope de la lista interna
        self._items.eliminar(tope)
        return tope

    def ver_tope(self):
        """
        Inspecciona y devuelve el elemento del tope sin quitarlo.
        Lanza la excepción PilaVaciaError si está vacía.
        """
        if self.esta_vacia():
            raise PilaVaciaError("La pila está vacía.")
        # Retorna directamente el valor alojado en la cabeza sin modificar la lista
        return self._items._cabeza.dato

    def esta_vacia(self):
        """Verifica si la pila está vacía utilizando el método propio de ListaEnlazada."""
        return self._items.esta_vacia()
