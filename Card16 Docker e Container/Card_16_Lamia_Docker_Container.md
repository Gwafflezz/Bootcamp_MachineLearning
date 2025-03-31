 
# Relatório 16:  Docker e Containers para Aplicações 

**Davi Bezerra Barros**


**Container:** Um container é um ambiente isolado onde uma aplicação e todas as suas dependências são hospedadas, e podem ser executado em qualquer  máquina que tenha um mecanismo para rodar container, como o Docker, sem precisar se preocupar com as especificidades do sistema operacional

**Imagem:** É o "template" que contém as instruções para a criação de um container, e é composta por múltiplas camadas empilhadas, cada uma especificando uma característica do ambiente. A imagem também contém os códigos binários, runtimes, dependências, filesytem e sistema operacional necessários para rodar uma aplicação quando instanciada em um container.

**Comandos de manupulação de containers**

- **Docker container ls:** Lista os containers
- **Docker container stop < container >:** Para container em execução
- **Docker container start** :  inicializa o container 
- **Docker container cp < src > < dst >:** copia o container
- **Docker container rm < nome_id >:** remove um container 
- **Docker container attach < nome_id >:** se anexa ao container em execução
- **Docker container inspect < nome_id_ >:** inspeciona as informações sobre o container
- **Docker container rename < nome_antigo> < nome_novo>:** Renomeia o container

**Filesystem**
![[Pasted image 20240804182225.png#center]]

***Modo iterativo:*** O modo iterativo permite que o usuário acesse e interaja com um container enquanto ele está sendo executado, para fazer as mudanças que forem necessárias.

Criando containers iterativamente:
![[Pasted image 20240804182159.png#center]]

***EXEC:*** O comando **Exec** permite que o usuário execute comandos no container ja em execução, sem a necessidade de entrar em seu ambiente.

Executando comandos com **exec**:
![[Pasted image 20240805155457.png#center]]
![[Pasted image 20240805155539.png#center]]

Copiando um diretório para o container:
![[Pasted image 20240805155951.png#center]]
![[Pasted image 20240805155927.png#center]]

Copiando do container para um diretório do sistema: 
![[Pasted image 20240805162857.png#center]]

**Mapeando volumes**

Ao deletar um container, todos os dados contidos nele são deletados também. Para evitar isso, os containers usam volumes para armazenar as informações e salvar seu estado, o que é muito útil para preservar logs, arquivos de configuração, datasets, etc..

![[Pasted image 20240805170135.png#center]]

**Mapeamento de portas**

Entendendo o processo de mapeamento de portas para fazer deploy de aplicações. As portas do processo podem ser mapeadas para uma porta especifica do hospedeiro, permitindo o acesso de outros hosts da rede ao server.

Criando um container com uma imagem do server Ngnix:
![[Pasted image 20240814140851.png#center]]

Acessando o server a partir do ip fornecido pelo comando inspect:
```
PS C:\Users\davi.barros> docker container inspect nginx
```
![[Pasted image 20240814141144.png#center]]
![[Pasted image 20240814181037.png#center]]

Criando um novo container mapeando a porta 80 do host na porta 80 do container: 
```
docker container run -d -p 80:80 ngnix ngnix
```
![[Pasted image 20240814182104.png#center]]

**Gerando imagens a partir de containers**

Assim como volumes são utilizados para guardar os dados gerados por um container, imagens podem ser geradas para salvar  seu estado. Isso facilita o processo de desenvolvimento ao permitir o compartilhamento e versionamento da aplicação. A criação de uma imagem base pode servir como ponto de partida para a criação de novos containers, como classes de objetos em programação orientada a objetos.

- Dockerfiles: Arquivo de texto que contém todas as instruções para construir uma imagem, define os comandos que o Docker irá executar sequencialmente para criar o ambiente de execução.

Gerando imagem a partir de um container:
![[Pasted image 20240815144733.png#center]]

Criando um novo container a partir da imagem gerada:
![[Pasted image 20240815144958.png#center]]

- **Arquivo TAR:**  *Tape ARchive*, agrupa diversos arquivos em um único arquivo, facilitando o backup e armazanamento. É o formato em que são exportadas as imagens utilizadas em containers. 

Salvando a imagem como um arquivo TAR:
![[Pasted image 20240815153227.png#center]]
Carregando a imagem  a partir de um arquivo .tar:
![[Pasted image 20240815153310.png#center]]

***Docker image history***: Exibe o historico de uma imagem do docker, trazendo informações sobre sua criação, alterações, tamanho, camadas que a compõe e outras informações relevantes.
![[Pasted image 20240815154827.png#center]]

***Docker image import***: Utilizado para criar uma imagem docker a partir de um arquivo .tar, reaproveitando um sistema de arquivos como base para a nova imagem.
![[Pasted image 20240815155810.png#center]]

Outros comandos úteis para gerenciamento de imagens:

- ***Docker image inspect:*** Usado para obter informaçoes detalhadas sobre a imagem
- ***Docker image prune:*** Limpa imagens não utilizadas
- ***Docker image pull:*** Baixa uma imagem de um registro
- ***Docker image tag:*** Cria um novo nome para uma imagem existente
- ***Docker image push:*** Envia uma magem para um registro


***Comandos utilizados para gerenciar imagens de containers:***

- **build** - Constrói uma imagem a partir de um Dockerfile.
- **history** - Mostra o histórico de uma imagem.
- **import** - Importa o conteúdo de um arquivo tar para criar uma imagem de sistema de arquivos.
- **inspect** - Exibe informações detalhadas sobre uma ou mais imagens.
- **load** - Carrega uma imagem a partir de um arquivo tar ou da entrada padrão (STDIN).
- **ls** - Lista as imagens.
- **prune** - Remove imagens não utilizadas.
- **pull** - Baixa (puxa) uma imagem ou repositório de um registro.
- **push** - Envia (empurra) uma imagem ou repositório para um registro.
- **rm** - Remove uma ou mais imagens.
- **save** - Salva uma ou mais imagens em um arquivo tar (streaming para STDOUT por padrão).
- **tag** - Cria uma tag (etiqueta) TARGET_IMAGE que se refere à SOURCE_IMAGE.


***Comando utilizados para gerenciamento do ambiente de execução dos containers (Docker engine):***

- **Docker system info**:  Informaçoes sobre o docker, containers e sobre a máquina hospedeira
- **Docker system prune:** Deleta todos os containers, imagens e redes não utilizadas.
- **Docker image prune:** Remove todas as imagens nao associadas a containers
- **Docker container prune:** Limpa todos os containers não utilizados
- **Docker network prune:** Remove todas as redes não utilizadas




