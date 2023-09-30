# Aplicação Cliente-Servidor
Aplicação python para simular servidor e cliente 

**Grupo:**
- Caio Finotti Bosco - 514303
- Luan Roger Santos Clementino - 517173
- Mateus de Sousa Araújo - 500924

## Objetivo

Este é um sistema de comunicação cliente-servidor feito em Python para um trabalho da disciplina de Redes, que oferece as seguintes funcionalidades:

1. Envio de arquivos do cliente para o servidor.
2. Obtenção da hora atual do servidor.
3. Envio de dados do sistema do servidor para o cliente.
4. Listagem de arquivos no servidor.
5. Encerrar conexão

## Requisitos

- Python 3.x instalado no cliente e no servidor.
- Biblioteca socket padrão do Python.

## Configuração

1. Clone este repositório em seu sistema local:

git clone https://github.com/MateusAra/Sockets.git

2. Em seu terminal, abra a pasta "Servidor" e execute o comando a seguir:

python3 servidorTCP.py

3. Em seguida, abra a pasta "Cliente" em outro terminal e execute o comando:

python3 clienteTCP.py


## Uso

O sistema oferece um menu interativo no cliente para escolher entre as funcionalidades disponíveis. Aqui está como usar cada uma delas:

1. **Envio de Dados do Sistema**
   - Digite "1" para escolher a opção de envio de dados do sistema no menu.
   - Os dados do sistema do servidor, como informações de hardware e sistema operacional, serão exibidos no cliente.

2. **Obtenção da Hora Atual**
   - Digite "2" para escolher a opção de obter a hora atual no menu.
   - A hora atual do servidor será exibida no cliente.

3. **Envio de Arquivos do Servidor**
   - Digite "3" para escolher a opção de envio de arquivos no menu.
   - Digite o nome do arquivo que você deseja receber.
   - O arquivo será transferido do servidor e armazenado na pasta "Cliente".

4. **Listagem de Arquivos**
   - Digite "4" para escolher a opção de listagem de arquivos no menu.
   - Uma lista de arquivos no servidor será exibida no cliente.

5. **Encerramento de Conexão**
   - Digite "5" para escolher a opção de sair (encerrar conexão) no menu.
   - A conexão do cliente com o servidor será encerrada.

## Múltiplas Conexões

Caso queira fazer mais de uma conexão com o cliente, inicie o servidor uma vez e, em seguida, abra diferentes abas do terminal e inicie o cliente em cada uma delas.
