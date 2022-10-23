class Nodo:
    def __init__(self, value=0, nextvalue=None):
        self.value = value
        self.next = nextvalue

    def __repr__(self):
        return f"{self.value}, {self.next}"

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return "[" + str(self.head) + "]"

def append(lista, newValor):
    newValor = Nodo(newValor)
    newValor.next = lista.head
    lista.head = newValor


lista = LinkedList()
i = 0
while i < 4:
    temp = int(input("Número: "))
    append(lista, temp)
    i += 1

print(lista)