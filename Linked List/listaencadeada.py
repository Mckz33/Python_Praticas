class Nodo:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"{self.value}, {self.next}"

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, list, value):
        value = Nodo(value)
        value.next = list.head
        list.head = value

    def search(self, list, value):
        chain = list.head
        while chain and chain.value != value:
            chain = chain.next
        return chain

    def remove(self, value):
        assert self.head, "Impossivel remover um valora de uma lista vazia"
        if self.head.value == value:
            self.head = self.head.next
        else:
            previous = None
            chain = self.head
            while chain and chain.value != value:
                previous = chain
                chain = chain.next
            if chain:
                previous.next = chain.next
            else:
                previous.next = None

    def __repr__(self):
        return f"[{self.head}]"


class NodoPile:
    def __init__(self, value=0, previous=None):
        self.value = value
        self.previous = previous

    def __repr__(self):
        return f"{self.value}, {self.previous}"


class Pile:
    def __init__(self):
        self.top = None

    def append(self, valor):
        value = NodoPile(valor)
        value.previous = self.top
        self.top = value

    def pop(self):
        assert self.top, "Impossivel remover um valor de uma pilha vazia"
        self.top = self.top.previous

    def __repr__(self):
        return f"[{self.top}]"

#PILHA

pilha = Pile()
for i in range(0, 8):
    pilha.append(i)

print(pilha)

pilha.pop()
pilha.pop()
pilha.pop()
pilha.pop()
print(pilha)


#LISTA
'''lista = LinkedList()
for i in range(0, 8):
    lista.insert(lista, i)
print(lista)

for i in range(0, 15):
    if lista.search(lista, i):
        print(f"Valor {i} encontrado: ")
    else:
        print(f"Valor {i} Não encontrado: ")

lista.remove(0)
lista.remove(1)
lista.remove(2)
lista.remove(3)
lista.remove(4)
print(f"Nova lista: {lista}")'''
