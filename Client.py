import socket
import sys
import os
import threading
import time

class cliente:
      def __init__(self,rHost = socket.gethostname(), rPort = 80 ):
            ''' Inicializa as Variaveis iniciais do cliente '''
            self.rHost = rHost
            self.rPort = rPort

      def sendMsg (self):
            ''' envia a msg ao servidor '''
            while True:
                  msg = input ( )
                  self.s.send (msg.encode ("utf-8"))
            
      def toReciveMsg (self):
            # recebe mensagem do servidor
            while True:
                  msg = self.s.recv(4096).decode("utf-8")
                  print (msg)

      def tcpConect (self,conect = 0):
            #conectar o cliente ao serve
            # por padrão conect é 0 ou seja rede local, diferente de 0  rede externa
            try:
                  self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	#Cria a conexão TCP 
            except:
                  print('[###] Erro ao criar o socket')
                  os._exit(1)
            address = (socket.gethostname(),80)
            if conect != 0 : address = (self.rHost,self.rPort) # para conexao fora de lan
            try:
                  self.s.connect(address)	#conecta ao servidor
            except:
                  print(" [###] Servidor não está conectado no momento.")
                  sys.exit()
      def main (self,conect):
            self.tcpConect(conect)
            
            thread = threading.Thread(target = self.toReciveMsg)
            thread.start()
            
            self.sendMsg()
class inicioClient :
      def __init__(self):
            pass
      def inicializacao ():
            while True :
                  option = str(input("[**] Option Default [Y/n] ? : ")).upper()
                  if option =='':
                        option = "Y"
                  if option == "Y":
                        print ("[**] Inicialização em rede < LAN >")
                        client = cliente()
                        client.main(1)
                        break
                  if option == "N":
                        while True:
                              rHost = str(input("   [*]Set rHost: "))
                              rPort = int(input("   [*]Set rPort: "))
                                    
                              if rHost != '' and rPort != '':
                                    break
                        print ("[**] Inicialização em rede < EXTERNA >")
                        client = cliente(rHost,rPort)
                        client.main(1)
                        break
  
                  
start = inicioClient
start.inicializacao()




			
            
