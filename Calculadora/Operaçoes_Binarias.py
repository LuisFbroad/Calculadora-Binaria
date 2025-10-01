import os

def limpar_terminal():
    os.system('cls')

def info_dec():
    while True:
        limpar_terminal()
        try:
            dnum = int(input("Digite o número decimal para ver a suas formas de\n  Binario\n  Octal\n  Hexadecimal\n"))
            nbin = bin(dnum)[2:]
            noct = oct(dnum)[2:]
            nhex = hex(dnum)[2:]
            print(f"Seu número {dnum}\n Binario = {nbin}\n Octal = {noct}\n Hexadecimal = {nhex}")
        except ValueError:
            print(f"Valor inválido {ValueError}")

def deci2b():
    while True:
        limpar_terminal()
        try:
            dnum = int(input("Digite o número decimal..: "))
            nbin = bin(dnum)[2:]
            print(f"O binario de {dnum} é {nbin}")
        except ValueError:
            print(f"Valor inválido {ValueError}")

def b2dec():
    while True:
        limpar_terminal()
        try:
            nbin = input("Digite o número binario..: ")
            ndec = int(nbin, 2)
            print(f"O decinmal de {nbin} é {ndec}")
        except ValueError:
            print(f"Valor inválido {ValueError}")

def dec2oct():
    while True:
        limpar_terminal()
        try:
            ndec = int(input("Digite seu número em decimal..: "))
            noct = oct(ndec)[2:]
            print(f"O octal de {ndec} é {noct}")
        except ValueError:
            print(f"Valor inválido {ValueError}")

def oct2dec():
    while True:
        limpar_terminal()
        try:
            noct = ("Digite o seu octal..:")
            ndec = int(noct, 8)
            print(f"A forma decimal de {noct} é {ndec}")
        except ValueError:
            print(f"Valor inválido {ValueError}")

def dec2hex():
    while True:
        limpar_terminal()
        try:
            ndec = int(input("Digite seu número em decimal..: "))
            nhex = hex(ndec)[2:]
            print(f"O Hexadecimal de {ndec} é {nhex}")
        except ValueError:
            print(f"Valor inválido {ValueError}")


def hex2dec():
    while True:
        limpar_terminal()
        try:
            nhex = input("Digite seu número em decimal..: ")
            ndec = int(nhex, 16)
            print(f"A forma decimal de {nhex} é {ndec}")
        except ValueError:
            print (f"Valor invalido {ValueError}")

info_dec()