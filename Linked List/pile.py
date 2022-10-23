class Nodo:
    def __init__(self, value=0, previous=None):
        self.value = value
        self.previous = previous

    def __repr__(self):
        return f"{self.value}, {self.previous}"


class Pile:
    def __init__(self):
        self.top = None

    def append(self, value):
        value = Nodo(value)
        value.previous = self.top
        self.top = value

    def pop(self):
        assert self.top, "Impossivel remover um valor de uma pilha vazia"
        self.top = self.top.previous

    def __repr__(self):
        return f"[{self.top}]"


pilha = Pile()
for i in range(0, 8):
    pilha.append(i)

print(pilha)

pilha.pop()
pilha.pop()
pilha.pop()
pilha.pop()
print(pilha)