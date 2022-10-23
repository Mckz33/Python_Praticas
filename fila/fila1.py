#– Crie um nó padrão da fila.
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
        # Crie uma função de inicialização da fila vazia
        value = Nodo(value)
        # Crie uma função push que cria e insere um novo nó para o final da fila.
        if self.first == None:
            self.first = value
            self.last = value
        else:
            self.last.next = value
            self.last = value
    # Crie uma função pop que remove o primeiro elemento da fila
    def remove(self):
        assert self.first, "impossivel remover um valor de uma fila vazia"
        self.first = self.first.next
        if self.first == None:
            self.last = None

    def __repr__(self):
        return f"[{self.first}]"