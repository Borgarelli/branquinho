#!/usr/bin/python2
import tornado.web  # Importa a classe para criar handlers de requisição HTTP
import tornado.websocket  # Importa a classe para criar handlers de WebSockets
import tornado.ioloop  # Importa o loop de eventos do Tornado

from tornado.options import define, options, parse_command_line  # Importa as opções de linha de comando do Tornado

define("port", default=8888, help="run on the given port", type=int)  # Define uma opção de linha de comando 'port' com valor padrão 8888

class IndexHandler(tornado.web.RequestHandler):  # Classe que lida com requisições HTTP
    def get(self):
        self.render("repete.html")  # Renderiza o arquivo HTML "repete.html" quando um GET é feito na raiz do servidor

class WebSocketHandler(tornado.websocket.WebSocketHandler):  # Classe que lida com conexões WebSocket
    def on_message(self, message):
        self.write_message(u"Servidor repete: " + message)  # Retorna a mensagem recebida, prefixada com "Servidor repete:"

app = tornado.web.Application([  # Cria uma instância da aplicação Tornado
    (r"/", IndexHandler),  # Mapeia a raiz do servidor para a classe IndexHandler
    (r"/websocket", WebSocketHandler),  # Mapeia o caminho "/websocket" para a classe WebSocketHandler
])

if __name__ == '__main__':
    parse_command_line()  # Parseia as opções de linha de comando
    app.listen(options.port)  # Inicia o servidor na porta especificada nas opções de linha de comando
    tornado.ioloop.IOLoop.instance().start()  # Entra no loop de eventos do Tornado para atender as requisições
