# Agendamento Online de Reuniões

### Este projeto tem por finalidade registrar, acompanhar, descrever e finalizar um processo de agendamento de reuniões

# Agendamento.py
<style>
th {
    border: 1px solid black;
    text-align: center;
}
td {
    border:1px solid black;

}
</style>
## Funções
<table>
    <tr >
        <th>Nome</th>
        <th>Descrição</th>
        <th>Paramêtros</th>
    </tr>
    <tr>
        <td>buscarAgendamento()</td>
        <td>Busca no banco de dados as informações dos seus agendamentos</td>
        <td>
            nomeCompleto
            senha
            confirmSenha
        </td>
    </tr>
    <tr>
        <td>agendar()</td>
        <td>Agenda as informações necessarias para registro</td>
        <td>
nomeCompleto, senha, confirmSenha, tema, hora, data, idUser
        </td>
    </tr>
    <tr>
        <td>todosAgendamento()</td>
        <td>Buscar todos os registros atuais de reuniões</td>
        <td>
nomeCompleto, senha, confirmSenha
        </td>
    </tr>
</table>

### Exemplos


# Banco.py

<style>
th {
    border: 1px solid black;
    text-align: center;
}
td {
    border:1px solid black;

}
</style>
## Funções
<table>
    <tr >
        <th>Nome</th>
        <th>Descrição</th>
        <th>Paramêtros</th>
    </tr>
    <tr>
        <td>createTable()</td>
        <td>Criar novas tabelas</td>
        <td>
            lista de querys
        </td>
    </tr>
    <tr>
        <td>insertTable()</td>
        <td>Inserir usuarios e reuniões nas tabelas</td>
        <td>
nomeCompleto, senha, confirmSenha, tema, hora, data, idUser
        </td>
    </tr>
    <tr>
        <td>selectTable()</td>
        <td>Buscar informações por usuario, todos os usuarios, todas as reuniões e todas as reuniões atreladas ao usuario</td>
        <td>
event, nomeCompleto, senha, confirmSenha, idUser, data, tema, hora
        </td>
    </tr>
</table>

### Exemplos

```python
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
```
```python
def insertTable(self, event,nomeCompleto, senha, confirmSenha, idUser, data, tema, hora):
    c = self.conexao.cursor()
    query=[
        "INSERT INTO reunioes (nome, data, tema, hora,idusuario_idusuario) VALUES ('%s', '%s', '%s','%s', %d);"%(nomeCompleto, data,tema,hora,idUser),
        "INSERT INTO idusuario (nome, senha, confirmSenha) VALUES ('%s','%s','%s')"% (nomeCompleto,senha,confirmSenha)
        ]
    if event == 1:  #adicionar usuario
        if senha == confirmSenha:
            print("Novo usuario: ",nomeCompleto)
            print("Senha: ",senha)
            print("Cadastrado com sucesso")
        else:
            return print("senha e confirmação de senha invalida")
    if event == 0: #
        c.execute(query[event])
        print("agendamento concluido")
    self.conexao.commit()
    c.close()
```