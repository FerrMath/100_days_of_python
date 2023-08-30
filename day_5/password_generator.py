from random import choice, randint

alfabeto = [
    chr(i) for i in range(ord('a'), ord('z')+1)
    ] + [
    chr(i) for i in range(ord('A'), ord('Z')+1)
    ]
simbolos = ["!", "@", "#", "$", "%", "&", "*"]
numeros = [str(i) for i in range(0,10)]
escolhas = []
senha = ""

quantidade = int(input("Quantos digitos deseja na sua senha?\n-> "))
quer_simbolo = input("Deseja simbolos? [s / n]\n-> ")

if quer_simbolo.lower() == "s":
    escolhas = [alfabeto,simbolos,numeros]
else:
    escolhas = [alfabeto,numeros]

for i in range(quantidade):
    lista = choice(escolhas)
    digito = choice(lista)
    senha += digito

print(f"Sua nova senha é: {senha}")