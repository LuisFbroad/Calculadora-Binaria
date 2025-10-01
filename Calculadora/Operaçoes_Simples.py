import os
from time import sleep

def limpar_terminal():
    os.system('cls')

def adiçao():
    limpar_terminal()
    num1 = float(input("Digite um o primeiro numero..: "))
    num2 = float(input(f"Digite quanto você quer adicionar a {num1}..: "))
    dif = num1 + num2
    print (f"{num1} + {num2} = {dif}")

def subtraçao():
    limpar_terminal()
    num1 = float(input("Digite um o primeiro numero..: "))
    num2 = float(input(f"Digite quanto você quer tirar de {num1}..: "))
    dif = num1 - num2
    print (f"{num1} - {num2} = {dif}")

def multiplicaçao():
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