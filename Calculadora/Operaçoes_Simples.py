import os
from time import sleep

def limpar_terminal():
    os.system('cls')

def adicao():
    limpar_terminal()
    num1 = float(input("Digite um o primeiro numero..: "))
    num2 = float(input(f"Digite quanto você quer adicionar a {num1}..: "))
    dif = num1 + num2
    print (f"{num1} + {num2} = {dif}")

def subtracao():
    limpar_terminal()
    num1 = float(input("Digite um o primeiro numero..: "))
    num2 = float(input(f"Digite quanto você quer tirar de {num1}..: "))
    dif = num1 - num2
    print (f"{num1} - {num2} = {dif}")

def multiplicacao():
    limpar_terminal()
    num1 = float(input("Digite um o primeiro numero..: "))
    num2 = float(input(f"Digite quanto você quer multiplicar {num1}..: "))
    dif = num1 * num2
    print (f"{num1} X {num2} = {dif}")

def divisao():
    limpar_terminal()
    num1 = float(input("Digite um o primeiro numero..: "))
    num2 = float(input(f"Digite o quanto você quer dividir de {num1}..: "))
    dif = num1 / num2
    print (f"{num1}/{num2} = {dif}")

def main_S():
    while True:
        sleep(2)
        limpar_terminal()
        try:
            opcao = int(input("Qual operação você deseja realizar ?\n 1 --- Adição\n 2 --- Subtração\n 3 --- Multiplicação\n 4 --- Divisão\n 0 --- Voltar ao menu\n\n"))
        
            if opcao == 1:
                adicao()
            elif opcao == 2:
                subtracao()
            elif opcao == 3:
                multiplicacao()
            elif opcao == 4:
                divisao()
            elif opcao == 0:
                break
        except ValueError as e:
            print(f"Opção invalida {e}")