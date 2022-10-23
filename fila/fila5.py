import random

class Processo:
    def __init__(self, id, nome, priority, wait):
        self.id = id
        self.nome = nome
        self.priority = priority
        self.wait = wait


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
        assert self.first, "Impossivel remover"
        self.first = self.first.next
        if self.first == None:
            self.last = None

    def __repr__(self):
        return f"[{self.first}]"

fila = Fila()

num = random.randrange(10)
num1 = random.randrange(10)
num2 = random.randrange(20, 50)


fila.insert({"id": num, "nome": "Window manager", "priority": num1, "wait": num2})
fila.insert({"id": num, "nome": "Window manager", "priority": num1, "wait": num2})
fila.insert({"id": num, "nome": "Window manager", "priority": num1, "wait": num2})

print(fila)