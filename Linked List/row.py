class Nodo:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"{self.value}, {self.next}"

class row:
    def __init__(self):
        self.first = None
        self.last = None

    def insert(self, value):
        # cria um novo nodo
        value = Nodo(value)
        # cria em uma lista vazia
        if self.first == None:
            self.first = value
            self.last = value
        else:
            # faz com que o novo nodo seja o ultimo da fila
            self.last.next = value
            # faz com que o ultimo da fila referencie um novo valor
            self.last = value

    def remove(self):
        assert self.first, "Impossivel remover um valor de uma fila vazia"
        self.first = self.first.next
        if self.first == None:
            self.last = None

    def __repr__(self):
        return f"[{self.first}]"


fila = row()

print(fila)

for i in range(10):
    fila.insert(i)

print(fila)