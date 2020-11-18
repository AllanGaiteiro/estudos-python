#### classes


class funsoes(object):
    def __init__(self,num1,num2):
        ### atributo passados pelo usuario
        self.num1 = num1
        self.num2 = num2
        self.erros = []
        ### atributos tipos caculos
        self.soma = (num1 + num2)
        self.sub = num1 - num2
        self.div = num1 / num2
        self.mult = num1 * num2
        
    ### atributo que armazena os erros
    def add_erro(self,erro):
        self.erros.append(erro)

print('sair[0] | soma[1] |  subtraçao[2] | divisao[3] | multiplicaçao[4]')

### estatus da aplicacao
status = True
### resposta
res = 0
while (status)  :
    
    menu = int(input('digite uma das opçoes acima: '))
    ## se menu é 0 nao presisa digitar mais nada
    f = 0
    if menu != 0:
        f = funsoes(int(input('\ndigite um numero: ')),int(input('\ndigite um numero: ')))
        ops = ''
    
    ## se é 0 sai do sistema
    if menu == 0:
        status = False
    ### diferença bem grande no else if comun
    elif menu == 1 :
        ops = 'soma'
        res = f.soma
    
    elif  menu == 2:
        ops = 'subtracao'
        res =  f.sub
        
    elif  menu == 3:
        ops = 'divisao'
        res =   f.div
        
    elif  menu == 4:
        ops = 'multiplicaçao'    
        res =  f.mult 
        
    else:
        f.add_erro('opçao do menu invalida')
    
    if (len(f.erros) == 0) & status:
        print('\nVocê digitou [',f.num1,'] e [',f.num2,'] a ', ops,' é igual a ', res )
        
    else :
        status = False
        print('Erro: ', f.erros)
        
        
print('\nTenha um bom dia')