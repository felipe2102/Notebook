from pathlib import Path
import datetime
from time import sleep

fileName = r"C:\Users\Felipe Ribeiro\Documents\Python\Assistente\3.0\Username.txt"
fileObj = Path(fileName)
if fileObj.is_file() == True :
    f = open('Username.txt', 'r')
    print('Bem Vindo,' + str(f.read()))
else :
    Usuário = input('Qual é o seu nome?')

    with open('Username.txt', 'w') as arquivo:
        arquivo.write(str(Usuário))
Dia = datetime.datetime.now().weekday()
Dias = ['Segunda-feira', 'terça', 'Quarta-feira', 'Quinta feira', 'Sexta-feira', 'sábado', 'Domingo']
Dia_Atual=Dias[Dia]
print('O que você quer?')
print('')
Resposta=input()
print('')

if Resposta == 'Aulas' :
    if Dia_Atual == 'Segunda-feira' :
        print('insira as aulas')
    else :
        if Dia_Atual == 'terça' :
            print('insira as aulas')
        else :
            if Dia_Atual == 'Quarta-feira' :
                print('insira as aulas')
            else :
                if Dia_Atual == 'Quinta feira' :
                    print('insira as aulas')
                else :
                    if Dia_Atual == 'Sexta-feira' :
                        print('insira as aulas teste')

print('')
sleep(120)