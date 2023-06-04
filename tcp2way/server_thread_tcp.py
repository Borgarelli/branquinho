#Servidor TCP
import socket
from threading import Thread

global tcp_con
import rsa

arqnomepub = 'C:\\Users\\borga\\Downloads\\socket-master\\tcp2way\\GabrielchaveGabrielPub.txt' #A chave publica do meu amigo, que será responsável para ele gerar as mensagens criptografadas para mim poder ler
arq = open(arqnomepub,'rb')
# lê o conteúdo do arquivo
txt = arq.read()
arq.close()

# carrega a chave pública do arquivo no formato PEM
pub = rsa.PublicKey.load_pkcs1(txt, format='PEM')


arqnomepri = 'C:\\Users\\borga\\Downloads\\socket-master\\tcp2way\\chavekauaPri.txt' #Aqui incluo a minha chave privada, pois somente eu que estou rodando o server posso descriptografar a mensagem que o meu amigo enviar
arq1 = open(arqnomepri,'rb')
##carrego a chave privada
txt1 = arq1.read()
arq1.close()

#decodifico para o formato expoente e modulo
pri = rsa.PrivateKey.load_pkcs1(txt1, format='PEM')

def enviar():
    global tcp_con
    msg = input()        
    while True:
        msgc = rsa.encrypt(msg.encode(), pub)
        tcp_con.send(msgc)
        msg = input()

# Endereco IP do Servidor
HOST = '10.10.11.3' #Aqui eu utilzo o meu endereço ipv4 que será resposnsável por manter a conexão

# Porta que o Servidor vai escutar
PORT = 5002

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

while True:
    tcp_con, cliente = tcp.accept()
    print ('Concetado por ', cliente)
    t_env = Thread(target=enviar, args=())
    t_env.start()
    while True:
        msg = tcp_con.recv(1024)
        if not msg: break
        msgd = rsa.decrypt(msg, pri)
        print("Gabriel:",msgd)
    print ('Finalizando conexao do Gabriel', cliente)
    tcp_con.close()