from random import choice, randint

minusculas = [chr(i) for i in range(ord('a'), ord('z')+1)] 
maiusculas = [chr(i) for i in range(ord('A'), ord('Z')+1)]
numeros = [str(i) for i in range(0,10)]
simbolos = ["!", "@", "#", "$", "&", "*"]
escolhas = []
senha = ""

quantidade = int(input("Quantos digitos deseja na sua senha?\n-> "))
quer_simbolo = input("Deseja simbolos? [s / n]\n-> ")

if quer_simbolo.lower() == "s":
    escolhas = [minusculas,maiusculas,simbolos,numeros]
else:
    escolhas = [minusculas,maiusculas,numeros]

for i in range(quantidade):
    lista = choice(escolhas)
    digito = choice(lista)
    senha += digito

print(f"Sua nova senha é: {senha}")