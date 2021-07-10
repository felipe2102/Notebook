# Bibliotecas
import sqlite3
from sqlite3 import Error

# Cria uma conexão com o banco de dados
def ConexaoBanco():
	Con = None
	try:
		Con = sqlite3.connect("database.db")
	except Error as ex:
		print("Ops! Um erro ocorreu!")
		print("Código de erro: ", ex)
	return Con

# Armazena o retorno das função na variável
vcon = ConexaoBanco()

# Checa se o usuário já entrou no programa
def CheckEnteredUser():
	c = vcon.cursor()
	CriarTabelas()
	try:
		c.execute("SELECT * FROM tb_dados")
		SearchData = c.fetchall()
		if SearchData == [(1,)]:
			entrou = True
		else:
			entrou = False
		return entrou
	except Error as ex:
		print("Ops! Um erro ocorreu!")
		print("Código de erro: ", ex)

# valida o login no banco de dados
def login(nome, senha):
	c = vcon.cursor()
	try:
		c.execute("SELECT * FROM tb_usuarios WHERE T_NOME = '"+nome+"' AND T_SENHA = '"+senha+"'")
		dados = c.fetchall()
		if dados == [(''+nome+'', ''+senha+'')]:
			return True
		else:
			return False
	except Error as ex:
		print("Ops! Um erro ocorreu!")
		print("Código de erro: ", ex)

# Cria um novo usuario no banco de dados
def criarUsuario(usuario, senha):
	c = vcon.cursor()
	try:
		c.execute("INSERT INTO tb_usuarios (T_NOME,T_SENHA) VALUES('"+usuario+"','"+senha+"')")
		vcon.commit()
	except Error as ex:
		print("Ops! Um erro ocorreu!")
		print("Código de erro: ", ex)

def InsereAulas(Aula, Dia, Hora):
	try:
		c = vcon.cursor()
		c.execute("INSERT INTO tb_aulas (T_MATERIA,T_DIA,N_HORARIO) VALUES('"+Aula+"','"+Dia+"','"+Hora+"')")
		vcon.commit()
	except Error as ex:
		print("Ops! Um erro ocorreu!")
		print("Código de erro: ", ex)

# Adiciona um novo compromisso no banco de dados
def InsereCompromisso(titulo, descrição, tipo):
	try:
		c = vcon.cursor()
		c.execute("INSERT INTO tb_compromissos (T_TITULO,T_DESCRIÇÃO,T_TIPO) VALUES('"+titulo+"','"+descrição+"','"+tipo+"')")
		vcon.commit()
	except Error as ex:
		print("Ops! Um erro ocorreu!")
		print("Código de erro: ", ex)

# Atualiza um compromisso do banco de dados
def editarCompromisso(tituloA, TipoA, TituloN, TipoN, Desc):
	try:
		c = vcon.cursor()
		c.execute("UPDATE tb_compromissos SET T_TITULO = '"+TituloN+"',T_DESCRIÇÃO = '"+Desc+"',T_TIPO = '"+TipoN+"' WHERE T_TITULO = '"+tituloA+"' AND T_TIPO = '"+TipoA+"'")
		vcon.commit()
	except Error as ex:
		print("Ops! Um erro ocorreu!")
		print("Código de erro: ", ex)

# Apaga um compromisso do banco de dados
def deletarcompromisso(titulo, tipo):
	try:
		c = vcon.cursor()
		c.execute("DELETE FROM tb_compromissos WHERE T_TITULO = '"+titulo+"' AND T_TIPO = '"+tipo+"'")
		vcon.commit()
	except Error as ex:
		print("Ops! Um erro ocorreu!")
		print("Código de erro: ", ex)

# Apaga todos os dados do banco de dados
def ApagarDados():
	c = vcon.cursor()
	try:
		c.execute("DELETE FROM tb_aulas")
	except Error as ex:
		print("Ops! Um erro ocorreu!")
		print("Código de erro: ", ex)

# Busca os dados de compromissos especificos no banco de dados
def Searcher(tipo):
	try:
		c = vcon.cursor()
		c.execute("SELECT * FROM tb_compromissos WHERE T_TIPO='"+tipo+"'")
		dados = c.fetchall()
		return dados
	except Error as ex:
		print("Ops! Um erro ocorreu!")
		print("Código de erro: ", ex)

# Busca os dadso das aulas no banco de dados
def BuscaAulas(Dia):
	c = vcon.cursor()
	try:
		c.execute('SELECT * FROM tb_aulas WHERE T_DIA="'+Dia+'"')
		dados = c.fetchall()
		return dados
	except Error as ex:
		print("Ops! Um erro ocorreu!")
		print("Código de erro: ", ex)

# Busca o dados dos compromissos no banco de dados
def BuscaComp():
	c = vcon.cursor()
	try:
		c.execute("SELECT * FROM tb_compromissos LIMIT 20")
		dados = c.fetchall()
		return dados
	except Error as ex:
		print("Ops! Um erro ocorreu!")
		print("Código de erro: ", ex)

# Altera o valor da coluna "JÁ_USOU" para 1
def Usou():
	c = vcon.cursor()
	try:
		c.execute("DELETE FROM tb_dados")
		c.execute("INSERT INTO tb_dados (T_JA_USOU) VALUES(1)")
		vcon.commit()
	except Error as ex:
		print("Ops! Um erro ocorreu!")
		print("Código de erro: ", ex)

# Pega os dados do site no banco de dados
def Site(OP, URL):
	c = vcon.cursor()
	if OP == "read":
		try:
			c.execute("SELECT * FROM tb_site")
			dados = c.fetchall()
			return dados
		except Error as ex:
			print("Ops! Um erro ocorreu!")
			print("Código de erro: ", ex)
	elif OP == "write":
		try:
			c.execute("DELETE FROM tb_site")
			c.execute("INSERT INTO tb_site (T_SITE) VALUES('"+URL+"')")
			vcon.commit()
		except Error as ex:
			print("Ops! Um erro ocorreu!")
			print("Código de erro: ", ex)
	else:
		print("Por favor, insira um tipo válido.")

def CriarTabelas():
	c = vcon.cursor()
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
				T_SENHA VARCHAR(128)
			);""")
		c.execute("""CREATE TABLE IF NOT EXISTS tb_dados(
				T_JA_USOU BOOLEAN
			);""")
		c.execute("""CREATE TABLE IF NOT EXISTS tb_site(
				T_SITE VARCHAR(512)
			);""")
		Site("write", "https://classroom.google.com")
	except Error as ex:
		print("Ops! Um erro ocorreu!")
		print("Código de erro: ", ex)