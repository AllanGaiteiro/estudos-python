

vagPat = input('Vagas e Partidos: ')

vagPat = vagPat.split(' ')


class Partidos:
    def __init__(self,nome,valores):
        self.nome = nome
        self.valores = valores
        self.vagas = 0
    
    def addVagas(self,vaga):
        self.vagas = vaga
        


valores = []
partidos = []
for i in range(int(vagPat[1])):
    val = int(input('Votos de Partidos: '))
    name = 'Partido '+ str(i)
    p = Partidos(name,val)
    partidos.append(p)
    valores.append(val)

total = 0
for i in range(len(valores)):
    total = total + valores[i]
    
for p in partidos:
    ###vaga = ((p.valores / total)* int(vagPat[0]))
    vaga = round((p.valores / total)* int(vagPat[0]))
    p.addVagas(vaga)
    
    print(p.nome, p.vagas)    
