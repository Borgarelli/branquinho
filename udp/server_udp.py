import socket
#Endereco IP do Servidor
HOST = '' # Aqui o servidor vai receber de forma automatica o endereço IP padrão do computador
# Porta que o Servidor vai escutar
PORT = 5002
udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)# Recebe os argumentos responsáveis por gerar o endereço para ser iniciado o servidor 
orig = (HOST, PORT) # Cria uma tupla chamada orig que contém o endereço IP do servidor e o número da porta que o servidor vai escutar
udp.bind(orig) # Realiza o bind do endereço gerado pelo udp
while True:
    msg, cliente = udp.recvfrom(1024) #Aqui define o tamanho maximo da mensagem que o usuário pode enviar por vez
    print(cliente, msg) #E aqui retorna a mensagem enviada pelo usuário
udp.close()