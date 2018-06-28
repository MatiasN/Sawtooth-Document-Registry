# Funcionamente da WebApp

- Esta aplicação corre em NodeJS, baseando-se em REST Resquests.
- Para funcionar em conjunto com a blockchain, esta terá de fazer, inicialmente, requests à blockchain (a partir de nodos escolhidos à mão inicialmente, e futuramente automatizar para o nodo mais próximo), estes requests (REST segundo documentação Sawtooth) irão servir para fazer uma cópia dos dados presentes na blockchain para a base de dados de onde é lançado este serviço, este processo serve como iniciação do serviço para poder ser utilizado pela instituição que o comprou. (O processo de copiar os dados da blockchain pode ser feito de x em x tempo para atualizar as bases de dados de todos os servidores onde correrá uma aplicação que utilize a blockchain)
- Estando a sincronização com a blockchain feita, procedesse aos processos normais da app. Consulta e inserção de documentos na blockchain.
- Consulta:
  É feito um get rest request a partir do front end para o servidor da app, que leva como parametros os campos fornecidos para a consulta, estes que sao utilizados para consultar o(s) artigo(s) na DB e devolver o(s) link(s) como resposta ao request para o front end (Em formato JSON).
- Inserção:
  É feito um post rest request a partir do front end para o servidor da app, que leva como body todos os parametros para inserção do artigo, após este request, o servidor trata de fazer um request de inserção na blockchain utilizando a API disponibilizada, e também atualizando a sua base de dados entretanto após o artigo ser inserido na blockchain, assim sabendo em que bloco foi enserido também.
 
## Componentes:
- Blockchain
- Servidor/WebApp
- Front end/Browser
- Bases de Dados do Servidor

# Apresentação:

## Topicos:

- Objetivos
- Tecnologias
- Funcionamento
- Implementação

### Objetivos
- Registar artigos cientificos numa blockchain privada, para user por parte de instituições
- Consulta e registo de artigos a partir de uma plataforma/app própria ligada à blockchain 
### Tecnologias
- WebApp: NodeJS server, MongoDB, REACT/Handlebars/Angular, REST services
- Blockchain: Sawtooth, Poet, REST services
### Funcionamento
- Por cada instuição a usufruir do serviço, terá que ter um nodo a participar na blockchain e uma plataforma com a WebApp integrada.
- Quando é feito o setup da WebApp, esta tem que se conectar à blockchain(usando o nodo mais proximo ou manualmente) para copiar toda a informação presente na blockchain para a DB, assim podendo os artigos ser consultados de maneira mais dinamica e versátil.
- Inserção de artigos (no idea)
- Ao fim de x tempo a WebApp faz uma atualização à DB fazendo pedidos dos blocos novos.
### Implementação
DIAGRAMAS

# Vantagem Principal
- No contexto de uma blockchain privada entre instituições, este projeto vai garantir uma integração e setup fácil de uma nova instituição que use a WebApp, pois esta vai buscar todos os artigos à blockchain, ficando com a mesma informação que todas as outras sem ser necessário processos de sincronização. 
- Isto aplica-se também às atualizações, todas as apps irão atualizar as suas bases de dados com a mesma informação presente na blockchain.
- Qualquer base de dados de uma WebApp, caso comprometida, não é necessário ser recuperada, pois a informação esta presente na blockchain, sendo a sua recuperação fazer uma nova cópia dos dados da blockchain.
- É possível resumir a utilidade deste projeto à Persistencia de dados entre varias instituições e as respetivas aplicações a correr em com a mesma informação mas em ambientes diferentes. 
