import socket
# Endereco IP do Servidor
SERVER = '127.0.0.1'
# Porta que o Servidor esta escutando
PORT = 5002
udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # Recebe os argumentos responsáveis por gerar o endereço para ser iniciado o servidor 
dest = (SERVER, PORT) # O dest realiza a mensa função que o orig em server_udp.py ele cria uma tupla chamada orig que contém o endereço IP do servidor e o número da porta que o servidor vai escutar
print ('Para sair use CTRL+X\n')
msg = input()
while msg != '\x18': # Enquanto a mensagem não for CTRL+X, envia a mensagem para o servidor
    udp.sendto (msg.encode(), dest) # Aqui ele envia a mensagem para o servidor com a função sendto() e é importante lembrar que a mensagem precisa ser convertida para bytes com a função encode()
    msg = input()
udp.close()