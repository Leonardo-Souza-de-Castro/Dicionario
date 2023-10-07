import random

d = {}

for _ in range(100): #quando não vamos utilizar a variável contadora colocamos o _ para representá-la 
    num = int(random.random() * 20)

    if d.get(num) != None:
        for chave in d:
            if chave == num:
                d[chave] += 1
    else:
        d[num] = 1

print(d)