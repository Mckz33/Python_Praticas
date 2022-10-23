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

    def remove(self):
        assert self.first, "Impossivel remover um valor"
        self.first = self.first.next
        if self.first == None:
            self.last = None

    def __repr__(self):
        return f"[{self.first}]"













"""class Fila:
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

    def remove(self):
        assert self.first, "Impossivel remover um valor de uma fila vazia"
        self.first = self.first.next
        if self.first == None:
            self.last = None

    def __repr__(self):
        return f"[{self.first}]"""


fila = Fila()
for i in range(9):
    fila.insert(i)

print(fila)

fila.remove()
fila.remove()
fila.remove()
fila.remove()
fila.remove()

print(fila)