class Aluno:
    def __init__(self, nota1=0, nota2=0, nota3=0, nota4=0):
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4

    def getNota1(self):
        return self.nota1
    def getNota2(self):
        return self.nota2
    def getNota3(self):
        return self.nota3
    def getNota4(self):
        return self.nota4

    def totalNotas(self):
        return self.nota1 + self.nota2 + self.nota3 + self.nota4

    def mediaNotas(self):
        return (self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4

qtdAlunos = int(input("Quantos Alunos: "))
listaAlunos = []
for i in range(0, qtdAlunos):
    print("Digita a nota do aluno ", i+1)
    nota1 = int(input("Nota 1: "))
    nota2 = int(input("Nota 2: "))
    nota3 = int(input("Nota 3: "))
    nota4 = int(input("Nota 4: "))
    aluno = Aluno(nota1, nota2, nota3, nota4)
    print("Média do aluno: ", aluno.mediaNotas())
    listaAlunos.append(aluno)


