# Bibliotecas
import sqlite3
from sqlite3 import Error

# Funções

# Cria uma conexão com o banco de dados
def ConexaoBanco():
	Con = None
	try:
		Con = sqlite3.connect("database.db")
	except Error as ex:
		print(ex)
	return Con

# Faz o login
def login():
	pass

# Cria um novo usuario 
def criarUsuario():
	pass

# Recebe os dados de compromissos do banco de dados
#def agendaSQLite():
#	c = main.vcon.cursor()
#	for row in c.execute("SELECT * FROM tb_compromissos LIMIT 20"):
#		Srow = str(row)
#		main.agenda.listWidget.addItems(row)

# Atualiza um compromisso do banco de dados
def editarCompromisso():
	pass

# Apaga todos os dados do banco de dados
def ApagarDados():
	c = main.vcon.cursor()
	try:
		c.execute("DELETE tb_aulas")
	except Error as ex:
		print(ex)

def CriarTabelas():
	c = main.vcon.cursor()
	try:
		c.execute("""CREATE TABLE IF NOT EXISTS tb_aulas(
				T_MATERIA VARCHAR(64),
				T_DIA VARCHAR(20),
				N_HORARIO INTEGER
			);""")
		c.execute("""CREATE TABLE IF NOT EXISTS tb_compromissos(
				T_TITULO VARCHAR(32),
				T_DESCRIÇÃO VARCHAR(128),
				T_TIPO VARCHAR(16)
			);""")
		c.execute("""CREATE TABLE IF NOT EXISTS tb_usuarios(
				T_NOME VARCHAR(512),
				T_USUARIO VARCHAR(128),
				T_SENHA INTEGER
			);""")
	except Error as ex:
		print(ex)