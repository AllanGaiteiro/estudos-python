
### nao presisa falar o tipo
pyto = "python"
lista = []
### formato do for é diferente
for x in pyto:
    ### nao tem push
    lista.append(x)

print(lista)
count = 0
pyto2 = ''

### cuidado com o len ele da quantidade nao posiçao 
while count < len(lista):
    ###print(lista[count])
    pyto2 = pyto2  + lista[count]
    count = count +1
    
print(pyto2)

