class Nodo:
    """Nodo para una lista simplemente enlazada."""
    
    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente

    def __repr__(self):
        return f"Nodo({self.dato!r})"
