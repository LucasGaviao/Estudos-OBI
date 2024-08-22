# correto 100%
pos = [int(i) for i in input().split()]

def check(lista, t):
    if t == 2:
        return "oitavas"
    esq = lista[0:t // 2]
    dir = lista[t // 2:]
    if (1 in esq and 9 in dir) or (1 in dir and 9 in esq):
        if t == 16:
            return "final"
        elif t == 8:
            return "semifinal"
        elif t == 4:
            return "quartas"
    if 1 in esq:
        return check(esq, t // 2)
    else:
        return check(dir, t // 2)

print(check(pos, 16))

