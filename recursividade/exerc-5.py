def somatorio(numero):
    if numero == 0:
        return 0
    else:
        return somatorio(numero-1) + numero

print(somatorio(4))