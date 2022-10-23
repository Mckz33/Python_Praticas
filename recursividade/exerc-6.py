def exponencial(k, n):
    if n == 0:
        return 1
    else:
        return exponencial(k, n-1) * k
print(exponencial(2, 10))