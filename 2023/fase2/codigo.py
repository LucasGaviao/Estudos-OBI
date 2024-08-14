# https://noic.com.br/materiais-informatica/comentario/obi-2023/fase2-p2/
# Resolução pessoal. Não oficialmente avaliada.

tamanho = int(input())
origem = input()
novo = []

i = 0
while i < tamanho:
    cont = 1
    anterior = origem[i]
    i += 1
    while i < tamanho and origem[i] == anterior:
        cont += 1
        i += 1
    novo.append(cont)
    novo.append(anterior)

for j in range(len(novo)):
    if j != len(novo)-1:
        print(novo[j], end=" ")
    else:
        print(novo[j])
