#Bibliotecas usadas
import json
import sqlite3
from sqlite3 import Error 
from datetime import datetime

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QListWidget
import os

#Variaveis
seg_aulaum = None
seg_auladois = None
seg_aulatres = None
seg_aulaquatro = None
seg_aulacinco = None
seg_aulaseis = None
ter_aulaum = None
ter_auladois = None
ter_aulatres = None
ter_aulaquatro = None
ter_aulacinco = None
ter_aulaseis = None
qua_aulaum = None
qua_auladois = None
qua_aulatres = None
qua_aulaquatro = None
qua_aulacinco = None
qua_aulaseis = None
qui_aulaum = None
qui_auladois = None
qui_aulatres = None
qui_aulaquatro = None
qui_aulacinco = None
qui_aulaseis = None
sex_aulaum = None
sex_auladois = None
sex_aulatres = None
sex_aulaquatro = None
sex_aulacinco = None
sex_aulaseis = None

def hide_all():
	home.hide()
	lessons.hide()
	compromisses.hide()
	configurations.hide()
	conf_lessons_segunda.hide()
	conf_lessons_terça.hide()
	conf_lessons_quarta.hide()
	conf_lessons_quinta.hide()
	conf_lessons_sexta.hide()
#Mostra a tela de aulas
def aulas():
	lessons.show()
	home.hide()

#Mostra a tela de compromissos
def comp():
	compromisses.show()
	home.hide()
	
#Mostra a tela de configurações
def conf():
	configurations.show()
	hide_all()

def conf_aulas():
	hide_all()
	conf_lessons_segunda.show()

#Volta para a tela inicial do programa
def voltar():
	hide_all()
	home.show()

def conf_seg():
	hide_all()

	global seg_aulaum 
	global seg_auladois
	global seg_aulatres
	global seg_aulaquatro
	global seg_aulacinco
	global seg_aulaseis

	seg_aulaum = conf_lessons_segunda.lineEdit_firstlesson.text()
	seg_auladois = conf_lessons_segunda.lineEdit_secondlesson.text()
	seg_aulatres = conf_lessons_segunda.lineEdit_3lesson.text()
	seg_aulaquatro = conf_lessons_segunda.lineEdit_fourlesson.text()
	seg_aulacinco = conf_lessons_segunda.lineEdit_fivelesson.text()
	seg_aulaseis = conf_lessons_segunda.lineEdit_sixlesson.text()

	conf_ter()

def conf_ter():
	hide_all()
	conf_lessons_terça.show()

	global ter_aulaum 
	global ter_auladois
	global ter_aulatres
	global ter_aulaquatro
	global ter_aulacinco
	global ter_aulaseis

	ter_aulaum = conf_lessons_terça.lineEdit_firstlesson.text()
	ter_auladois = conf_lessons_terça.lineEdit_secondlesson.text()
	ter_aulatres = conf_lessons_terça.lineEdit_3lesson.text()
	ter_aulaquatro = conf_lessons_terça.lineEdit_fourlesson.text()
	ter_aulacinco = conf_lessons_terça.lineEdit_fivelesson.text()
	ter_aulaseis = conf_lessons_terça.lineEdit_sixlesson.text()

def conf_qua():
	hide_all()

	global qua_aulaum 
	global qua_auladois
	global qua_aulatres
	global qua_aulaquatro
	global qua_aulacinco
	global qua_aulaseis

	conf_lessons_quarta.show()
	qua_aulaum = conf_lessons_quarta.lineEdit_firstlesson.text()
	qua_auladois = conf_lessons_quarta.lineEdit_secondlesson.text()
	qua_aulatres = conf_lessons_quarta.lineEdit_3lesson.text()
	qua_aulaquatro = conf_lessons_quarta.lineEdit_fourlesson.text()
	qua_aulacinco = conf_lessons_quarta.lineEdit_fivelesson.text()
	qua_aulaseis = conf_lessons_quarta.lineEdit_sixlesson.text()

def conf_qui():
	hide_all()

	global qui_aulaum 
	global qui_auladois
	global qui_aulatres
	global qui_aulaquatro
	global qui_aulacinco
	global qui_aulaseis

	conf_lessons_quinta.show()
	qui_aulaum = conf_lessons_quinta.lineEdit_firstlesson.text()
	qui_auladois = conf_lessons_quinta.lineEdit_secondlesson.text()
	qui_aulatres = conf_lessons_quinta.lineEdit_3lesson.text()
	qui_aulaquatro = conf_lessons_quinta.lineEdit_fourlesson.text()
	qui_aulacinco = conf_lessons_quinta.lineEdit_fivelesson.text()
	qui_aulaseis = conf_lessons_quinta.lineEdit_sixlesson.text()

def conf_sex():
	hide_all()

	global sex_aulaum 
	global sex_auladois
	global sex_aulatres
	global sex_aulaquatro
	global sex_aulacinco
	global sex_aulaseis

	conf_lessons_sexta.show()
	sex_aulaum = conf_lessons_sexta.lineEdit_firstlesson.text()
	sex_auladois = conf_lessons_sexta.lineEdit_secondlesson.text()
	sex_aulatres = conf_lessons_sexta.lineEdit_3lesson.text()
	sex_aulaquatro = conf_lessons_sexta.lineEdit_fourlesson.text()
	sex_aulacinco = conf_lessons_sexta.lineEdit_fivelesson.text()
	sex_aulaseis = conf_lessons_sexta.lineEdit_sixlesson.text()


def conf_finalize():
	hide_all()
	if Weekday == 0:
		aulaum = seg_aulaum
		auladois = seg_auladois
		aulatres = seg_aulatres
		aulaquatro = seg_aulaquatro
		aulacinco = seg_aulacinco
		aulaseis = seg_aulaseis
	elif Weekday == 1:
		aulaum = ter_aulaum
		auladois = ter_auladois
		aulatres = ter_aulatres
		aulaquatro = ter_aulaquatro
		aulacinco = ter_aulacinco
		aulaseis = ter_aulaseis
	elif Weekday == 2:
		aulaum = qua_aulaum
		auladois = qua_auladois
		aulatres = qua_aulatres
		aulaquatro = qua_aulaquatro
		aulacinco = qua_aulacinco
		aulaseis = qua_aulaseis
	elif Weekday == 3:
		aulaum = qui_aulaum
		auladois = qui_auladois
		aulatres = qui_aulatres
		aulaquatro = qui_aulaquatro
		aulacinco = qui_aulacinco
		aulaseis = qui_aulaseis
	elif Weekday == 4:
		aulaum = sex_aulaum
		auladois = sex_auladois
		aulatres = sex_aulatres
		aulaquatro = sex_aulaquatro
		aulacinco = sex_aulacinco
		aulaseis = sex_aulaseis
	elif Weekday == 5:
		QMessageBox.about(home,'ALERT','Você não tem aulas hoje ;)')
	elif Weekday == 6:
		QMessageBox.about(home,'ALERT','Você não tem aulas hoje ;)')
	else:
		QMessageBox.about(lessons,'ERROR','PANI NO SISTEMA ALGUEM ME DESCONFIGUROU')
	
	lessons.aula1.setText(aulaum)
	lessons.aula2.setText(auladois)
	lessons.aula3.setText(aulatres)
	lessons.aula4.setText(aulaquatro)
	lessons.aula5.setText(aulacinco)
	lessons.aula6.setText(aulaseis)

	if aulaseis == '':
		lessons.aula6.setText('Você não tem sexta aula')
	
	print(aulaum, auladois, aulatres, aulaquatro, aulacinco, aulaseis)

	QMessageBox.about(home,'ALERT','Configuração finalizada!')
	home.show()

#Inseri a informação do dia da semana na variavel "Weekday"
Weekday = datetime.now().weekday()


#Carrega as definições do PyQt5 na variavel "app"
app = QtWidgets.QApplication([])
#carrega as interfaces em suas respectivas variáveis
home = uic.loadUi(".\\_pages\\normal\\index.ui")
lessons = uic.loadUi(".\\_pages\\normal\\Lessons.ui")
compromisses = uic.loadUi(".\\_pages\\normal\\compromisses.ui")
configurations = uic.loadUi(".\\_pages\\normal\\configurations.ui")
conf_lessons_segunda = uic.loadUi(".\\_pages\\configuration\\aulas_segunda.ui")
conf_lessons_terça = uic.loadUi(".\\_pages\\configuration\\aulas_terça.ui")
conf_lessons_quarta = uic.loadUi(".\\_pages\\configuration\\aulas_quarta.ui")
conf_lessons_quinta = uic.loadUi(".\\_pages\\configuration\\aulas_quinta.ui")	
conf_lessons_sexta = uic.loadUi(".\\_pages\\configuration\\aulas_sexta.ui")
#Ativa a função respectiva para iniciar a janela de cada opção
home.Button_aulas.clicked.connect(aulas)
home.Button_comp.clicked.connect(comp)
home.Button_conf.clicked.connect(conf)
home.Button_exit.clicked.connect(exit)

configurations.Button_redaula.clicked.connect(conf_aulas)
lessons.Button_reconf.clicked.connect(conf_aulas)

conf_lessons_segunda.Button_continuar.clicked.connect(conf_seg)
conf_lessons_terça.Button_continuar.clicked.connect(conf_qua) 
conf_lessons_quarta.Button_continuar.clicked.connect(conf_qui) 
conf_lessons_quinta.Button_continuar.clicked.connect(conf_sex) 
conf_lessons_sexta.Button_continuar.clicked.connect(conf_finalize) 

#Volta para a janela "index"
lessons.Button_return.clicked.connect(voltar)
compromisses.Button_return.clicked.connect(voltar)
configurations.Button_return.clicked.connect(voltar)
conf_lessons_segunda.Button_return.clicked.connect(voltar)

#Mostra a janela "index"
home.show()
#Executa a aplicação
app.exec()
