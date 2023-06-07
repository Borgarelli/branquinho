# Pré - requisitos
Para esse código funcionar, é necessário estar com o python na sua versão mais recente, nesse código estamos rodando ele na versão do python 2, porém ele funciona sem problema nenhum, e também é necessário a instalação do miniframework Tornado, que fica responsável pelas requisições HTTP, é interessante utilizar a extensão Live Server do próprio Vscode para facilitar a visualização e execução do repete.html

### Instalando o Tornado
```
pip install tornado
```

## Executando o chat

### Executando o serverrepete
Para iniciarmos, é necessário iniciarmos nosso server, que será responsável por abrigar nosso usuário e receber nossas mensagens

```
python run serverrepete.py
```
O serverrepete, fica responsável por criar nosso servidor local, através do miniframework Tornado, através de funções, ele estabiliza e cuida das requisições POST e GET das requisições HTTP, que serão requisitadas pelo repete.html, diferente do serverchat, o serverrepete se trata de um server local, que ficará responsável por estabelecer as requisções HTTP que o repete.html irá utilizar, e com isso repetir toda mensagem que o usuário enviar, retornando as mensagens pelo GET, e repetindo tudo que o usuário enviar com um POST.

### Executando o repetehtml
Depois de subirmos o servidor, e o tornado estabelecer as requisições HTTP, basta iniciarmos nosso repetidor com o username e a mensagem que queremos enviar

```
run repete.html
```
o repete.html, fica responsável por ser o usuário que irá fazer nosso chat funcionar, ele recebe a mesma porta estabelecida pelo serverrepete, e exibe a aplicação lá, por isso é importantissimo sempre rodar os servidores antes 


# Repositório original
Caso queira ter acesso ao repositório original da atividade, basta acessar aqui [Diogo Branquinho](https://github.com/diogobranquinho/websocket)