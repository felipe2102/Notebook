#Bibliotecas
import PySimpleGUI as sg
from pathlib import Path
#Variaveis
Usuario = open('Username.txt','w')
Aulas_Seg = open('Aulas_Segunda-Feira.txt','w')
Aulas_Ter = open('Aulas_Terça-Feira.txt','w')
Aulas_Qua = open('Aulas_Quarta-Feira.txt','w')
Aulas_Qui = open('Aulas_Quinta-Feira.txt','w')
Aulas_Sex = open('Aulas_Sexta-Feira.txt','w')
#Janelas
sg.popup("para começarmos vamos configurar algumas coisas primeiro.")
nome = sg.PopupGetText("Qual o seu nome?")
Aulas_Segunda = sg.PopupGetText('Quais aulas você tem na segunda?')
Aulas_Terça = sg.PopupGetText('Quais aulas você tem na terça?')
Aulas_Quarta = sg.PopupGetText('Quais aulas você tem na quarta?')
Aulas_Quinta = sg.PopupGetText('Quais aulas você tem na quinta?')
Aulas_Sexta = sg.PopupGetText('Quais aulas você tem na sexta?')
sg.popup('configuração finalizada, você já pode abrir o arquivo principal!')

#Salvar os arquivos
Usuario.write(nome)
Aulas_Seg.write(Aulas_Segunda)
Aulas_Ter.write(Aulas_Terça)
Aulas_Qua.write(Aulas_Quarta)
Aulas_Qui.write(Aulas_Quinta)
Aulas_Sex.write(Aulas_Sexta)