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
        assert self.top, "impossivel remover um valor de uma pilha vazia"
        self.top = self.top.previous

    def __repr__(self):
        return f"[{self.top}]"


pilha = Pile()

for i in range(5):
    pilha.append(i)

print(pilha)

pilha.pop()
pilha.pop()

print(pilha)

# class Nodo:
#     def __init__(self, value=0, next=None):
#         self.value = value
#         self.next = next
#
#     def __repr__(self):
#         return f"{self.value}, {self.next}"
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def insert(self, list, value):
#         value = Nodo(value)
#         value.next = list.head
#         list.head = value
#
#
#     def insertAfter(self, list, previous, value):
#         assert self.head, "Impossivel inserir"
#         value = Nodo(value)
#         value.next = previous.next
#         previous.next = value
#
#
#     def search(self, list, value):
#         chain = list.head
#         while chain and chain.value != value:
#             chain = chain.next
#         return chain
#
#     def remove(self, value):
#         assert self.head, "Impossivel remover um valor de uma lista vazia"
#         if self.head == value:
#             self.head = self.head.next
#         else:
#             previous = None
#             chain = self.head
#             while chain and chain.value != value:
#                 previous = chain
#                 chain = chain.next
#             if chain:
#                 previous.next = chain.next
#             else:
#                 previous.next = None
#
#
#     def __repr__(self):
#         return f"[{self.head}]"
#
#
# lista = LinkedList()
#
# for i in range(6):
#     lista.insert(lista, i)
#
# print(lista)
#
# for i in range(8):
#     if lista.search(lista, i):
#         print(f"Valor {i} encontrado!")
#     else:
#         print(f"Valor {i} não encontrado!")
#
#
# lista.insertAfter(lista, lista.head, 100)
#
# print(lista)



# class Nodo:
#     def __init__(self, value=0, next=None):
#         self.value = value
#         self.next = next
#
#     def __repr__(self):
#         return f"{self.value}, {self.next}"
#
#
# class Fila:
#     def __init__(self):
#         self.first = None
#         self.last = None
#
#     def insert(self, value):
#         value = Nodo(value)
#         if self.first == None:
#             self.first = value
#             self.last = value
#         else:
#             self.last.next = value
#             self.last = value
#
#     def remove(self):
#         assert self.first, "Impossivel remover um valor de uma fila vazia"
#         self.first = self.first.next
#         if self.first == None:
#             self.last = None
#
#     def __repr__(self):
#         return f"[{self.first}]"
#
#
# fila = Fila()
#
# for i in range(5):
#     fila.insert(i)
#
# print(fila)
#
# fila.remove()
# fila.remove()
#
# print(fila)