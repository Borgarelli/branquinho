#!/usr/bin/python2
import tornado.web  
import tornado.websocket  
import tornado.ioloop  

from tornado.options import define, options, parse_command_line  

define("port", default=8887, help="run on the given port", type=int)  # Define uma opção de linha de comando 'port' com valor padrão 8887

chatTexto = "<h2>Chat Server Prj BDD</h2>"  # Define uma variável para armazenar o conteúdo do chat (HTML)
connections = set()  # Define um conjunto para armazenar as conexões WebSocket ativas

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("chat.html")  # Renderiza o arquivo HTML "chat.html" quando um GET é feito na raiz do servidor

class WebSocketHandler(tornado.websocket.WebSocketHandler):  
    def open(self):
        global connections
        connections.add(self)  # Adiciona a conexão WebSocket ao conjunto de conexões ativas
        self.write_message(chatTexto)  # Envia a mensagem inicial para o cliente WebSocket

    def on_message(self, message):
        global chatTexto
        global connections

        objTexto = message.strip().split(',')
        userName = objTexto[0]  
        mensagem = objTexto[1]  
        hora = objTexto[2]  

        # Atualiza o conteúdo do chat com as informações da nova mensagem
        chatTexto += "<div class='msgBody'>"
        chatTexto += "<p class='username'>"
        chatTexto += userName
        chatTexto += " diz: </p>"
        chatTexto += "<p class='message'>"
        chatTexto += mensagem
        chatTexto += "<span class='time'>"
        chatTexto += hora
        chatTexto += "</span>"
        chatTexto += "</p>"
        chatTexto += "</div>"
        print(chatTexto)  
        for con in connections:
            con.write_message(chatTexto)  # Envia a mensagem atualizada para todos os clientes conectados

    def on_close(self):
        global connections
        connections.remove(self)  # Remove a conexão WebSocket do conjunto de conexões ativas

app = tornado.web.Application([  # Cria uma instância da aplicação Tornado
    (r"/", IndexHandler),  # Mapeia a raiz do servidor para a classe IndexHandler
    (r"/websocket", WebSocketHandler),  # Mapeia o caminho "/websocket" para a classe WebSocketHandler
])

if __name__ == '__main__':
    parse_command_line()  
    app.listen(options.port)  # Inicia o servidor na porta especificada nas opções de linha de comando
    tornado.ioloop.IOLoop.instance().start()  # Entra no loop de eventos do Tornado para atender as requisições
