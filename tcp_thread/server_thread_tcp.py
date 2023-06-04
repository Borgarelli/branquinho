#Servidor TCP
import socket
from threading import Thread

# Função que irá lidar com cada conexão recebida
def conexao(con,cli):
    while True:
        msg = con.recv(1024) # Recebe dados da conexão
        if not msg: break # Sai do loop se não receber nada
        print (msg)
    print ('Finalizando conexao do cliente', cli)
    con.close()  

# Endereco IP do Servidor
HOST = '' 
PORT = 5002 
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1) # Aqui define o número máximo de conexões simultâneas que o servidor irá aceitar


while True:
    con, cliente = tcp.accept() # Aqui ele aceita uma nova conexão
    print ('Concetado por ', cliente)
    t = Thread(target=conexao, args=(con,cliente,)) # Cria uma nova thread para lidar com a conexão
    t.start() # Inicia a nova thread criada
