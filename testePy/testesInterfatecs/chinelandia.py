conjunto = int(input('digite a quantidade de conjuntoos:'))
pares = []
for i in range(conjunto):
    par = input('Digite os pares:')
    par = par.split(' ')
    par[0] = int(par[0])

    par[1] = int(par[1])
    pares.append(par)

repetindo = []
for i in range(len(pares)):
    left = -1
    right = -1
    for j in range(len(pares)):
        if pares[i][0] == pares[j][0]:
            left = left + 1

        if pares[i][1] == pares[j][1]:
            right = right + 1

    if (left) > 0:
        repetindo.append([pares[i][0],'E',left])
    if (right) > 0:
        repetindo.append([pares[i][1],'D', right])


def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l

repetindo = remove_repetidos(repetindo)


if len(repetindo) == 0:
    print('SEM TROCAS DESTA VEZ')

else:
    for x in repetindo:
        print(x)