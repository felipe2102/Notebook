import PySimpleGUI as sg 
from pathlib import Path
import datetime
from time import sleep

#fileName = r'Username.txt'
#fileObj = Path('Username.txt')
Dia = datetime.datetime.now().weekday()
Dias = ['Segunda-feira', 'terça', 'Quarta-feira', 'Quinta feira', 'Sexta-feira', 'sábado', 'Domingo']
Dia_Atual=Dias[Dia]
Aulas_Dia = None

def  janela_login():
    sg.theme('SystemDefault')
    layout = [
        [sg.Text('Nome')],
        [sg.Input(key='Nome')],
        [sg.Button('Continuar')]
        ]
    return sg.Window('Login', layout=layout, finalize=True)
def janela_principal():
    sg.theme('SystemDefault')
    layout = [
        [sg.Text('O que você quer?')],
        [sg.Input(key='Resposta')],
        [sg.Button('Enviar')]
    ]
    return sg.Window('Digite', layout=layout, finalize=True)
janela1, janela2 = janela_login(), None

while True:
    window, event, values = sg.read_all_windows()
#    if fileObj.is_file() == True :
#        nome = open('Username.txt', 'r')
#        sg.popup('Bem Vindo!', str(nome.read()), title='Olá!')
#        janela1 = janela_principal()
#    else:
#        janela1 = janela_login()
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    if window == janela2 and event == sg.WIN_CLOSED:
        break
    if window == janela1 and event == 'Continuar':
        sg.popup('Bem Vindo!', title='Olá!')
        janela2 = janela_principal()
        janela1.hide()
    if window == janela2 and event == 'Enviar':
        if values['Resposta'] == 'Aulas':
            if Dia_Atual == 'Segunda-feira' :
                sg.popup('insira as aulas')
            else :
                if Dia_Atual == 'terça' :
                    sg.popup('insira as aulas')
                else :
                    if Dia_Atual == 'Quarta-feira' :
                        sg.popup('insira as aulas')
                    else :
                        if Dia_Atual == 'Quinta feira' :
                            sg.popup('insira as aulas')
                        else :
                            if Dia_Atual == 'Sexta-feira' :
                                sg.popup('insira as aulas teste')
