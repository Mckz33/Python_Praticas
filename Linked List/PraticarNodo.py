#================================= NODO E LISTA VAZIA ==========================================================

class Nodo:
    def __init__(self, value=0, nextValue=None):
        self.value = value
        self.next = nextValue

    def __repr__(self):
        return f"{self.value}, {self.next}"


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return "[" + str(self.head) + "]"


#=================================== INSERIR ELEMENTO ========================================================

def append(lista, newValue):
    newValue = Nodo(newValue) # cria um novo nodo, Nodo tem 2 posiçoes.
    newValue.next = lista.head # avança para a posiçao 2 cujo valor é None e passa a ter valor
    lista.head = newValue # cria uma cabeça, para dar continuidade ao proximo valor, ao excluir esse comando so terá um unico valor

#===================================== BUSCAR ELEMENTO ======================================================

def busca(lista, value):
    corrente = lista.head # criou uma variavel que recebeu o head
    while corrente and corrente.value != value: # enquanto corrente(head) e o corrente.valor(valor) for diferente do que busco
        corrente = corrente.next # passo para o proximo
    return corrente # ao achar retorna corrente

lista = LinkedList()
for i in range(8):
    append(lista, i)
print("Lista:", lista)

for i in range(8, -4, -2):
    elemento = busca(lista, i)
    if elemento:
        print(f"Elemento {i} presente na lista!")
    else:
        print(f"Elemento {i} não encontrado.")


print(lista)


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
#     def append(self, list, value):
#         value = Nodo(value)
#         value.next = list.head
#         list.head = value
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
# pilhaLista = PileList()
# print("Pilha vazia", pilhaLista)
#
# pilhaLista.append(pilhaLista, 1)
# pilhaLista.append(pilhaLista, 2)
# pilhaLista.append(pilhaLista, 3)
# pilhaLista.append(pilhaLista, 4)
# pilhaLista.append(pilhaLista, 5)
# pilhaLista.append(pilhaLista, 6)
# pilhaLista.remove(4)
# pilhaLista.remove(2)
# pilhaLista.remove(1)
# print(pilhaLista)
#
#
# print("=================")
# while pilhaLista.head:
#     pilhaLista.pop()
#     print(pilhaLista)
#

