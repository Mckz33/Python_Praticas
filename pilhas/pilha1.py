class Nodo:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"{self.value}, {self.next}"

class Pile:
    def __init__(self):
        self.head = None

    def append(self, value):
        value = Nodo(value)
        value.next = self.head
        self.head = value

    def pop(self):
        assert self.head, "Impossivel remover um valor de uma lista vazia"
        self.head = self.head.next


    def search(self, list, value):
        chain = list.head
        while chain and chain.value != value:
            chain = chain.next
        return chain

    def __repr__(self):
        return f"[{self.head}]"

pilha = Pile()

for i in range(0, 8):
    pilha.append(i)

print(pilha)


def valorMaior():
    for i in pilha:
        return print(pilha.search(pilha, i))

valorMaior()