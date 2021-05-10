#Bibliotecas usadas
import PySimpleGUI as sg
from datetime import datetime
from pathlib import Path
import os.path
import os

#Verificar qual o dia da semana Atual e define ele em uma variavel
Dia = datetime.now().weekday()
Dias_semana = ['Segunda-feira', 'terça', 'Quarta-feira', 'Quinta feira', 'Sexta-feira', 'sábado', 'Domingo']
Dia_Atual=Dias_semana[Dia]

#Cria os arquivos caso eles não existam 
def setup():
	#Cria os arquivos
	os.mkdir('./Data')
	os.mkdir('./Data/Lessons')
	Aulas_Seg = open('Data/Lessons/Aulas_Segunda-Feira.txt','w')
	Aulas_Ter = open('Data/Lessons/Aulas_Terça-Feira.txt','w')
	Aulas_Qua = open('Data/Lessons/Aulas_Quarta-Feira.txt','w')
	Aulas_Qui = open('Data/Lessons/Aulas_Quinta-Feira.txt','w')
	Aulas_Sex = open('Data/Lessons/Aulas_Sexta-Feira.txt','w')
	#Pega as informações das aulas do úsuario
	sg.popup("parece que você não tem nenhuma aula configurada ;-;")
	Aulas_Segunda = sg.PopupGetText('Quais aulas você tem na segunda?')
	Aulas_Terça = sg.PopupGetText('Quais aulas você tem na terça?')
	Aulas_Quarta = sg.PopupGetText('Quais aulas você tem na quarta?')
	Aulas_Quinta = sg.PopupGetText('Quais aulas você tem na quinta?')
	Aulas_Sexta = sg.PopupGetText('Quais aulas você tem na sexta?')
	sg.popup('configuração finalizada!')
	#Escreve as alterações nos arquivos
	Aulas_Seg.write(Aulas_Segunda)
	Aulas_Ter.write(Aulas_Terça)
	Aulas_Qua.write(Aulas_Quarta)
	Aulas_Qui.write(Aulas_Quinta)
	Aulas_Sex.write(Aulas_Sexta)

#Verifica quais as aulas do dia
def home():
	sg.theme('DarkGrey13')
	layout = [
		[sg.Text('O que você deseja?')],
		[sg.Button('Aulas'), sg.Button('Ajuda'), sg.Exit()]
		]
	return sg.Window('Home', layout, element_justification='c', size=(170,70), finalize=True)

def help():
	sg.theme('DarkGrey13')
	layout = [
		[sg.Text('Se você ver algum bug, você pode reportar ele em:')],
		[sg.Text('https://github.com/Felipe2102/Assistente-Escolar/issues/new')],
		[sg.Button('Voltar')]
	]
	return sg.Window('Ajuda', layout, element_justification='c', finalize=True)
#Tenta acessar os arquivos, se os arquivos não existirem ele abre a janela de configuração
try:
	aula_seg = open('Data/Lessons/Aulas_Segunda-Feira.txt', 'r').read()
	aula_ter = open('Data/Lessons/Aulas_Terça-Feira.txt', 'r').read()
	aula_qua = open('Data/Lessons/Aulas_Quarta-Feira.txt', 'r').read()
	aula_qui = open('Data/Lessons/Aulas_Quinta-Feira.txt', 'r').read()
	aula_sex = open('Data/Lessons/Aulas_Sexta-Feira.txt', 'r').read()
except FileNotFoundError:
	setup()
#Verifica novamente os arquivos para caso o usuário tenha configurado no comando anterior 
#ele tenha como usar o programa sem precisar reiniciar o programa
try:
	aula_seg = open('Data/Lessons/Aulas_Segunda-Feira.txt', 'r').read()
	aula_ter = open('Data/Lessons/Aulas_Terça-Feira.txt', 'r').read()
	aula_qua = open('Data/Lessons/Aulas_Quarta-Feira.txt', 'r').read()
	aula_qui = open('Data/Lessons/Aulas_Quinta-Feira.txt', 'r').read()
	aula_sex = open('Data/Lessons/Aulas_Sexta-Feira.txt', 'r').read()
except FileNotFoundError:
	setup()

index, ajuda = home(), None

while True:
	#Lê o valor da janela
	window, event, values = sg.read_all_windows()
	#Verifica se a janela foi fechada
	if window == index and event == sg.WIN_CLOSED or event == 'Exit':
		break
	if window == index and event == 'Ajuda':
		ajuda = help()
		index.hide()
	if window == ajuda and event == 'Voltar':
		index.un_hide()
		ajuda.hide()
	#Verifica o Input do Usuário
	if window == index and event == 'Aulas':
		if Dia_Atual == 'Segunda-feira':
			sg.popup(aula_seg)
		elif Dia_Atual == 'terça':
			sg.popup(aula_ter)
		elif Dia_Atual == 'Quarta-feira':
			sg.popup(aula_qua)
		elif Dia_Atual == 'Quinta feira':
			sg.popup(aula_qui)
		elif Dia_Atual == 'Sexta-feira' :
			sg.popup(aula_sex)