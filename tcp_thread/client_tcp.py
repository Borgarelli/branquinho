#Cliente TCP
import socket
# Endereco IP do Servidor
SERVER = '127.0.0.1'
# Porta que o Servidor esta escutando
PORT = 5002
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
dest = (SERVER, PORT)
tcp.connect(dest) # Aqui ele realiza a conexão com o servidor
print ('Para sair use CTRL+X\n')
msg = input()
while msg != '\x18': # Aqui ele irá entrar em um loop infinito enquanto a entrada do usuário não for CTRL+X
    tcp.send (msg.encode()) # Envia a mensagem codificada em bytes para o servidor
    msg = input() 
tcp.close() 
