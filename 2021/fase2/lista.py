tam = int(input())
lista = [int(i) for i in input().split()]

acoes = 0
for i in range(tam):
    if tam-i-1 >= 0 and lista[i] == lista[tam-i-1]:
        continue
    if i+1 < tam and (lista[i]+lista[i+1] == lista[tam-i-1] or( tam-i-2 >= 0  and lista[i]+lista[i+1] == lista[tam-i-1] + lista[tam-i-2])):
        lista[i] = lista[i]+lista[i+1]
        lista.pop(i+1)
        tam -= 1 
        
        acoes += 1
    
    if tam-i-2 >= 0 and lista[tam-i-1]+lista[tam-i-2] == lista[i]:
        lista[tam-i-2] = lista[tam-i-1]+lista[tam-i-2]
        lista.pop(tam-i-1)
        tam -= 1
        
        acoes += 1

print(f"{acoes}")
