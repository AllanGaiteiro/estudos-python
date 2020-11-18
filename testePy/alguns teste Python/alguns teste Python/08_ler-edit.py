
### arquivo lido 
arquivo = open(input('Nome do arquivo a ser: '), 'r')
texto = arquivo.readlines()

### aruivo editado
texto.append(input('Insira texto:'))
arquivo = open(input('Nome darquivo a ser editado:'), 'w')
arquivo.writelines(texto)
arquivo.close()
