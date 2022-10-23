class Nodo:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"{self.value}, {self.next}"


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, list, previous, value):
        value = Nodo(value)
        value.next = previous.next
        previous.next = value

    def insert_start(self, list, value):
        value = Nodo(value)
        value.next = list.head
        list.head = value

    def search(self, list, value):
        chain = list.head
        while chain and chain.value != value:
            chain = chain.next
        return chain

    def remove(self, value):
        assert self.head, "Impossivel remover uma valor de uma lista vazia"
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