import random

d = {}

for i in range(100):
    num = int(random.random() * 20)

    if d.get(num) != None:
        for chave in d:
            if chave == num:
                d[chave] += 1
    else:
        d[num] = 1

print(d)