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
        for query in querys:
            c = self.conexao.cursor()
            try:
                c.execute(query)
                if event == 1 and senha == confirmSenha:
                    print("Novo usuario: ",nomeCompleto)
                    print("Senha: ",senha)
                    print("Cadastrado com sucesso")     
                    self.conexao.commit()
                    c.close()           
            except:
                self.conexao.commit()
                c.close()
                print("Usuario: %s foi confirmado"% (nomeCompleto))
                print("Agendamento concluido")
                print("_______________________________________")
                print()
            

    def selectTable(self, nomeCompleto, senha, confirmSenha):
        querys = [
            ("SELECT * FROM reunioes"),
            ("SELECT * FROM idusuario WHERE nome='%s' and senha='%s' and confirmSenha='%s'" % (nomeCompleto,senha,confirmSenha)),
            ("SELECT * FROM reunioes LEFT JOIN idusuario ON reunioes.nome = idusuario.nome WHERE reunioes.nome = '%s' and idusuario.senha = '%s' and idusuario.confirmSenha = '%s' "% (nomeCompleto,senha,confirmSenha))
            ]
        for query in querys:
            c = self.conexao.cursor()
            c.execute(query)
            linhas = c.fetchall()
            for linha in linhas:
                try:
                    print("Nome: ", linha[1])
                    print("Data:", linha[2])
                    print("Tema da reunião:", linha[3])
                    print("Horário da reunião:", linha[4])
                    print("id usuario: ",linha[5])
                    print("_______________________________________")
                    print()
                    print("executado com sucesso")
                except:
                    print("Id: ", linha[0])
                    print("Nome:", linha[1])
                    print("Senha:", linha[2])
                    print("_______________________________________")
                    print()
                    print("executado com sucesso")
                    return linha[0]
            self.conexao.commit()
            c.close()