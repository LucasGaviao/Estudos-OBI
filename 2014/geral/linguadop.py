codigo = input()

palavras = codigo.split()

mensagem = []
for palavra in palavras:
    for i in range(len(palavra)):
        if i%2 != 0:
            mensagem.append(palavra[i])
    if palavras.index(palavra) != len(palavras) - 1:
        mensagem.append(' ')

saida = ''
for l in mensagem:
    saida += l

print(saida)
