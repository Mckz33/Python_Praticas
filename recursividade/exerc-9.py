def somatorio(n):
    if n == 1:
        return 1
    return somatorio(n-1) + n

print(somatorio(3))