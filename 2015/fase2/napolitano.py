dic = {"I":1,
       "V":5,
       "X":10,
       "L":50,
       "C":100,
       "D":500,
       "M":1000}
nap = input()
numero = [dic[i] for i in nap.strip()]

for i in range(len(nap)):
    for n in dic:
        if dic[n]>dic[nap[i]] and n in nap[i:]:
            numero[nap.index(n)] -= numero[i]
            numero[i] = 0

print(sum(numero))