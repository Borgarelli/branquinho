#python3 version
import rsa
print('\\-------------------------------//')
print('**Prj Banco de Dados Distribuidos**')
print('\\-------------------------------//')
print('Cifrador de mensagens')
print('Digite as seguintes informacoes')
arqnomepub = input('Endereco da chave publica (c:\chaves\myPub.txt): ')
msg = input('Mensagem a ser cifrada: ').encode('utf-8')
arqnomemsg = input('Endereco e nome da mensagem (c:\msg.txt): ')

##abro o arquivo com a chave
arq = open(arqnomepub,'rb')
##carrego a chave
txt = arq.read()
arq.close()

#decodifico para o formato expoente e modulo
pub = rsa.PublicKey.load_pkcs1(txt, format='PEM')

#cifro a msg
msgc = rsa.encrypt(msg,pub)

#salvo a msgc no arquvio
arq = open(arqnomemsg,'wb')
arq.write(msgc)
arq.close()

print('Mensagem cifrada no arquivo ' + arqnomemsg)



