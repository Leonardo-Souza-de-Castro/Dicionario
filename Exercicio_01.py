def procuraChave(dicionario, valor):
    lista_chaves = []
    for chave in dicionario:
        if dicionario.get(chave) == valor:
            lista_chaves.append(chave)

    print(lista_chaves)


d = {
    'teste' : 0,
    'teste1' : 2,
    'teste2' : 10,
}

procuraChave(d, 1)