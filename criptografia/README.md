# Criptografia em Python
Utilizando a bibliotéca do RSA para demonstrar um exemplo de criptografia assimétrica, com gerações de chaves públicas e privadas.

# Pré - requisitos
Para esse código funcionar, é necessário estar com o python na sua versão mais recente, que é o python 3 e também da biblioteca RSA.

### Instalando o rsa
```
pip install rsa
```

## Executando a criptografia

### Executando o geraChaves
Para iniciarmos, é necessário gerarmos nossa chave pública e privada, atráves do geraChaves.py

```
python run geraChaves.py
```
Onde primeiro, será perguntado qual o tamanho da chave que você deseja criar, elas variam de 1 a 1024, mas o mais indicado é utilizar do tamanho 512.

Depois ele irá pedir o endereço do arquivo onde será salvo as chaves, por padrão ele sempre salva na raiz da pasta.

E por fim ele irá pedir o nome do arquivo e gerar as suas duas chaves.

### Executando o cifrarMsg
Depois de termos gerados nossas chaves, iremos criar e criptografar nossa mensagem, e faremos isso atráves do cifrarMsg.py

```
python run cifrarMsg.py
```

Onde primeiro, ele irá perguntar o endereço da chave publica, bastando apenas inserir o nome da sua chave publica, exemplo: "testePub.txt"

Depois ele irá perguntar o conteúdo da mensagem, bastando você digitar o que quer que a mensagem contenha.

E por fim, informe um nome para o arquivo da mensagem, exemplo "Teste"

### Executando o decifrarMsg
Agora que já criamos nossas chaves, e ja escrevemos e criptografamos nossa mensagem, basta apenas descriptografa-la para ver o que seu contéudo guarda.

```
python run decifrarMsg.py
```
Primeiro ele irá perguntar o endereço da sua chave privada, pois quando foi feita a criptografia dela, ela é sempre gerada com a sua chave privada.

E depois o nome que você escolheu para sua mensagem, no caso acima utilizamos o nome "Teste", então basta informarmos "Teste" que ele irá revelar o contéudo da mensagem no terminal.

# Repositório original
Caso queira ter acesso ao repositório original da atividade, basta acessar aqui [Diogo Branquinho](https://github.com/diogobranquinho/criptografia)