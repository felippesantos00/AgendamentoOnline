from time import sleep
import PySimpleGUI as sg
import Banco as banco
from random import randint

def buscarAgendamento(): 
    if event == 'meusAgendamentos':
        window.FindElement('_output_').Update('')
        nomeCompleto = str(values['NomeCompleto'])
        senha = str(values['senha'])
        confirmSenha = str(values['senha'])
        banco.Banco().selectTable(nomeCompleto, senha, confirmSenha)

def agendar():
    if event == 'agendar': 
        nomeCompleto = str(values['NomeCompleto'])
        senha = str(values['senha']) 
        confirmSenha = str(values['senha'])
        tema = str(values['tema'])
        hora = str(values['hora'])
        data = str(values['data'])
        window.FindElement('_output_').Update('')
        idUser = banco.Banco().selectTable(nomeCompleto, senha, confirmSenha)
        banco.Banco().insertTable(0,nomeCompleto,senha,confirmSenha,idUser,data,tema,hora)
        
def todosAgendamento():
    if event == 'todosAgendamentos':
        window.FindElement('_output_').Update('')
        nomeCompleto = str(values['NomeCompleto'])
        senha = str(values['senha']) 
        confirmSenha = str(values['senha'])
        progressBar = window.FindElement('progressBar')
        progressBar.UpdateBar(0)
        a = 0
        for a in range(10000):
            progressBar.UpdateBar(a+1, 10000)
        progressBar.UpdateBar(0, 10000)
        banco.Banco().selectTable(nomeCompleto,senha,confirmSenha)
        
sg.theme('SystemDefault1')
temas = ['Brainstorm', 'Briefing', 'Apresentação', 'Encontro recorrente']
hours = ['10:00','10:30','11:00','11:30','12:00','12:30','13:00','13:30','14:00','14:30','15:30','16:00']
def win_1():
    layout = [
        [sg.Image(filename="imagens/201-calendar-1.png"),sg.Text("Agendamento de Reuniões",justification='center',size=(30,1))],
        [sg.Text("Nome Completo ",border_width=10,justification='left'), sg.Input(key='NomeCompleto',size=(20,1))],
        [sg.Text("Senha ",border_width=10,justification="left"),sg.Input(key='senha',password_char='*',size=(20,1))],
        [sg.Text("Selecione uma data")],
        [sg.CalendarButton("Calendario",format='%d-%m-%y'),sg.Input(size=(20,1),key='data')],
        [sg.Text("Selecione o tema da reunião"), sg.Text("Selecione o horario da reunião")],
        [sg.Combo(temas,size=(20,10),key='tema'),sg.Combo(hours,size=(20,10),key='hora')],
        [sg.Button("Agendar agora",key="agendar"), sg.Button("ver todos os agendamentos",key='todosAgendamentos'),sg.Button("Meus agendamentos",key='meusAgendamentos')],
        [sg.Button("Consultar Banco",key='banco'), sg.Button("Cadastrar Usuario",key='cadastrar')],
        [sg.Output(size=(60,7),key='_output_',echo_stdout_stderr=False)],
        [sg.ProgressBar(0,size=(20,5),key='progressBar')]
    ]
    return sg.Window('', layout,finalize=True)

def win_2():
    layout = [
        [sg.Text("Novo Usuario"),sg.Image(filename="imagens/201-add-user.png")],
        [sg.Text("Nome Usuario ")],
        [sg.Input(key='nomeNovo',size=(20,1))],
        [sg.Text("Senha ")],
        [sg.Input(key='senhaNova',password_char='*',size=(20,1))],
        [sg.Text("Confirmar Senha ")],
        [sg.Input(key='confirmSenhaNova',password_char='*',size=(20,1))],
        [sg.Button("Cadastrar",key='Cadastrar'),sg.Button("Cancelar",key='Cancelar')]
    ]
    return sg.Window('Cadastro', layout, finalize=True)

window1, window2 = win_1(), None
banco.Banco().createTable()
while True:
    window, event,values = sg.read_all_windows()       
    if event == sg.WIN_CLOSED or event == 'Cancelar' or event == 'Exit':
        window.close()
        if window == window2:
            window2 = None
        elif window == window1:
            break
    elif event == 'Calendario':
        date = sg.popup_get_date()
        if date:
            month, day, year = date
            window['data'].update(f"{day:0>2d}-{month:0>2d}-{year}")
    todosAgendamento()
    agendar()
    buscarAgendamento()
    if event == 'cadastrar' and not window2:
        window2 = win_2()
    if event == 'Cadastrar':
        idUser = randint(0, 1000)
        nomeNovo = str(values['nomeNovo'])
        senhaNova = str(values['senhaNova'])
        confirmSenhaNova = str(values['confirmSenhaNova'])
        banco.Banco().insertTable(1,nomeNovo,senhaNova,confirmSenhaNova,idUser,'','','')
        sleep(1)
        window2 = window.close()
    elif event == 'banco':
        window.FindElement('_output_').Update('')
        nomeCompleto = str(values['NomeCompleto'])
        senha = str(values['senha']) 
        confirmSenha = str(values['senha'])
        banco.Banco().selectTable(nomeCompleto, senha, confirmSenha)
window.close()
