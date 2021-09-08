import sqlite3
from time import sleep
class Banco():
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')

    def createTable(self):
        c = self.conexao.cursor()
        queryConstrutor = ["CREATE TABLE idusuario(\
        ididusuario  INTEGER  NOT NULL PRIMARY KEY \
        ,nome VARCHAR(28) NOT NULL\
        ,senha INTEGER  NOT NULL\
        ,confirmSenha INTEGER  NOT NULL\
        );",
        "CREATE TABLE reunioes(\
        idreunioes INTEGER  NOT NULL PRIMARY KEY \
        ,nome VARCHAR(28) NOT NULL\
        ,tema VARCHAR(19)\
        ,data DATE \
        ,hora VARCHAR(5)\
        ,idusuario_idusuario INTEGER  NOT NULL\
        );"
        ]
        try:
            print("Iniciando....")
            sleep(1)
            print("Banco Estruturado")
            for query in queryConstrutor:
                c.execute(query)
                self.conexao.commit()
        except:
            print()
        c.close()
    
    def insertTable(self, event,nomeCompleto, senha, confirmSenha, idUser, data, tema, hora):
        querys =[
            "INSERT INTO reunioes (nome, data, tema, hora,idusuario_idusuario) VALUES ('%s', '%s', '%s','%s', %d);"%(nomeCompleto, data,tema,hora,idUser),
            "INSERT INTO idusuario (ididusuario, nome, senha, confirmSenha) VALUES ('%d','%s','%s','%s');"% (idUser, nomeCompleto,senha,confirmSenha)
            ]
        c = self.conexao.cursor()
        if event == 'Cadastrar' and senha == confirmSenha:    #adicionar usuario
            c.execute(querys[1])
            print("Novo usuario: ",nomeCompleto)
            print("Senha: ",senha)
            print("Cadastrado com sucesso")
            self.conexao.commit()
            c.close()
        elif event == 'agendar' and idUser != 'not sucess' and senha == confirmSenha:
            c.execute(querys[0])
            print()
            print("Usuario: %s foi confirmado"% (nomeCompleto))
            print("Agendamento concluido")
            print("_______________________________________")
            print()
            self.conexao.commit()
            c.close()
        else:
            print("id do usuario não retornou")

    def selectTable(self, event, nomeCompleto, senha, confirmSenha):
        querys = [
            ("SELECT * FROM reunioes"),
            ("SELECT * FROM idusuario WHERE nome='%s' and senha='%s' and confirmSenha='%s'" % (nomeCompleto,senha,confirmSenha)),
            ("SELECT * FROM reunioes LEFT JOIN idusuario ON reunioes.nome = idusuario.nome WHERE reunioes.nome = '%s' and idusuario.senha = '%s' and idusuario.confirmSenha = '%s' "% (nomeCompleto,senha,confirmSenha))
            ]
        c = self.conexao.cursor()
        if event == 'meusAgendamentos':
            c.execute(querys[2])
            linhas = c.fetchall()
            for linha in linhas:
                print("Nome: ", linha[1])
                print("Data:", linha[2])
                print("Tema da reunião:", linha[3])
                print("Horário da reunião:", linha[4])
                print("id usuario: ",linha[5])
                print("_______________________________________")
                print()
                print("executado com sucesso")
        elif event == 'validaUser' or event == 'agendar':
            c.execute(querys[1])
            linhas = c.fetchall()
            if linhas == []:
                print("Usuario não encontrado, favor verificar senha ou nome completo corretamente")
            else:    
                for linha in linhas:
                    try:
                        print()
                        print("Id: ", linha[0])
                        print("Nome:", linha[1])
                        print("Senha:", linha[2])
                        print("_______________________________________")
                        print()
                        print("Usuario verificado com sucesso")
                        print()
                        return "\nId: %s\nNome: %s\nSenha: %s\nUsuario verificado com sucesso"% (linha[0],linha[1],linha[2])
                    except:
                        return 'not sucess'
        elif event == 'todosAgendamentos':    
            c.execute(querys[0])
            linhas = c.fetchall()
            for linha in linhas:
                print("Nome: ", linha[1])
                print("Data:", linha[2])
                print("Tema da reunião:", linha[3])
                print("Horário da reunião:", linha[4])
                print("id usuario: ",linha[5])
                print("_______________________________________")
                print()
                print("executado com sucesso")
        self.conexao.commit()
        c.close()