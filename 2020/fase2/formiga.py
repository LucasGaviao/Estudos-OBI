s, t, p = map(int, input().split()) # salões, tuneis , partida
alturas = list(map(int, input().split())) # altura das salas 

# crinado uma lista para cada salão
tuneis = {}
for q in range(s):
    tuneis[q+1] = []
#print(tuneis)

# adicionando a lista de cada salão os possiveis para escorregar
for i in range(0, t):
    a, b = map(int, input().split())
    if alturas[a-1] > alturas[b-1]:
        tuneis[a].append(b)
    elif alturas[a-1] < alturas[b-1]:
        tuneis[b].append(a)
    #print(f"{alturas[a-1] > alturas[b-1]}\n{alturas[a-1] < alturas[b-1]}")

#print(tuneis)

# se o salão de partida for o mais baixo não é necessario verificar os caminhos
if tuneis[p] == []:
    print(0)
    exit()

r1 = 0

def contarCaminhos(listaT, sala, reg, cont):
    #print(f"lista[{sala}]:{listaT}, cont:{cont}")
    if listaT != []:
        for destino in listaT:
            #print(f"1-lista[{sala}]:{listaT}, cont:{cont}, reg: {reg}, destino: {destino}\n")
            reg = max(cont, reg, contarCaminhos(tuneis[destino], destino, reg, cont+1))
            #print(f"2-lista[{sala}]:{listaT}, cont:{cont}, reg: {reg}, destino: {destino}")
    return max(reg, cont)
r1 = contarCaminhos(tuneis[p], p,0, 0)
print(r1)
