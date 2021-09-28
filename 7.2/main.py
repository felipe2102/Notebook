#Bibliotecas usadas
import PySimpleGUI as sg
from datetime import datetime
import os

#Verificar qual o dia da semana Atual e define ele em uma variavel
Dia = datetime.now().weekday()

#Cria os arquivos caso eles não existam 
def setup():
	#Define o tema
	sg.theme('DarkGrey13')
	#Cria as pastas
	os.mkdir('./Data')
	os.mkdir('./Data/Lessons')

	#Cria os arquivos
	ASEG = open('Data/Lessons/Aulas_seg.txt','w')
	ATER = open('Data/Lessons/Aulas_ter.txt','w')
	AQUA = open('Data/Lessons/Aulas_qua.txt','w')
	AQUI = open('Data/Lessons/Aulas_qui.txt','w')
	ASEX = open('Data/Lessons/Aulas_sex.txt','w')
	#Fecha os arquivos criados
	ASEG.close()
	ATER.close()
	AQUA.close()
	AQUI.close()
	ASEX.close()
	#Reabre os arquivos como leitura e escrita
	ASEG = open('Data/Lessons/Aulas_seg.txt','r+')
	ATER = open('Data/Lessons/Aulas_ter.txt','r+')
	AQUA = open('Data/Lessons/Aulas_qua.txt','r+')
	AQUI = open('Data/Lessons/Aulas_qui.txt','r+')
	ASEX = open('Data/Lessons/Aulas_sex.txt','r+')
	#Pega o input do usuário e salva as alterações 
	sg.popup("parece que você não tem nenhuma aula configurada ;-;")
	ASEG.write(sg.PopupGetText('Quais aulas você tem na segunda?'))
	ATER.write(sg.PopupGetText('Quais aulas você tem na terça?'))
	AQUA.write(sg.PopupGetText('Quais aulas você tem na quarta?'))
	AQUI.write(sg.PopupGetText('Quais aulas você tem na quinta?'))
	ASEX.write(sg.PopupGetText('Quais aulas você tem na sexta?'))
	sg.popup('configuração finalizada!')
	#Fecha os arquivos
	ASEG.close()
	ATER.close()
	AQUA.close()
	AQUI.close()
	ASEX.close()

def Redefinir():
	#Define o tema
	sg.theme('DarkGrey13')
	#Remove os arquivos
	os.remove('./Data/Lessons/Aulas_seg.txt')
	os.remove('./Data/Lessons/Aulas_ter.txt')
	os.remove('./Data/Lessons/Aulas_qua.txt')
	os.remove('./Data/Lessons/Aulas_qui.txt')
	os.remove('./Data/Lessons/Aulas_sex.txt')
	#Cria os arquivos
	ASEG = open('Data/Lessons/Aulas_seg.txt','w')
	ATER = open('Data/Lessons/Aulas_ter.txt','w')
	AQUA = open('Data/Lessons/Aulas_qua.txt','w')
	AQUI = open('Data/Lessons/Aulas_qui.txt','w')
	ASEX = open('Data/Lessons/Aulas_sex.txt','w')
	#Fecha os arquivos criados
	ASEG.close()
	ATER.close()
	AQUA.close()
	AQUI.close()
	ASEX.close()
	#Reabre os arquivos como leitura e escrita
	ASEG = open('Data/Lessons/Aulas_seg.txt','r+')
	ATER = open('Data/Lessons/Aulas_ter.txt','r+')
	AQUA = open('Data/Lessons/Aulas_qua.txt','r+')
	AQUI = open('Data/Lessons/Aulas_qui.txt','r+')
	ASEX = open('Data/Lessons/Aulas_sex.txt','r+')
	#Pega as informações das aulas do úsuario e escreve as alterações nos arquivos
	ASEG.write(sg.PopupGetText('Quais aulas você tem na segunda?'))
	ATER.write(sg.PopupGetText('Quais aulas você tem na terça?'))
	AQUA.write(sg.PopupGetText('Quais aulas você tem na quarta?'))
	AQUI.write(sg.PopupGetText('Quais aulas você tem na quinta?'))
	ASEX.write(sg.PopupGetText('Quais aulas você tem na sexta?'))
	#Informa ao úsuario que é presciso reiniciar o programa para concluir as configurações
	sg.popup('configuração finalizada, reinicie o programa para aplicar as novas configurações.')
	#Fecha os arquivos novamente 
	ASEG.close()
	ATER.close()
	AQUA.close()
	AQUI.close()
	ASEX.close()

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
		[sg.Text('Redefinir as aulas:'), sg.Button('Redefinir')],
		[sg.Text('Se você ver algum bug, você pode reportar ele em:')],
		[sg.Text('https://github.com/Felipe2102/Assistente-Escolar/issues/new')],
		[sg.Button('Voltar')]
	]
	return sg.Window('Ajuda', layout, element_justification='c', finalize=True)
#Tenta acessar os arquivos, se os arquivos não existirem ele abre a janela de configuração
try:
	ASEG = open('Data/Lessons/Aulas_seg.txt','r').read()
	ATER = open('Data/Lessons/Aulas_ter.txt','r').read()
	AQUA = open('Data/Lessons/Aulas_qua.txt','r').read()
	AQUI = open('Data/Lessons/Aulas_qui.txt','r').read()
	ASEX = open('Data/Lessons/Aulas_sex.txt','r').read()
except FileNotFoundError:
	setup()
#Verifica novamente os arquivos para caso o usuário tenha configurado no comando anterior 
#ele tenha como usar o programa sem precisar reiniciar o programa
try:
	ASEG = open('Data/Lessons/Aulas_seg.txt','r').read()
	ATER = open('Data/Lessons/Aulas_ter.txt','r').read()
	AQUA = open('Data/Lessons/Aulas_qua.txt','r').read()
	AQUI = open('Data/Lessons/Aulas_qui.txt','r').read()
	ASEX = open('Data/Lessons/Aulas_sex.txt','r').read()
except FileNotFoundError:
	setup()

index, ajuda = home(), None

if __name__ == "__main__":
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
		if window == ajuda and event == 'Redefinir':
			ajuda.hide()
			Redefinir()
			break
		#Verifica o Input do Usuário
		if window == index and event == 'Aulas':
			if Dia == 0:
				sg.popup(ASEG)
			elif Dia == 1:
				sg.popup(ATER)
			elif Dia == 2:
				sg.popup(AQUA)
			elif Dia == 3:
				sg.popup(AQUI)
			elif Dia == 4 :
				sg.popup(ASEX)
			elif Dia == 5 or Dia == 6:
				sg.popup('Hoje você não tem aulas!')
			else:
				sg.popup('Erro: Não foi possivel mostrar as aulas')