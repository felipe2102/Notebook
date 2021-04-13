# Bibliotecas
import os
import DataBase as db
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import *

# Faz o login
def login():
	pass

# Cria um novo usuario 
def criarUsuario():
	pass

# Recebe o input das aulas do usuário e armazena no banco de dados
def config_seg():
	main.aulas.hide()
	ApagarDados()
	CriarTabelas()
	main.conf_seg.show()

def config_ter():
	DiaAula = "Segunda"
	PrimeiraAula = main.conf_seg.lineEdit_1aula.text()
	SegundaAula = main.conf_seg.lineEdit_2aula.text()
	TerceiraAula = main.conf_seg.lineEdit_3aula.text()
	QuartaAula = main.conf_seg.lineEdit_4aula.text()
	QuintaAula = main.conf_seg.lineEdit_5aula.text()
	SextaAula = main.conf_seg.lineEdit_6aula.text()
	try:
		c = main.vcon.cursor()
		c.execute("INSERT INTO tb_aulas (T_MATERIA,T_DIA,N_HORARIO)VALUES('"+PrimeiraAula+"','"+DiaAula+"','7:00')")
		c.execute("INSERT INTO tb_aulas (T_MATERIA,T_DIA,N_HORARIO)VALUES('"+SegundaAula+"','"+DiaAula+"','7:50')")
		c.execute("INSERT INTO tb_aulas (T_MATERIA,T_DIA,N_HORARIO)VALUES('"+TerceiraAula+"','"+DiaAula+"','8:40')")
		c.execute("INSERT INTO tb_aulas (T_MATERIA,T_DIA,N_HORARIO)VALUES('"+QuartaAula+"','"+DiaAula+"','9:50')")
		c.execute("INSERT INTO tb_aulas (T_MATERIA,T_DIA,N_HORARIO)VALUES('"+QuintaAula+"','"+DiaAula+"','10:40')")
		c.execute("INSERT INTO tb_aulas (T_MATERIA,T_DIA,N_HORARIO)VALUES('"+SextaAula+"','"+DiaAula+"','11:30')")
		main.vcon.commit()
	except Error as ex:
		print(ex)
	main.conf_seg.hide()
	main.conf_ter.show()

def config_qua():
	DiaAula = "Terça"
	PrimeiraAula = main.conf_ter.lineEdit_1aula.text()
	SegundaAula = main.conf_ter.lineEdit_2aula.text()
	TerceiraAula = main.conf_ter.lineEdit_3aula.text()
	QuartaAula = main.conf_ter.lineEdit_4aula.text()
	QuintaAula = main.conf_ter.lineEdit_5aula.text()
	SextaAula = main.conf_ter.lineEdit_6aula.text()
	try:
		c = main.vcon.cursor()
		c.execute("INSERT INTO tb_aulas (T_MATERIA,T_DIA,N_HORARIO)VALUES('"+PrimeiraAula+"','"+DiaAula+"','7:00')")
		c.execute("INSERT INTO tb_aulas (T_MATERIA,T_DIA,N_HORARIO)VALUES('"+SegundaAula+"','"+DiaAula+"','7:50')")
		c.execute("INSERT INTO tb_aulas (T_MATERIA,T_DIA,N_HORARIO)VALUES('"+TerceiraAula+"','"+DiaAula+"','8:40')")
		c.execute("INSERT INTO tb_aulas (T_MATERIA,T_DIA,N_HORARIO)VALUES('"+QuartaAula+"','"+DiaAula+"','9:50')")
		c.execute("INSERT INTO tb_aulas (T_MATERIA,T_DIA,N_HORARIO)VALUES('"+QuintaAula+"','"+DiaAula+"','10:40')")
		c.execute("INSERT INTO tb_aulas (T_MATERIA,T_DIA,N_HORARIO)VALUES('"+SextaAula+"','"+DiaAula+"','11:30')")
		main.vcon.commit()
	except Error as ex:
		print(ex)
	main.conf_ter.hide()
	main.conf_qua.show()

def config_qui():
	DiaAula = "Quarta"
	PrimeiraAula = main.conf_qua.lineEdit_1aula.text()
	SegundaAula = main.conf_qua.lineEdit_2aula.text()
	TerceiraAula = main.conf_qua.lineEdit_3aula.text()
	QuartaAula = main.conf_qua.lineEdit_4aula.text()
	QuintaAula = main.conf_qua.lineEdit_5aula.text()
	SextaAula = main.conf_qua.lineEdit_6aula.text()
	try:
		c = main.vcon.cursor()
		c.execute("INSERT INTO tb_aulas (T_MATERIA,T_DIA,N_HORARIO)VALUES('"+PrimeiraAula+"','"+DiaAula+"','7:00')")
		c.execute("INSERT INTO tb_aulas (T_MATERIA,T_DIA,N_HORARIO)VALUES('"+SegundaAula+"','"+DiaAula+"','7:50')")
		c.execute("INSERT INTO tb_aulas (T_MATERIA,T_DIA,N_HORARIO)VALUES('"+TerceiraAula+"','"+DiaAula+"','8:40')")
		c.execute("INSERT INTO tb_aulas (T_MATERIA,T_DIA,N_HORARIO)VALUES('"+QuartaAula+"','"+DiaAula+"','9:50')")
		c.execute("INSERT INTO tb_aulas (T_MATERIA,T_DIA,N_HORARIO)VALUES('"+QuintaAula+"','"+DiaAula+"','10:40')")
		c.execute("INSERT INTO tb_aulas (T_MATERIA,T_DIA,N_HORARIO)VALUES('"+SextaAula+"','"+DiaAula+"','11:30')")
		main.vcon.commit()
	except Error as ex:
		print(ex)
	main.conf_qua.hide()
	main.conf_qui.show()

def config_sex():
	DiaAula = "Quinta"
	PrimeiraAula = main.conf_qui.lineEdit_1aula.text()
	SegundaAula = main.conf_qui.lineEdit_2aula.text()
	TerceiraAula = main.conf_qui.lineEdit_3aula.text()
	QuartaAula = main.conf_qui.lineEdit_4aula.text()
	QuintaAula = main.conf_qui.lineEdit_5aula.text()
	SextaAula = main.conf_qui.lineEdit_6aula.text()
	try:
		c = main.vcon.cursor()
		c.execute("INSERT INTO tb_aulas (T_MATERIA,T_DIA,N_HORARIO)VALUES('"+PrimeiraAula+"','"+DiaAula+"','7:00')")
		c.execute("INSERT INTO tb_aulas (T_MATERIA,T_DIA,N_HORARIO)VALUES('"+SegundaAula+"','"+DiaAula+"','7:50')")
		c.execute("INSERT INTO tb_aulas (T_MATERIA,T_DIA,N_HORARIO)VALUES('"+TerceiraAula+"','"+DiaAula+"','8:40')")
		c.execute("INSERT INTO tb_aulas (T_MATERIA,T_DIA,N_HORARIO)VALUES('"+QuartaAula+"','"+DiaAula+"','9:50')")
		c.execute("INSERT INTO tb_aulas (T_MATERIA,T_DIA,N_HORARIO)VALUES('"+QuintaAula+"','"+DiaAula+"','10:40')")
		c.execute("INSERT INTO tb_aulas (T_MATERIA,T_DIA,N_HORARIO)VALUES('"+SextaAula+"','"+DiaAula+"','11:30')")
		main.vcon.commit()
	except Error as ex:
		print(ex)
	main.conf_qui.hide()
	main.conf_sex.show()

# Finaliza a configuração
def config_ends():
	DiaAula = "Sexta"
	PrimeiraAula = main.conf_sex.lineEdit_1aula.text()
	SegundaAula = main.conf_sex.lineEdit_2aula.text()
	TerceiraAula = main.conf_sex.lineEdit_3aula.text()
	QuartaAula = main.conf_sex.lineEdit_4aula.text()
	QuintaAula = main.conf_sex.lineEdit_5aula.text()
	SextaAula = main.conf_sex.lineEdit_6aula.text()
	try:
		c = main.vcon.cursor()
		c.execute("INSERT INTO tb_aulas (T_MATERIA,T_DIA,N_HORARIO)VALUES('"+PrimeiraAula+"','"+DiaAula+"','7:00')")
		c.execute("INSERT INTO tb_aulas (T_MATERIA,T_DIA,N_HORARIO)VALUES('"+SegundaAula+"','"+DiaAula+"','7:50')")
		c.execute("INSERT INTO tb_aulas (T_MATERIA,T_DIA,N_HORARIO)VALUES('"+TerceiraAula+"','"+DiaAula+"','8:40')")
		c.execute("INSERT INTO tb_aulas (T_MATERIA,T_DIA,N_HORARIO)VALUES('"+QuartaAula+"','"+DiaAula+"','9:50')")
		c.execute("INSERT INTO tb_aulas (T_MATERIA,T_DIA,N_HORARIO)VALUES('"+QuintaAula+"','"+DiaAula+"','10:40')")
		c.execute("INSERT INTO tb_aulas (T_MATERIA,T_DIA,N_HORARIO)VALUES('"+SextaAula+"','"+DiaAula+"','11:30')")
		main.vcon.commit()
	except Error as ex:
		print(ex)
	QMessageBox.about(main.conf_sex,'ALERTA', "CONFIGURAÇÃO FINALIZADA")
	voltar()

# Recebe os dados de compromissos do banco de dados
def agendaSQLite():
	c = vcon.cursor()
	c.execute("SELECT * FROM tb_compromissos LIMIT 20")
	data = c.fetchall()
	agenda.tableWidget.setColumnWidth(0,200)
	agenda.tableWidget.setColumnWidth(1,400)
	agenda.tableWidget.setColumnWidth(2,90)

	for row in data:
		inx = data.index(row)
		agenda.tableWidget.insertRow(inx)
		# add more if there is more columns in the database.
		agenda.tableWidget.setItem(inx, 0, QTableWidgetItem(row[0]))
		agenda.tableWidget.setItem(inx, 1, QTableWidgetItem(row[1]))
		agenda.tableWidget.setItem(inx, 2, QTableWidgetItem(row[2]))

# Deleta um compromisso do banco de dados
def deletarCompromisso():
	agenda.treeWidget.clear()
	agendaSQLite()

# Adiciona um compromisso no banco de dados
def adicionarCompromisso():
	pass

# Mostra a janela para criar um novo compromisso
def MostraAdicionarCompromisso():
	main.agenda.hide()
	main.novo_evento.show()

# Mostra a janela para editar um compromisso
def MostraEditarCompromisso():
	main.agenda.hide()
	main.novo_evento.show()

# Mostra a janela para editar um compromisso
def MostraDeletarCompromisso():
	main.agenda.hide()
	main.deletar_evento.show()
# Mostra a janela de login
def mostra_login():
	pass

# Mostra a janela de registro de novos usuarios
def mostra_registroUsuario():
	pass

# Mostra a janela de aulas
def mostra_aulas():
	vhome.hide()
	main.aulas.show()

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
	novo_evento.hide()
	deletar_evento.hide()
	home.show()

# Fecha o programa
def sair():
	home.close()


# Salva a aplicação do PyQt5 em uma variavel
app = QtWidgets.QApplication([])

# Adiciona o valor da função "ConexaoBanco()" dentro da variável vcon
vcon = db.ConexaoBanco()

# Carrega as janelas
home = uic.loadUi("_pages/index.ui")
agenda = uic.loadUi("_pages/agenda.ui")
configuraçao = uic.loadUi("_pages/configuração.ui")
aulas = uic.loadUi("_pages/aulas.ui")
novo_evento = uic.loadUi("_pages/novo_compromisso.ui")
deletar_evento = uic.loadUi("_pages/deletar_compromisso.ui")

# Carrega as janelas de configuração
conf_seg = uic.loadUi("_pages/aulas_segunda.ui")
conf_ter = uic.loadUi("_pages/aulas_terça.ui")
conf_qua = uic.loadUi("_pages/aulas_quarta.ui")
conf_qui = uic.loadUi("_pages/aulas_quinta.ui")
conf_sex = uic.loadUi("_pages/aulas_sexta.ui")

# Chama uma função para o botão clicado
home.Button_aulas.clicked.connect(mostra_aulas)
home.Button_agenda.clicked.connect(mostra_agenda)
home.Button_config.clicked.connect(mostra_config)
agenda.Button_adicionar.clicked.connect(MostraAdicionarCompromisso)
agenda.Button_editar.clicked.connect(MostraEditarCompromisso)
agenda.Button_deletar.clicked.connect(MostraDeletarCompromisso)

# Volta para a página inicial
agenda.Button_voltar.clicked.connect(voltar)
configuraçao.Button_voltar.clicked.connect(voltar)
aulas.Button_voltar.clicked.connect(voltar)
novo_evento.Button_voltar.clicked.connect(voltar)
deletar_evento.Button_voltar.clicked.connect(voltar)

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

# Sai do programa
home.Button_sair.clicked.connect(sair)

# Mostra a janela principal
home.show()

# Retorna todas os dados presentes no banco de dados
agendaSQLite()

# Executa o programa
app.exec()