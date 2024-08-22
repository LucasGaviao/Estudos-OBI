# correto! 100/100
t = int(input())
baixo = [int(i) for i in input().split()]

baixo.sort()
menor = baixo[0]
possivel = "N"
if menor <= 8:
    possivel = "S"
    for i in range(t):
        if i-1 > 0 and abs(baixo[i] - baixo[i-1]) > 8:
            possivel = "N"
            break
        if i+1 < t and abs(baixo[i] - baixo[i+1]) > 8:
            possivel = "N"
            break

print(possivel)
