def fatorialDuplo(num):
    if num%2==0:
        num-=1
    if num <= 0:
        return 1
    else:
        return fatorialDuplo(num-2) * num

print(fatorialDuplo(5))