import random

class Jogador:
    def __init__(self,nome,vez,res):
        self.nome = nome
        self.vez = vez
        self.res = res
        self.list = []
        
    def addList(self,l):
        self.list.append(l)
        self.res = self.res + l
        
    
l = Jogador("LUISA",0,0)
a = Jogador("ANTONIO",1,0)

qtd = int(input('numero de vezes: '))
count = 1
player = 0
while count <= qtd:
    
    val = (random.randint(1,6))+1
    
    if player == 0:
        l.addList(val)
    else:
        a.addList(val)
    
    
    if val != 6:
        if player == 0:
            player = 1
        else:
            player = 0
    
    print(val)
    count = count + 1
    
if l.res > a.res:
    print(l.nome,l.list)
elif l.res < a.res:
    print(a.nome,a.list)
else:
    print('EMPATE',a.res + l.res)
    