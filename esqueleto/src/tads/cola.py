from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import ColaVaciaError

class Cola:
    """
    Estructura FIFO (First In, First Out) implementada sobre ListaEnlazada.
    Se encola al final de la lista y se desencola por el frente (inicio de la lista).
    """
    def __init__(self):
        # Se utiliza la ListaEnlazada propia como soporte de datos
        self._items = ListaEnlazada()

    def encolar(self, dato):
        """Agrega un nuevo elemento al final (rear) de la cola."""
        self._items.insertar_al_final(dato)

    def desencolar(self):
        """
        Remueve y retorna el elemento en el frente (front) de la cola.
        Lanza ColaVaciaError si la cola está vacía.
        """
        if self.esta_vacia():
            raise ColaVaciaError("No hay elementos en la cola.")
        
        # Obtiene el dato en el frente de la cola (primer nodo de la lista)
        frente = self.ver_frente()
        # Elimina dicho elemento de la lista interna
        self._items.eliminar(frente)
        return frente

    def ver_frente(self):
        """
        Retorna el primer elemento en la fila sin quitarlo.
        Lanza ColaVaciaError si está vacía.
        """
        if self.esta_vacia():
            raise ColaVaciaError("La cola está vacía.")
        return self._items._cabeza.dato

    def esta_vacia(self):
        """Verifica si la cola se encuentra vacía."""
        return self._items.esta_vacia()
