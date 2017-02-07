import socket
import sys

cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria objeto socket
host = socket.gethostname() #pega o nome do pc
port = 12310 #seta a porta do servidor para conexão
cs.connect(('xxx.xxx.x.xx',port)) #seta os dados do host e a port
msg = cs.recv(1024) #seta o tamanho maximo da mensagem
cs.close() #encerra a conexão com o servidor
print msg.decode('ascii') #mostra a mensagem vinda do servidor
