# Pré - requisitos
Para esse código funcionar, é necessário estar com o python na sua versão mais recente, nesse código estamos rodando ele na versão do python 2, porém ele funciona sem problemas nenhum, e também é necessário a biblioteca Tornado, que fica resposnsável pelas requisições HTTP

### Instalando o Tornado
```
pip install tornado
```

## Executando o chat

### Executando o serverchat
Para iniciarmos, é necessário iniciarmos nosso server, que será responsável por abrigar qualquer usuário que se conecte ao nosso localhost

```
python run serverchat.py
```
O serverchat, fica responsável por criar nosso servidor, através do miniframework Tornado, atravéz de funções, ele estabiliza e cuida das requisições POST e GET das requisições HTTP, que serão requisitadas pelo chat.html, por se tratar de um websocket, ele pode abrigar inúmeras requisições de diferentes usuários ao mesmo tempo, retornando as mensagens pelo GET, e imprimindo na tela do chat para todos visualizarem.

### Executando o chathtml
Depois de subirmos o servidor, e o tornado estabelecer as requisições HTTP, basta iniciarmos nosso chat com o username e a mensagem que queremos enviar

```
run chat.html
```
Para facilitar a utilização do código, recomendo utilizar a extensão Live Server do próprio Vscode, é de extrema importancia que o servidor tenha sido rodado, é legal notarmos, que o chat em si ele não está configurado no html, mas sim no serverchat, o front só fica responsável por "logarmos" no chat, com um usuário e a mensagem que ele deseja enviar


# Repositório original
Caso queira ter acesso ao repositório original da atividade, basta acessar aqui [Diogo Branquinho](https://github.com/diogobranquinho/criptografia)