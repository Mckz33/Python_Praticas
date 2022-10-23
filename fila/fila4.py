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

    def reverse(self, value):
        value = Nodo(value)
        value.next = self.first
        self.first = value

    def remove(self):
        assert self.first, "Impossivel remover um valor"
        self.first = self.first.next
        if self.first == None:
            self.last = None


    def search(self, list, value):
        chain = list.first
        while chain and chain.value != value:
            chain = chain.next
        return chain

    def __repr__(self):
        return f"[{self.first}]"


fila = Fila()

for i in range(10):
    fila.insert(i)

rever = []
for i in range(10):
    if fila.search(fila, i):
        rever.append(i)

print(rever)
rever.reverse()

for i in rever:
    fila.remove()

for i in rever:
    fila.reverse(i)

print(fila)

"""while rever:
    fila.remove()

for i in rever:
    fila.insert(rever[i])

print(fila)
"""