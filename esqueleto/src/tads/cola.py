from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import ColaVaciaError

class Cola:
    """
    Estructura FIFO (First In, First Out) implementada sobre ListaEnlazada[cite: 1].
    Se encola al final de la lista y se desencola por el frente (inicio de la lista)[cite: 1].
    """
    def __init__(self):
        # Se utiliza la ListaEnlazada propia como soporte de datos[cite: 1]
        self._items = ListaEnlazada()

    def encolar(self, dato):
        """
        Agrega un nuevo elemento al final (rear) de la cola[cite: 1].
        """
        self._items.insertar_al_final(dato)

    def desencolar(self):
        """
        Remueve y retorna el elemento en el frente (front) de la cola[cite: 1].
        Lanza `ColaVaciaError` si la cola está vacía[cite: 1].
        """
        if self.esta_vacia():
            raise ColaVaciaError("No hay elementos en la cola.")[cite: 1]
        
        # Obtiene el dato en el frente de la cola (primer nodo de la lista)[cite: 1]
        frente = self.ver_frente()
        # Elimina dicho elemento de la lista interna[cite: 1]
        self._items.eliminar(frente)
        return frente

    def ver_frente(self):
        """
        Retorna el primer elemento en la fila sin quitarlo[cite: 1].
        Lanza `ColaVaciaError` si está vacía[cite: 1].
        """
        if self.esta_vacia():
            raise ColaVaciaError("La cola está vacía.")[cite: 1]
        return self._items._cabeza.dato

    def esta_vacia(self):
        """Verifica si la cola se encuentra vacía[cite: 1]."""
        return self._items.esta_vacia()
