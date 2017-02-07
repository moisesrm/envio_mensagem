import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria objeto socket
host = '' #define ip do servidor ao qual irá se conectar, mas como é o servidor não precisa definir
port = 1234 #define a porta para que os clientes possam se conectar
s.bind((host,port)) #seta o host e a port no socket
s.listen(10) #tempo de espera para o cliente se conectar
while 1: #manter a conexão
  cs,addr = s.accept() #estabelece a conexão com o cliente
  cs.send('Funcionando') #envia a mensagem para o cliente
s.close() #encerra a conexão