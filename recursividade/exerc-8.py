def mdc(x, y):
    if y == 0:
        return x
    elif x == 0:
        return y
    if max(x, y) % min(x, y) == 0:
        return min(x, y)

    for i in range(min(x, y)-1, 1, -1):
        if min(x, y) % i == 0:
            return mdc(i, max(x, y))
    return 0

print(mdc(12, 8))