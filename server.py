import socket
import Banco as banco
import re
host = socket.gethostbyname(socket.gethostname())
# functions
def server(host, port=8080):
    data_payload = 2048 #The maximum amount of data to be received at once
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
    # Enable reuse address/port
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the port
    server_address = (host, port)
    print ("Starting up echo server  on %s port %s" % server_address)
    sock.bind(server_address)
    # Listen to clients, argument specifies the max no. of queued connections
    sock.listen()
    print('aguardando conexão de um cliente')
    i = 0    
    
    while True:
        client, address = sock.accept()
        data = client.recv(data_payload)
        print ('conectado em', address)
        if data:
            message = data.decode('utf-8')
            pattern = 'Solicitação de (login)'
            recvConfirm = re.sub(pattern,'\g<1>', message)
            if 'login' in recvConfirm:
                pattern = '\nSolicitação de login\nNome: (\w+)\nSenha: (\w+)'
                nomeCompleto = re.sub(pattern, '\g<1>', message)
                senha = re.sub(pattern, '\g<2>', message)
                confirmSenha = senha
                enviando = banco.Banco().selectTable("validaUser", nomeCompleto,senha, confirmSenha)
                if enviando != None:
                    enviando.split('\n')
                else:
                    enviando = "Não foi possivel realizar o login, verifique seu usuario e senha"    
                client.send(bytes(enviando, "utf-8"))
            else:
                client.send(data)
        client.close()
        if not data:
            print('fechando conexão')
            client.close()
            break
            # end connection
    #def insert():
#Execution
server(host)


# servidor recebe cliente
# cliente requisita login
# servidor recebe requisição
# verifica no banco
# envia aprovação
