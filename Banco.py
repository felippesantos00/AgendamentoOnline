import sqlite3

class Banco():
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()
        print("Iniciando....")

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
            for query in queryConstrutor:
                c.execute(query)
                print("Executando query:" + query)
                self.conexao.commit()
        except:
            print("As tabelas ja foram criadas anteriormente")
        c.close()
    
    def insertTable(self, event,nomeCompleto, senha, confirmSenha, idUser, data, tema, hora):
        c = self.conexao.cursor()
        querys =[
            "INSERT INTO reunioes (nome, data, tema, hora,idusuario_idusuario) VALUES ('%s', '%s', '%s','%s', %d);"%(nomeCompleto, data,tema,hora,idUser),
            "INSERT INTO idusuario (ididusuario, nome, senha, confirmSenha) VALUES ('%d','%s','%s','%s');"% (idUser, nomeCompleto,senha,confirmSenha)
            ]
        for query in querys:
            if event == 1:  #adicionar usuario
                if senha == confirmSenha:
                    print("Novo usuario: ",nomeCompleto)
                    print("Senha: ",senha)
                    print("Cadastrado com sucesso")
                    self.conexao.commit()
                    c.close()
                else:
                    return print("senha e confirmação de senha invalida")
            elif event == 0: #
                c.execute(query[event])
                print("agendamento concluido")
                self.conexao.commit()
                c.close()

    def selectTable(self, event, nomeCompleto, senha, confirmSenha):
        querys = [
            ("SELECT * FROM loginUsuarios"),
            ("SELECT * FROM reunioes"),
            ("SELECT * FROM idusuario WHERE nome='%s' and senha='%s' and confirmSenha='%s'" % (nomeCompleto,senha,confirmSenha)),
            ("SELECT * FROM reunioes LEFT JOIN idusuario ON reunioes.nome = idusuario.nome WHERE reunioes.nome = '%s' and idusuario.senha = '%s' and idusuario.confirmSenha = '%s' "% (nomeCompleto,senha,confirmSenha))
            ]
        if senha == confirmSenha:
            c = self.conexao.cursor()
            c.execute(querys[event])
            linhas = c.fetchall()
            if event == 1:
                for linha in linhas: # Consultar todos as reunioes
                    print("Nome: ", linha[1])
                    print("Data:", linha[2])
                    print("Tema da reunião:", linha[3])
                    print("Horário da reunião:", linha[4])
                    print("id usuario: ",linha[5])
                    print("_______________________________________")
                    print()
                print("executado com sucesso")
            if event == 3 or event == 2: # Consultar minhas as reunioes ou meu usuario
                for linha in linhas:
                    print("Nome: ", linha[1])
                    print("Data:", linha[2])
                    print("Tema da reunião:", linha[3])
                    print("Horário da reunião:", linha[4])
                    print("id usuario: ",linha[5])
                    print("_______________________________________")
                    print()
                    return linha[5]
                print("executado com sucesso")
        else:
            return print('Senha incorreta')
        self.conexao.commit()
        c.close()