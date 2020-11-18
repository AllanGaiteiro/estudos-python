#### Palindro ####
palindro = int(input('digite o tamanho do palindro: '))
dna = input('Digite o DNA:')
listFrent = []

for let in dna:
    listFrent.append(let)
resposta = 'N'
res = ''
count = 0
res = 'N'
while count <= len(listFrent)-1:
    
    init = -2
    fim = 0
    while (fim - init) >= 1 :
        
        if fim > len(listFrent)-1:
            init = fim = 0
        elif fim == 0:
            
            init = count
            fim = count + palindro - 1 
        elif listFrent[init] == listFrent[fim]:
            res = 'S'
            
            init = init + 1
            fim = fim - 1
        else:
            init = fim = 0
            res = 'N'     
    count = count + 1
    if res == "S":
        resposta = 'S'
        
        
print(resposta)           

    