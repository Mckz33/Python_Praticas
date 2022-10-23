def inverte(n):
    n = str(n)
    if n == '':
        return n
    return inverte(n[1:]) + n[0]
print(inverte(123))