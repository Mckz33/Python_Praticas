def Multip_Rec(n1, n2):
    if n1 == 0:
        return 0
    if n2 == 0:
        return 0
    return Multip_Rec(n1-1, n2) + n2

print(Multip_Rec(3, 3))