def verificaRepeticao(k, n):
    k = str(k)
    n = str(n)
    if n == '':
        return 0
    if k == n[0]:
        return verificaRepeticao(k, n[1:]) + 1
    return verificaRepeticao(k, n[1:])


print(verificaRepeticao(2, 762021192))