class Nodo:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"{self.value}, {self.next}"


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, list, value):
        value = Nodo(value)
        value.next = list.head
        list.head = value

    def search(self, list, value):
        chain = list.head
        while chain and chain.value != value:
            chain = chain.next
        return chain

    def __repr__(self):
        return f"[{self.head}]"

lista = LinkedList()
rem = []
for i in range(5):
    lista.insert(lista, i)
    rem.append(i)
    lista.insert(lista, i)
    rem.append(i)

print(lista)

lista.removeDuplicatas(lista)
print(lista)


#
# for i in range(6):
#     if lista.search(lista, i):
#         print(f"Valor {i} encontrado")
#     else:
#         print(f"Valor {i} não encontrado!")
#
# print(rem)
# myset = set(rem)
# print(myset)
