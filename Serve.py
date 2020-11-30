import socket
import threading
import os
import time

class Servidor:
      def __init__(self,rHost = socket.gethostname(), rPort = 80 ): #detemina as portas do servidor
                                                                              #por padrão utiliza serve lan 
            self.rHost = rHost
            self.sPort = rPort
            self.clients = {}


            self.tcp = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
            self.tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


            infoSocket = (rHost,rPort)
            
            self.tcp.bind (infoSocket)
            self.tcp.listen(5) # servidor a espera de cliente
            
            print("\n[**] Servidor a espera: [{}]".format (infoSocket))
            
      def entConect (self): # aqui estabele a conexão co,m o cliente 
             while True:
                  (client, addr) = self.tcp.accept() # client termo usado para classificar os clientes 
                  self.addr = addr # addr tratase do ip e porta
                  
                  print ("[*] Cliente Conect [{}:{}]".format (addr[0],addr[1])) # print so no servidor
                  
                  thread = threading.Thread(target = self.welcomeCliente, args = (client,)) # parametro que aceita mais de um cliente e direciona a parte inicial
                  thread.start()
      def welcomeCliente (self,client): # parte inicial e nome do cliente 
            client.send('[**] Conexão Bem Sucedida ... \n    [*] Digite um nome: '.encode('utf-8')) # envia ao cliente
            name = client.recv(1024).decode ("utf-8")

            print ("[*] Cliente {} conectado".format(name))
            self.clients[name] = (client) # adiciona ao dicionario clientes 

            msg = "[@] User Conectado"
            self.sendToMsg (client,msg) # aqui se redireciona as mensage é funciona tipo um loop 
            self.listenMsg(client) # recebe novas mensagens e retorna a esta função
            
      
      def sendToMsg (self,client,msg): # direciona as mensagens 
            def whatUser (): # devine quem é remetente e quem é destinatario 
                  rem = " "
                  des = " "
                  for name in (self.clients):
                        if client == self.clients[name]: rem = name # nome do remetente whatUser()[0]
                        if client != self.clients[name]: des = name # nome do destinatario whatUser()[1]
                  return rem,des
            
            if (whatUser()[1]) == " ": # definer se ele estar sozinho
                  while True:
                        msg = " [##] Parece que Você esta sozinho ..."
                        self.sendMsg (whatUser()[0],msg)
                        # parametros a baixo ser substituido por uma tela de carregamento
                        for i in range (1,10):
                              msg = "Aguarde "
                              self.sendMsg (whatUser()[0], msg)
                              time.sleep (1)
                              
                              
                        
                        if (whatUser()[1]) != " ": # nao estar sozinho 
                              os.system('clear')
                              
                              msg = "[*] User : " + whatUser()[1] + " Pronto para o Bate Papo"
                              self.sendMsg (whatUser()[0],msg)
                              break
            
            else:
                  msg = "< " + whatUser()[0] + " >" + msg
                  self.sendMsg (whatUser()[1],msg)
                        
            
            
            

      def sendMsg (self,clientt,msg): # envia a mensagem
            # pretendo separar mensagem do servidor (com parametros '[') do user 
            try:
                  client = self.clients[clientt] # acessa ao dicionario e procura o cliente alvo 
                  client.send((msg).encode('utf-8'))
            except:
                  pass
      def listenMsg (self,client): # recebe toadas as mensagens 
            while True:
                  try:
                        msg = client.recv(4026).decode('utf-8')
                        #self.comando_msg(apelido, msg)  função desabilitada que vai testar se o nome é repitido ou se é comando interno que vai ser criado futuramente
                        self.sendToMsg(client,msg)
                  except:
                        break

                  
      def main(self):
           #Começa a execução do servidor, aqui as threads são inicializadas e enviadas aos respectivos métodos'''
            try:
                  self.entConect()
                  print ("[!] Tudo Correto com o servidor")
            except :
                  pass
            

class defaultServe: # para iniciar o servidor em modo lan (default) ou em rede externa
      
      def __init__(self):
            option = str (input( "[**] Option Defaut  [Y/n]:")).upper()
            if option == '':
                  option = "Y"
            self.introServe(option)
            pass
      
      def introServe(self,option = "Y"):
            if option == "Y":
                  print ("[**] Inicialização em rede < LAN >")
                  serve = Servidor()
                  serve.main()
            if option == "N":
                  print ("[**] Inicialização em rede < EXTERNA >")
                  info=self.infohostAndPort()
                  serve = Servidor(info[0],info[1])
                  serve.main()
            else :
                  print ("Option Invalida")
                  defaultServe()
      def infohostAndPort (self):
            while True:
                  rHost = str(input("[@] rHost = "))
                  rPort = int(input("[@] rPort = "))
                  if rHost != '' and rHost != '' :
                        break 
            return rHost,rPort
       
            

defaultServe()   
