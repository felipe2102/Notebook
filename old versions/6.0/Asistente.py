# Bibliotecas

import os
import os.path
import PySimpleGUI as sg 
from pathlib import Path
import datetime
from time import sleep

#Sistema que detecta o dia da semana atual
Dia = datetime.datetime.now().weekday()
Dias = ['Segunda-feira', 'terça', 'Quarta-feira', 'Quinta feira', 'Sexta-feira', 'sábado', 'Domingo']
Dia_Atual=Dias[Dia]
Aulas_Dia = None

#variaveis

def setup():
if os.path.exists('./Data'):
    Aulas_Seg = open('Data/Aulas_Segunda-Feira.txt','r')
    Aulas_Ter = open('Data/Aulas_Terça-Feira.txt','r')
    Aulas_Qua = open('Data/Aulas_Quarta-Feira.txt','r')
    Aulas_Qui = open('Data/Aulas_Quinta-Feira.txt','r')
    Aulas_Sex = open('Data/Aulas_Sexta-Feira.txt','r')
    aula_segunda = Aulas_Seg.read()
    aula_terça = Aulas_Ter.read()
    aula_quarta = Aulas_Qua.read()
    aula_quinta = Aulas_Qui.read()
    aula_sexta = Aulas_Sex.read()
    answer = sg.popup_get_text('O que você quer?')

    if answer == 'Aulas':
        if Dia_Atual == 'Segunda-feira' :
            sg.popup(aula_segunda)
        else :
            if Dia_Atual == 'terça' :
                sg.popup(aula_terça)
            else :
                if Dia_Atual == 'Quarta-feira' :
                    sg.popup(aula_quarta)
                else :
                    if Dia_Atual == 'Quinta feira' :
                        sg.popup(aula_quinta)
                    else :
                        if Dia_Atual == 'Sexta-feira' :
                            sg.popup(aula_sexta)
else:
    setup()
