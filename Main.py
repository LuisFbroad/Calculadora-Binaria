import os
##from Calculadora.Operaçoes_Binarias import 
from Calculadora.Operaçoes_Simples import main_S
def limpar_terminal():
    os.system('cls')

def Qcalculadora():
    while True:
        limpar_terminal()
        opcao = int(input("Qual Calculadora você quer acessar ?\n Simples --- 1\n Binaria --- 2\n\n"))
        if opcao == 1:
            main_S()

Qcalculadora()