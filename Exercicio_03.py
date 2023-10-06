import random

def soma_dados():
    return random.randint(2,12)

d = {}

for i in range(1000):
    num = soma_dados()

    if d.get(num) != None:
        for chave in d:
            if chave == num:
                d[chave] += 1
    else:
        d[num] = 1

for chave in d:
    a = d.get(chave)

    prc = (a * 100)/1000

    d[chave] = str(prc) + '%'


print(d)

