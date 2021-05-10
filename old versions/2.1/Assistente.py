import datetime
from time import sleep

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