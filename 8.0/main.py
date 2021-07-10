# Bibliotecas
import os
import DataBase as db
import webbrowser as wb
from datetime import datetime
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import *

# Armazena o dia da semana atual em uma variavel
Dias_semana = ['Segunda', 'terça', 'Quarta', 'Quinta', 'Sexta', 'sábado', 'Domingo']
Dia_da_semana=Dias_semana[datetime.now().weekday()]

#dia = datetime.now().date()

# Faz o login
def login():
	Usuário = Login.lineEdit.text()
	Senha = Login.lineEdit_2.text()
	IsLogged = db.login(Usuário, Senha)
	if IsLogged == True and db.CheckEnteredUser() == False:
		Login.hide()
		home.hide()
		config_inicial()
	elif IsLogged == True:
		Login.hide()
		home.show()
		agendaSQLite()
		BuscaAulas()
	else:
		QMessageBox.about(Login,'ALERTA',"USUÁRIO OU SENHA INCORRETOS")

# Cria um novo usuário
def RegUsuário():
	Usuário = registra.lineEdit.text()
	Senha = registra.lineEdit_2.text()
	Senha2 = registra.lineEdit_3.text()
	if Senha == Senha2:
		db.criarUsuario(Usuário, Senha)
		QMessageBox.about(registra,'ALERTA',"USUÁRIO ADICIONADO!")
		registra.hide()
		Login.show()
	else:
		QMessageBox.about(registra,'ALERTA',"AS SENHAS NÃO CONDIZEM")

# Mostra a tela de login
def MostraLogin():
	registra.hide()
	Login.show()

# Cria um novo usuario 
def MostraCriarUsuario():
	Login.hide()
	registra.show()

# Faz a configuração inicial
def config_inicial():
	home.hide()
	db.Usou()
	config_seg()

# Recebe o input das aulas do usuário e armazena no banco de dados
def config_seg():
	aulas.hide()
	configuraçao.hide()
	conf_seg.show()
	home.hide()

def config_ter():
	DiaAula = "Segunda"
	PrimeiraAula = conf_seg.lineEdit_1aula.text()
	SegundaAula = conf_seg.lineEdit_2aula.text()
	TerceiraAula = conf_seg.lineEdit_3aula.text()
	QuartaAula = conf_seg.lineEdit_4aula.text()
	QuintaAula = conf_seg.lineEdit_5aula.text()
	SextaAula = conf_seg.lineEdit_6aula.text()
	db.InsereAulas(PrimeiraAula, DiaAula, "7:00")
	db.InsereAulas(SegundaAula, DiaAula, '7:50')
	db.InsereAulas(TerceiraAula, DiaAula, '8:40')
	db.InsereAulas(QuartaAula, DiaAula, '9:50')
	db.InsereAulas(QuintaAula, DiaAula, '10:40')
	db.InsereAulas(SextaAula, DiaAula, '11:30')
	conf_seg.hide()
	conf_ter.show()

def config_qua():
	DiaAula = "Terça"
	PrimeiraAula = conf_ter.lineEdit_1aula.text()
	SegundaAula = conf_ter.lineEdit_2aula.text()
	TerceiraAula = conf_ter.lineEdit_3aula.text()
	QuartaAula = conf_ter.lineEdit_4aula.text()
	QuintaAula = conf_ter.lineEdit_5aula.text()
	SextaAula = conf_ter.lineEdit_6aula.text()
	db.InsereAulas(PrimeiraAula, DiaAula, '7:00')
	db.InsereAulas(SegundaAula, DiaAula, '7:50')
	db.InsereAulas(TerceiraAula, DiaAula, '8:40')
	db.InsereAulas(QuartaAula, DiaAula, '9:50')
	db.InsereAulas(QuintaAula, DiaAula, '10:40')
	db.InsereAulas(SextaAula, DiaAula, '11:30')
	conf_ter.hide()
	conf_qua.show()

def config_qui():
	DiaAula = "Quarta"
	PrimeiraAula = conf_qua.lineEdit_1aula.text()
	SegundaAula = conf_qua.lineEdit_2aula.text()
	TerceiraAula = conf_qua.lineEdit_3aula.text()
	QuartaAula = conf_qua.lineEdit_4aula.text()
	QuintaAula = conf_qua.lineEdit_5aula.text()
	SextaAula = conf_qua.lineEdit_6aula.text()
	db.InsereAulas(PrimeiraAula, DiaAula, '7:00')
	db.InsereAulas(SegundaAula, DiaAula, '7:50')
	db.InsereAulas(TerceiraAula, DiaAula, '8:40')
	db.InsereAulas(QuartaAula, DiaAula, '9:50')
	db.InsereAulas(QuintaAula, DiaAula, '10:40')
	db.InsereAulas(SextaAula, DiaAula, '11:30')
	conf_qua.hide()
	conf_qui.show()

def config_sex():
	DiaAula = "Quinta"
	PrimeiraAula = conf_qui.lineEdit_1aula.text()
	SegundaAula = conf_qui.lineEdit_2aula.text()
	TerceiraAula = conf_qui.lineEdit_3aula.text()
	QuartaAula = conf_qui.lineEdit_4aula.text()
	QuintaAula = conf_qui.lineEdit_5aula.text()
	SextaAula = conf_qui.lineEdit_6aula.text()
	db.InsereAulas(PrimeiraAula, DiaAula, '7:00')
	db.InsereAulas(SegundaAula, DiaAula, '7:50')
	db.InsereAulas(TerceiraAula, DiaAula, '8:40')
	db.InsereAulas(QuartaAula, DiaAula, '9:50')
	db.InsereAulas(QuintaAula, DiaAula, '10:40')
	db.InsereAulas(SextaAula, DiaAula, '11:30')
	conf_qui.hide()
	conf_sex.show()

# Finaliza a configuração
def config_ends():
	DiaAula = "Sexta"
	PrimeiraAula = conf_sex.lineEdit_1aula.text()
	SegundaAula = conf_sex.lineEdit_2aula.text()
	TerceiraAula = conf_sex.lineEdit_3aula.text()
	QuartaAula = conf_sex.lineEdit_4aula.text()
	QuintaAula = conf_sex.lineEdit_5aula.text()
	SextaAula = conf_sex.lineEdit_6aula.text()
	db.InsereAulas(PrimeiraAula, DiaAula, '7:00')
	db.InsereAulas(SegundaAula, DiaAula, '7:50')
	db.InsereAulas(TerceiraAula, DiaAula, '8:40')
	db.InsereAulas(QuartaAula, DiaAula, '9:50')
	db.InsereAulas(QuintaAula, DiaAula, '10:40')
	db.InsereAulas(SextaAula, DiaAula, '11:30')
	QMessageBox.about(conf_sex,'ALERTA', "CONFIGURAÇÃO FINALIZADA")
	voltar()

# Recebe os dados de compromissos do banco de dados e adiciona no QTableWidget
def agendaSQLite():
	data = db.BuscaComp()
	agenda.tableWidget.setColumnWidth(0,200)
	agenda.tableWidget.setColumnWidth(1,400)
	agenda.tableWidget.setColumnWidth(2,90)
	agenda.tableWidget.setRowCount(0)

	for row in data:
		inx = data.index(row)
		agenda.tableWidget.insertRow(inx)
		agenda.tableWidget.setItem(inx, 0, QTableWidgetItem(row[0]))
		agenda.tableWidget.setItem(inx, 1, QTableWidgetItem(row[1]))
		agenda.tableWidget.setItem(inx, 2, QTableWidgetItem(row[2]))

# Recebe os dados de compromissos do banco de dados e adiciona no QTableWidget
def BuscaAulas():
	data = db.BuscaAulas(Dia_da_semana)
	aulas.tableWidget.setColumnWidth(0,150)
	aulas.tableWidget.setColumnWidth(1,110)
	aulas.tableWidget.setColumnWidth(2,100)
	aulas.tableWidget.setRowCount(0)

	for row in data:
		inx = data.index(row)
		aulas.tableWidget.insertRow(inx)
		aulas.tableWidget.setItem(inx, 0, QTableWidgetItem(row[0]))
		aulas.tableWidget.setItem(inx, 1, QTableWidgetItem(row[1]))
		aulas.tableWidget.setItem(inx, 2, QTableWidgetItem(row[2]))		

# Busca compromissos especificos no banco de dados
def Buscador():
	typeofcomp = buscar_evento.comboBox.currentText()
	data = db.Searcher(typeofcomp)
	agenda.tableWidget.setRowCount(0)

	for row in data:
		inx = data.index(row)
		agenda.tableWidget.insertRow(inx)
		agenda.tableWidget.setItem(inx, 0, QTableWidgetItem(row[0]))
		agenda.tableWidget.setItem(inx, 1, QTableWidgetItem(row[1]))
		agenda.tableWidget.setItem(inx, 2, QTableWidgetItem(row[2]))

	buscar_evento.hide()
	agenda.show()

def abrir_site():
	site_url = db.Site("read", "PLACEHOLDER")
	site_url = str(site_url[0][0])
	wb.open_new_tab(site_url)

def editar_site():
	global site_url
	site_url = configuraçao.lineEdit.text()
	db.Site("write", site_url)

# Deleta um compromisso do banco de dados
def deletarCompromisso():
	title = deletar_evento.lineEdit.text()
	typeofcomp = deletar_evento.comboBox.currentText()
	db.deletarcompromisso(title, typeofcomp)
	agendaSQLite()
	deletar_evento.hide()
	agenda.show()

# Redefini as aulas no banco de dados
def RedefinirAulas():
	db.ApagarDados()
	config_seg()

# Adiciona um compromisso no banco de dados
def adicionarCompromisso():
	title = novo_evento.lineEdit_title.text()
	description = novo_evento.lineEdit_description.text()
	typeofcomp = novo_evento.comboBox.currentText()
	db.InsereCompromisso(title, description, typeofcomp)
	novo_evento.hide()
	agenda.show()

# Edita os compromissos no banco de dados
def editarCompromisso():
	titulo_Antigo = editar_evento.lineEdit_tituloAntigo.text()
	Tipo_Antigo =  editar_evento.comboBox_TipoAntigo.currentText()
	Titulo_Novo = editar_evento.lineEdit_tituloNovo.text()
	Tipo_Novo = editar_evento.comboBox_TipoNovo.currentText()
	Descrição_Nova = editar_evento.lineEdit_descrio.text()
	db.editarCompromisso(titulo_Antigo, Tipo_Antigo, Titulo_Novo, Tipo_Novo, Descrição_Nova)
	agendaSQLite()
	editar_evento.hide()
	agenda.show()

# Mostra a janela para criar um novo compromisso
def MostraAdicionarCompromisso():
	agenda.hide()
	novo_evento.show()

# Mostra a janela para editar um compromisso
def MostraEditarCompromisso():
	agenda.hide()
	editar_evento.show()

# Mostra a janela para editar um compromisso
def MostraDeletarCompromisso():
	agenda.hide()
	deletar_evento.show()

# Mostra a janela de editar compromisso
def MostraBuscarCompromisso():
	agenda.hide()
	buscar_evento.show()

# Mostra a janela de aulas
def mostra_aulas():
	home.hide()
	aulas.show()

# Mostra a agenda
def mostra_agenda():
	home.hide()
	agenda.show()

# Mostra a janela de configurações
def mostra_config():
	home.hide()
	configuraçao.show()

# Abre o editor de eventos
def mostraEditor():
	agenda.hide()
	novo_evento.show()

# Volta para a tela inicial
def voltar():
	aulas.hide()
	agenda.hide()
	configuraçao.hide()
	conf_seg.hide()
	conf_ter.hide()
	conf_qua.hide()
	conf_qui.hide()
	conf_sex.hide()
	home.show()

# Volta para a tela agenda
def voltarAgenda():
	novo_evento.hide()
	editar_evento.hide()
	deletar_evento.hide()
	buscar_evento.hide()
	agenda.show()

# Fecha o programa
def sair():
	home.close()

# Salva a aplicação do PyQt5 na variável "app"
app = QtWidgets.QApplication([])

# Carrega as janelas de login e novo usuário
registra = uic.loadUi("_pages/Registro.ui")
Login = uic.loadUi("_pages/login.ui")

# Carrega as janelas principais do programa
home = uic.loadUi("_pages/index.ui")
agenda = uic.loadUi("_pages/agenda.ui")
configuraçao = uic.loadUi("_pages/configuração.ui")
aulas = uic.loadUi("_pages/aulas.ui")
novo_evento = uic.loadUi("_pages/novo_compromisso.ui")
editar_evento = uic.loadUi("_pages/editar_compromisso.ui")
buscar_evento = uic.loadUi("_pages/deletar_compromisso.ui")
deletar_evento = uic.loadUi("_pages/deletar_compromisso.ui")

# Carrega as janelas de configuração
conf_seg = uic.loadUi("_pages/aulas_segunda.ui")
conf_ter = uic.loadUi("_pages/aulas_terça.ui")
conf_qua = uic.loadUi("_pages/aulas_quarta.ui")
conf_qui = uic.loadUi("_pages/aulas_quinta.ui")
conf_sex = uic.loadUi("_pages/aulas_sexta.ui")

# Mostra a janela de novo usuário
Login.Button_registro.clicked.connect(MostraCriarUsuario)

# Chama a função de login quando o botão é clicado
Login.Button_login.clicked.connect(login)

# Chama a função para criar um novo usuário
registra.Button_criar.clicked.connect(RegUsuário)

# Mostra a janela de login
registra.Button_voltar.clicked.connect(MostraLogin)

# Chama uma função para o botão clicado
home.Button_aulas.clicked.connect(mostra_aulas)
home.Button_agenda.clicked.connect(mostra_agenda)
home.Button_config.clicked.connect(mostra_config)
home.Button_site.clicked.connect(abrir_site)
agenda.Button_adicionar.clicked.connect(MostraAdicionarCompromisso)
agenda.Button_editar.clicked.connect(MostraEditarCompromisso)
agenda.Button_Buscar.clicked.connect(MostraBuscarCompromisso)
agenda.Button_deletar.clicked.connect(MostraDeletarCompromisso)
aulas.Button_reconfigurar.clicked.connect(RedefinirAulas)
configuraçao.Button_redaula.clicked.connect(RedefinirAulas)
configuraçao.Button_salvar_site.clicked.connect(editar_site)

# Volta para a página inicial
agenda.Button_voltar.clicked.connect(voltar)
configuraçao.Button_voltar.clicked.connect(voltar)
aulas.Button_voltar.clicked.connect(voltar)
novo_evento.Button_voltar.clicked.connect(voltarAgenda)
editar_evento.Button_voltar.clicked.connect(voltarAgenda)
deletar_evento.Button_voltar.clicked.connect(voltarAgenda)
buscar_evento.Button_voltar.clicked.connect(voltarAgenda)

# Chama a função para adicionar, remover e deletar compromissos
novo_evento.Button_confirma.clicked.connect(adicionarCompromisso)
editar_evento.Button_confirma.clicked.connect(editarCompromisso)
buscar_evento.Button_confirma.clicked.connect(Buscador)
deletar_evento.Button_confirma.clicked.connect(deletarCompromisso)

# Começa o proscesso de configuração
aulas.Button_reconfigurar.clicked.connect(config_seg)

# Passa para a proxima tela da configuração
conf_seg.Button_continuar.clicked.connect(config_ter)
conf_ter.Button_continuar.clicked.connect(config_qua)
conf_qua.Button_continuar.clicked.connect(config_qui)
conf_qui.Button_continuar.clicked.connect(config_sex)
conf_sex.Button_continuar.clicked.connect(config_ends)

# Cancela o proscesso de configuração
conf_seg.Button_cancelar.clicked.connect(voltar)
conf_ter.Button_cancelar.clicked.connect(voltar)
conf_qua.Button_cancelar.clicked.connect(voltar)
conf_qui.Button_cancelar.clicked.connect(voltar)
conf_sex.Button_cancelar.clicked.connect(voltar)

# Recarrega os compromissos
agenda.Button_reload.clicked.connect(agendaSQLite)

# Sai do programa
home.Button_sair.clicked.connect(sair)

# Cria as tabelas no banco de dados
db.CriarTabelas()

# Mostra a janela de login
Login.show()

# Executa o PyQt5
app.exec()

