# https://olimpiada.ic.unicamp.br/pratique/ps/2015/f2/usina/
# Resolução pessoal. Não oficialmente avaliada.

'''informações importantes:
    tem um engenheiro descendo os escorregadores na velocidade de 1m/s
    se uma pessoa ouve um grito ela automaticamente propaga a informação "tomando" o lugar de quem le avisou'''

def deltaT(esc, scp, t):
    if esc.chegada in scp:
        if esc.comprimento <= t:
            return 0
        return esc.comprimento - t
    return esc.comprimento

def defineMelhor(esc, fim):
    if esc.chegada == fim:
        return esc.tempoDeChegar
    return None

    
def busca(inicio):
    if mapa[inicio] == [] and inicio != n:
        return -1  
    
    '''print("=="*10)
    print(f"INICIO: {inicio}")
    for j in mapa:
        for o in mapa[j]:
            print(o)
    print("=="*10)'''
    
    for item in mapa[inicio]:
        temp = -1
        if item.melhor == None:
            if temp >= 0:
                item.melhor = busca(item.chegada)
                temp = min(temp, item.melhor)
                #return temp
            else:
                temp = busca(item.chegada)
                item.melhor = temp
                #return temp
        else:
            if temp >= 0:
                temp = min(temp, item.melhor)
                #return temp
            else:
                temp = item.melhor
                #return temp
        return temp

class Escorrega:
    
    def __init__(self, primeiro, segundo, distancia):
        self.partida = int(primeiro)
        self.chegada = int(segundo)
        self.comprimento = int(distancia)
        self.tempoDeChegar = deltaT(self, salasComP, k)
        self.melhor = defineMelhor(self, n)
    
        
    def __str__(self):
        #return 'Partida ' + str(self.partida) + ', Chegada ' + str(self.chegada) + ', Comprimento ' + str(self.comprimento) + ', deltaT ' + str(self.tempoDeChegar)
        return f'Partida {self.partida}, Chegada {self.chegada}, Comprimento {self.comprimento}, deltaT {self.tempoDeChegar}, melhor {self.melhor}'
n, m, c, k = (int(i) for i in input().split()) # n°salas, n°escorrecadores,n° de sala com pessoas, distancia possivele de ouvir em metros
salasComP = [int(i) for i in input().split()]

mapa = {}
#tuneis = []

for i in range(n):
    mapa[i+1] = []

for _ in range(m):
    a = input().split()
    escorrega = Escorrega(a[0], a[1], a[2])
 #   tuneis.append(escorrega)
    mapa[escorrega.partida].append(escorrega)
    
print(busca(1))


'''print("=="*10)
print(f"DEPOIS:")
for j in mapa:
    for o in mapa[j]:
        print(o)
print("=="*10)'''
