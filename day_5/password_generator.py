from random import choice, shuffle

minusculas = [chr(i) for i in range(ord('a'), ord('z')+1)] 
maiusculas = [chr(i) for i in range(ord('A'), ord('Z')+1)]
numeros = [str(i) for i in range(0,10)]
simbolos = ["!", "@", "#", "$", "&", "*"]
escolhas = []
senha = ""

total = int(input("Quantos digitos deseja em sua senha?\n"))
qtt_num = int(input("Quantos números deseja?\n"))
qtt_simb = int(input("Quantos simbolos?\n"))

if qtt_num > 0:
    for i in range(qtt_num):
        num = choice(numeros)
        escolhas.append(num)

if qtt_simb > 0:
    for i in range(qtt_simb):
        simb = choice(simbolos)
        escolhas.append(simb)

while len(escolhas) < total:
    letras = choice([minusculas,maiusculas])
    escolhas.append(choice(letras))

shuffle(escolhas)
senha = "".join(escolhas)

print(f"Sua nova senha é: {senha}")

####################### OLD VERSION #######################

# quantidade = int(input("Quantos digitos deseja em sua senha? "))
# quer_simbolo = input("Deseja simbolos em sua senha? ")

# if quer_simbolo.lower() == "s":
#     escolhas = [minusculas,maiusculas,simbolos,numeros]
# else:
#     escolhas = [minusculas,maiusculas,numeros]

# for i in range(quantidade):
#     lista = choice(escolhas)
#     digito = choice(lista)
#     senha += digito