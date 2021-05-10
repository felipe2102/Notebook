#Bibliotecas
import sqlite3
import PySimpleGUI as sg
import os
import os.path
from PyQt5 import uic, QtWidgets
from sqlite3 import Error

#Cria uma conexão com o banco de dados sqlite3
def conexaoBanco():
    caminho="Database.db"
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as er:
        print(er)
    return con
