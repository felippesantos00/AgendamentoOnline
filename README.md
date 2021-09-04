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
            nomeCompleto
            senha
            confirmSenha
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
