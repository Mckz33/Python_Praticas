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
        assert self.head, "Impossivel acrescentar em uma lista vazia"
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
        assert self.head, "impossivel remover um valor de uam lista vazia"
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


lista = LinkedList()

lista.insert_start(lista, 1)
lista.insert_start(lista, 5)
lista.insert_end(lista, lista.head, 2)
lista.insert_end(lista, lista.head, 3)
lista.insert_end(lista, lista.head, 4)

print(lista)

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
#     def insert_end(self, list, previous, value):
#         assert previous, "Nodo anterior precisa existir na lista"
#         value = Nodo(value)
#         value.next = previous.next
#         previous.next = value
#
#     def insert_start(self, list, value):
#         value = Nodo(value)
#         value.next = list.head
#         list.head = value
#
#     def search(self, list, value):
#         chain = list.head
#         while chain and chain.value != value:
#             chain = chain.next
#         return chain
#
#     def remove(self, value):
#         assert self.head, "impossivel remover um valor de uma lista vazia"
#         if self.head.value == value:
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
#     def __repr__(self):
#         return f"[{self.head}]"
#
#
#
# class Pile:
#     def __init__(self):
#         self.previous = None
#
#     def append(self, value):
#         value = Nodo(value)
#         value.next = self.previous
#         self.previous = value
#
#     def pop(self):
#         assert self.previous, "Impossivel remover um valor de uma lista vazia"
#         self.previous = self.previous.next
#
#     def __repr__(self):
#         return f"[{self.previous}]"
#
# '''Para ser possivel organizar em ordem o insert_start deve-se iniciar e finalizar para ficar em ordem'''
# lista = LinkedList()
#
# lista.insert_start(lista, 1)
# lista.insert_start(lista, 5)
# lista.insert_end(lista, lista.head, 2)
# lista.insert_end(lista, lista.head, 3)
# lista.insert_end(lista, lista.head, 4)
#
# print(lista)

'''=================================================================================================='''

# class Nodo:
#     def __init__(self, dado=0, proximo_nodo=None):
#         self.dado = dado
#         self.proximo = proximo_nodo
#
#     def __repr__(self):
#         return f"{self.dado}, {self.proximo}"
#
#
# class ListaEncadeada:
#     def __init__(self):
#         self.cabeca = None
#
#     def insere_depois(self, lista, nodo_anterior, novo_dado):
#         assert nodo_anterior, "Nodo anterior precisa existir na lista"
#         novo_nodo = Nodo(novo_dado)
#         novo_nodo.proximo = nodo_anterior.proximo
#         nodo_anterior.proximo = novo_nodo
#
#     def insere_no_inicio(self, lista, value):
#         value = Nodo(value)
#         value.proximo = lista.cabeca
#         lista.cabeca = value
#
#     def __repr__(self):
#         return f"[{self.cabeca}]"
#
#
#
#
# lista = ListaEncadeada()
# print("Lista vazia", lista)
#
# lista.insere_no_inicio(lista, 1)
# lista.insere_no_inicio(lista, 2)
# lista.insere_no_inicio(lista, 3)
#
# nodo_anterior = lista.cabeca
# lista.insere_depois(lista, nodo_anterior, 1)
# lista.insere_depois(lista, nodo_anterior, 2)
# lista.insere_depois(lista, nodo_anterior, 3)
#
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
# class PileList:
#     def __init__(self):
#         self.head = None
#
#     def insert(self, list, value):
#         value = Nodo(value)
#         value.next = list.head
#         list.head = value
#     def search(self, list, value):
#         chain = list.head
#         while chain and chain.value != value:
#             chain = chain.next
#         return chain
#
#     def remove(self, value):
#         assert self.head, "ipossivel remover um valor de uma lista vazia"
#         if self.head.value == value:
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
#     def append(self, value):
#         value = Nodo(value)
#         value.next = self.head
#         self.head = value
#
#     def pop(self):
#         assert self.head, "impossivel remover um valor de uma lista"
#         self.head = self.head.next
#
#     def __repr__(self):
#         return f"[{self.head}]"

# pilhaLista = LinkedList()
# pile = Pile()
# print("Pilha vazia", pilhaLista)
#
# pilhaLista.insert_start(pilhaLista, 1)
# pilhaLista.insert_start(pilhaLista, 2)
# pilhaLista.insert_start(pilhaLista, 3)
# pilhaLista.insert_start(pilhaLista, 4)
# pilhaLista.insert_start(pilhaLista, 5)
#
# print(pilhaLista)
#
# previous = pilhaLista.head
# pile.pop()
# pile.pop()
#
# print(pilhaLista)

'''=================================================================================================='''

# class Nodo:
#     def __init__(self, value=0, next=None):
#         self.value = value
#         self.next = next
#
#     def __repr__(self):
#         return f"{self.value}, {self.next}"
#
# class PileList:
#     def __init__(self):
#         self.head = None
#
#     def insere(self, list, value):
#         value = Nodo(value)
#         value.next = list.head
#         list.head = value
#
#     def append(self, value):
#         value = Nodo(value)
#         value.next = self.head
#         self.head = value
#
#     def pop(self):
#         assert self.head, "Impossivel remover um valor de uma lista vazia"
#         self.head = self.head.next
#
#     def search(self, list, value):
#         chain = list.head
#         while chain and chain.value != value:
#             chain = chain.next
#         return chain
#
#     def remove(self, value):
#         assert self.head, "Impossivel remover um valor de uma lista vazia"
#         if self.head.value == value:
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
#     def __repr__(self):
#         return f"[{self.head}]"
#
#

'''=================================================================================================='''


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
#
#     def append(self, list, value):
#         value = Nodo(value)
#         value.next = list.head
#         list.head = value
#
#     def search(self, list, value):
#         chain = list.head
#         while chain and chain.value != value:
#             chain = chain.next
#         return chain
#
#     def pop(self):
#         assert self.head, "impossivel remover um valor de uma lista vazia"
#         self.head = self.head.next

#     def remove(self, value):
#         assert self.head, "impossivel remover um valor de uma lista vazia"
#         if self.head.value == value:
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
#     def __repr__(self):
#         return f"[{self.head}]"


# lista = LinkedList()
#
# lista.append(lista, 1)
# lista.append(lista, 2)
# lista.append(lista, 3)
# lista.append(lista, 4)
# lista.append(lista, 5)
#
# while lista.head:
#     lista.pop()
#     print(lista)
#
# print(lista)



'''lista = LinkedList()
for i in range(11, -2, -1):
    elemento = lista.search(lista, i)
    if elemento:
        print(f"O valor {i} possui na lista")
    else:
        print(f"O valor {i} não possui na lista")

lista.append(lista, "Priquito")

lista.remove(4)
lista.remove(2)
lista.remove(6)

print(lista)'''