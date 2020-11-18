
class Pessoa:
    def __init__(self):
        self.nome = ''
        self.idade = 0
        self.altura = 0
        self.cpf = ''
        self.reseva = 0
        
    def updateReserva(self,money):
        self.reseva = self.reseva + money
        
    __updateReserva = updateReserva 


class Pai(Pessoa):
    
    def __init__(self):
        self.dependente = []
        
    def addDependentes(self,dp):
        ### adcionar na lista
        self.dependente.append(dp)
    def removDependentes(self,dp):
        ### remov da lista
        self.dependente.remove(dp)
        ###'alex',27,1.7,'444.444.44',1200

#### criei o Pai na subclasse de pessoa (pai)       
alex = Pai()

### usei atributos de pessoa
alex.nome = 'alex'
alex.idade = 27
alex.altura = 1.7
alex.cpf = '444.444.44'
alex.reseva = 1200
### alterei meu foundos
alex.updateReserva(2000)
#### classe pessoa
bela = Pessoa()
bela.nome = 'bela'
bela.idade = 13
bela.altura = 1.3
bela.cpf = '444.432.44'
bela.reseva = 0

### tornei bela dependent de alex
alex.addDependentes(bela)


#### remover um dependente
##alex.removDependentes(bela)

# chamei a bela

print(alex.dependente[0].nome)

print(alex.reseva)



###############################
# alex é uma pai q tem por dependente uma pessoa a bela ###############################