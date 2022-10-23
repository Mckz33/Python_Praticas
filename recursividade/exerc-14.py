def contador(n):
    if n == 0:
        return [0, ]

    return contador(n - 2) + [n, ]


print(contador(6))