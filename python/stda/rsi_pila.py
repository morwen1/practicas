



"""
curso de estructuras de datos con python

"""
class Pila():
    """
    modulo creado por morwen
    """

    def __init__(self):
        self.items = []
    

    def estaVacia (self):
        return self.items == []
    
    def incluir(self,item):
        self.items.append(item)

    def extraer(self):
        return self.items.pop()
    
    def inspeccionar(self):
        return self.items[len(self.items)-1]

    def tamano(self):
        return len(self.items)

    def imprimir(self):
        print(self.items)
