#python3 version
import rsa
print ('\\-------------------------------//')
print (' **Prj Banco de Dados Distribuidos**')
print (' \\-------------------------------//')
print ('Gerador de chaves assimetricas')
print ('Digite as seguintes informacoes')
size = input('Tamanho da chave: ')
end = input('Endereco do arquivo (c:\chaves\): ')
nome = input('Nome do arquivo: ')

##gero as chaves com o tamanho informado
(pub,pri) = rsa.newkeys(int(size))

##crio o arquivo pub
arqnomepub = end + nome + 'Pub.txt'
#codifico o exponente e modulo da chave para o formate PEM
arq = open(arqnomepub,'wb')
arq.write(pub.save_pkcs1(format='PEM'))
arq.close()

##crio o arquivo pri
arqnomepri = end + nome + 'Pri.txt' 
arq = open(arqnomepri,'wb')
##codifico o exponente e modulo da chave para o formate PEM
arq.write(pri.save_pkcs1(format='PEM'))
arq.close()

print ('Chaves geradas com sucesso')
print (arqnomepub)
print (arqnomepri)






