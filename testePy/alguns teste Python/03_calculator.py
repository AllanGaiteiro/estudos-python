
##### calculado ######

### funcoes
def soma(a,b):
    return (a + b)

def sub(a,b):
    return (a - b)

def div(a,b):
    return (a / b)

def mult(a,b):
    return (a * b)
###############

print('sair[0] | soma[1] |  subtraçao[2] | divisao[3] | multiplicaçao[4]')
### variavel qu armazena os erros
erro = []
### estatus da aplicacao
status = True
### resposta
res = 0
while (status)  :
    
    menu = int(input('digite uma das opçoes acima: '))
    ## se menu é 0 nao presisa digitar mais nada
    if menu != 0:
        
        a = int(input('\ndigite um numero: '))
        b = int(input('\ndigite um numero: '))
        ops = ''
    
    ## se é 0 sai do sistema
    if menu == 0:
        status = False
    ### diferença bem grande no else if comun
    elif menu == 1 :
        ops = 'soma'
        print('\nexecultando a',ops)
        res = soma(a,b)
    
    elif  menu == 2:
        ops = 'subtracao'
        print('\nexecultando a',ops)
        res =  sub(a,b)
        
    elif  menu == 3:
        
        ops = 'divisao'
        print('\nexecultando a',ops)
        res =   div(a,b)
        
        
    elif  menu == 4:
        ops = 'multiplicaçao'    
        print('\nexecultando a',ops)
        res =  mult(a,b)
        
        
    else:
        erro.append('opçao do menu invalida')
    
    if (len(erro) == 0) & (menu != 0):
        print('\nVocê digitou [',a,'] e [',b,'] a ', ops,' é igual a ', res )
        
    elif len(erro) != 0:
        print('Erro: ', erro)
        
print('\nTenha um bom dia')

