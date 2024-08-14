# https://noic.com.br/wp-content/uploads/2023/08/grupos-pt.pdf
# Resolução pessoal. Não oficialmente avaliada.

E, M, D = (int(i) for i in input().split())
bom = {}
ruim = {}
for i in range(E):
    bom[i+1] = []
    ruim[i+1] = []
     
for _ in range(M):
    a, b = (int(i) for i in input().split())
    bom[a].append(b)
for _ in range(D):
    a, b = (int(i) for i in input().split())
    ruim[a].append(b)

cont_quebras = 0
for _ in range(int(E//3)):
    grupo = [int(p) for p in input().split()]
    for pessoa in grupo:
        for par in bom[pessoa]:
            if par not in grupo:
                cont_quebras += 1
                
        for par in ruim[pessoa]:
            if par in grupo:
                cont_quebras += 1
              
print(cont_quebras)
