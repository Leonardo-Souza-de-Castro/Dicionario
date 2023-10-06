def caracterUnico():
    a = input("Digite uma palavra: ")

    b = a.lower()

    d = {}

    soma = 0

    for i in range(len(b)):
        if d.get(b[i]) != None:
            for chave in d:
                if chave == b[i]:
                    d[chave] += 1
        else:
            d[b[i]] = 1
            soma += 1

    print(f"{a} : {soma}")

    

caracterUnico()