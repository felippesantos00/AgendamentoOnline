import socket
import re
host = socket.gethostbyname(socket.gethostname())
def client(host, port=8080):
    while True:
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect the socket to the server
        server_address = (host, port)
        print ("Connecting to %s port %s" % server_address)
        sock.connect(server_address)
        # Send data
        message = str(input("Digite sua mensagem"))
        pattern = re.compile(message)
        if message == 'login':
            print("Informe seu login e senha")
            nomeCompleto = str(input("Nome: "))
            senha = str(input("Sua senha: "))
            message = "\nSolicitação de login\nNome: %s\nSenha: %s"%(nomeCompleto,senha)
            message.split('\n')
        if pattern.match('s'):
            print('fechando conexao')
            sock.close()
            break
        print ("Sending %s" % message)
        sock.sendall(message.encode('utf-8'))
        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(1024)
            amount_received += len(data)
            print ("Received: %s" % data.decode('utf-8'))
    #def send():

    #def received():    
        

client(host)