# https://olimpiada.ic.unicamp.br/pratique/ps/2014/f2/voo/
# Resolução pessoal.
class Horario:
    def __init__(self, horario):
        if len(horario) == 2:
            self.hora = int(horario[0])
            self.min = int(horario[1])
        elif len(horario) == 1:
            self.hora = int(horario[0])//60
            self.min = int(horario[0])%60

    def __add__(self, other):
        bonus = 0
        novomin = self.min + other.min
        if novomin > 60:
            bonus = 1
            novomin -= 60
        novahora = self.hora + other.hora + bonus
        if novahora > 24 or (novahora == 24 and novomin > 0):
            novahora -= 24
        return Horario([novahora, novomin])
    
    def __str__(self):
        return str(self.hora) + ':' + str(self.min)
    
    def __sub__(self, other):
        bonus = 0
        novomin = self.min - other.min
        if novomin < 0:
            bonus = 1        
            novomin += 60
        novahora = self.hora - other.hora - bonus
        if novahora < 0:
            novahora += 24
        return Horario([novahora, novomin])
    
    def toMin(self):
        return self.hora*60 + self.min

pa, cb, pb, ca = (Horario(i.split(":")) for i in input().split())

delta1 = cb - pa
delta2 = ca - pb

tempoDeVoo = Horario([(delta1 + delta2).toMin()//2])
ref = delta1 if min(delta1.toMin(), delta2.toMin()) == delta1.toMin() else delta2
fusorario = Horario([ref.toMin() - tempoDeVoo.toMin()])

if ref == delta2:
    fusorario.hora *= -1

print(f"{tempoDeVoo.toMin()} {fusorario.hora}")
