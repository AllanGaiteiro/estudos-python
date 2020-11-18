### trabalhando testo tomar cuidado com o caminho


### r = leitura
### w = escrita, reescreve o arquivo
### x = escrita, verifica se o arquivo ja existe se sim retorna um erro
### a = escrita, inseri no final do arquivo
### b = modo binario
### t = modo testo(padrao)
### + = atualizar. tanto leitura tando escrita 


arquivo = open('07_arquivosTXT.txt', 'a')
arquivo.write("Olá, mundo!")
print(arquivo)