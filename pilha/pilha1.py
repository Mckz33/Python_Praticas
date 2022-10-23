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
        assert self.top, "Impossivel"
        self.top = self.top.previous

    def search(self, value):
        cont = []
        chain = self.top
        while chain and chain.value != value:
            chain = chain.previous
            cont.append(chain)
        return max(cont)


    def __repr__(self):
        return f"[{self.top}]"


pilha = Pile()

cont = 0
for i in range(5):
    pilha.append(i)
    cont += 1
print(pilha)

print(pilha.search(pilha))

