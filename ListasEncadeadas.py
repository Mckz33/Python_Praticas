class NodoLista:
    """ 1- Esta representa um nodo de uma lista encadeada."""
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.next = proximo_nodo

    def __repr__(self):
        return f"{self.dado} -> {self.proximo}"

class ListaEncadeada:
    """ 2- Esta classe representa uma lista encadeada."""
    def __init__(self):
        self.cabeca = None

    def __repr__(self):
        return "[" + str(self.cabeca) + "]"

"""====================== INSERÇÃO ======================"""

def append(lista, novo_dado):
    """ 1- cria um novo nodo com o dado a ser armazenado."""
    novo_nodo = NodoLista(novo_dado)
    """ 2- Faz com que o novo nodo seja a cabeça da lista."""
    novo_nodo.proximo = lista.cabeca
    """ 3- Faz com que a cabeça da lista referencie o novo nodo."""
    lista.cabeca = novo_nodo

"""====================== BUSCAR ======================"""

def busca(lista, valor):
    corrente = lista.cabeca
    while corrente and corrente.dado != valor:
        corrente = corrente.proximo
    return corrente


lista = ListaEncadeada()
for i in range(8):
    append(lista, i)
print("Lista", lista)
for i in range(8, -4, -2):
    elemento = busca(lista, i)
    if elemento:
        print(f"Elemento {i} presente na lista!")
    else:
        print(f"Elemento {i} não encontrado!")


"""print("Lista vazia:", lista)

insere_no_inicio(lista, 5)
print("Lista contém um único elemento:", lista)

insere_no_inicio(lista, "Manjuba")
print("Insere um novo elemento:", lista)
insere_no_inicio(lista, "Tinindo")
print("Insere um novo elemento:", lista)
insere_no_inicio(lista, "Pafoca")
print("Insere um novo elemento:", lista)
insere_no_inicio(lista, "Priquito")
print("Insere um novo elemento:", lista)"""