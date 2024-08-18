N = int(input())

class Pacman:
    def __init__(self):
        self.comida = 0
        self.max = 0

    def getStatus(self, pos):
        if pos == 'o':
            self.comida += 1
        elif pos == 'A':
            self.comida = 0
    
    def setMax(self):
        if self.comida > self.max:
            self.max = self.comida


player = Pacman()

for l in range(N):
    linha = input()
    if l%2 == 0:
        for i in range(N):
            player.getStatus(linha[i])
            player.setMax()
    else:
        for i in range(N-1,-1,-1):
            player.getStatus(linha[i])
            player.setMax()

print(player.max)
