summa = 0
kv = 0
while True:
    a = int(input())
    summa += a
    kv += a ** 2
    if summa == 0:
        print(kv)
