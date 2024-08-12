# Minha resolução para o problema Dona Formiga(https://olimpiada.ic.unicamp.br/pratique/ps/2020/f2/formiga/)

def contarCaminhos(possivel, sala, registro, cont, dicionario):
    #print(f"lista[{sala}]:{listaT}, cont:{cont}")
    if possivel != []:
        for destino in possivel:
            #print(f"1-lista[{sala}]:{listaT}, cont:{cont}, reg: {reg}, destino: {destino}\n")
            registro = max(cont, registro, contarCaminhos(tuneis[destino], destino, registro, cont+1, dicionario))
            #print(f"2-lista[{sala}]:{listaT}, cont:{cont}, reg: {reg}, destino: {destino}")
    return max(registro, cont)

# lendo os inputs
s, t, p = map(int, input().split()) # salões, tuneis , partida
alturas = list(map(int, input().split())) # altura das salas 

# crinado uma lista para cada salão
tuneis = {}
for q in range(s):
    tuneis[q+1] = []
#print(tuneis)

# adicionando a lista de cada salão os possiveis para escorregar
for i in range(0, t):
    a, b = map(int, input().split()) # lendo as salas que estão ligadas
    if alturas[a-1] > alturas[b-1]:
        tuneis[a].append(b)
    elif alturas[a-1] < alturas[b-1]:
        tuneis[b].append(a)

#print(tuneis)

# se o salão de partida for o mais baixo não é necessario verificar os caminhos
if tuneis[p] == []:
    print(0)
    exit()
r1 = contarCaminhos(tuneis[p], p,0, 0, tuneis)
print(r1)
