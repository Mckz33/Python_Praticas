class Nodo:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"{self.value}, {self.next}"

class Fila:
    def __init__(self):
        self.first = None
        self.last = None

    def insert(self, value):
        value = Nodo(value)
        if self.first == None:
            self.first = value
            self.last = value
        else:
            self.last.next = value
            self.last = value

    def search(self, list, value):
        chain = list.first
        while chain and chain.value != value:
            chain = chain.next
        return chain

    # Crie uma função que percorre e imprime todos os elementos da fila.
    def buscar(self, valor):
        for i in range(valor):
            if fila.search(fila, i):
                print(f"Valor {i} encontrado na posição!")
            else:
                print(f"Valor {i} é invalido!")

    def __repr__(self):
        return f"[{self.first}]"


fila = Fila()

fila.insert(2)
fila.insert(3)
fila.insert(4)
fila.insert(5)
fila.insert(6)

print(fila.buscar(10))