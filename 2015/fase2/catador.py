# Resolção pessoal. Ainda não testada.
n, m = (int(i) for i in input().split())
baldes = [int(c) for c in input().split()]
indices = [int(i) for i in input().split()]

for i in indices:
    refC = baldes[i-1]
    for j in range(n):
        if abs(j+1-i) <= refC:
            if baldes[j] > 0:
                baldes[j] -= 1

print(sum(baldes))
