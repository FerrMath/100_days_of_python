import string

letras = string.ascii_lowercase

def run_operation(operation: str):
    if "encode" != operation and "decode" != operation:
        print("Operação invalida, tente novamente!\n")
        return None
    
    msg = input("Digite a menssagem: ")
    key = int(input("Digite o número chave: "))    

    if operation.lower() == "encode":
        return encrypt(msg, key)
    elif operation.lower() == "decode":
        return decript(msg, key)


def encrypt(msg: str, key: int):
    encrypted = ""
    for letra in msg:
        if letra in letras:
            base = letras.find(letra)
            index = (base + key) % len(letras)
            encrypted += letras[index]
        else:
            encrypted += letra
    return encrypted


def decript(msg: str, key: int):
    decrypted = ""
    for letra in msg:
        if letra in letras:
            base = letras.find(letra)
            index = (base - key) % len(letras)
            decrypted += letras[index]
        else:
            decrypted += letra
    return decrypted

if __name__ == "__main__":
    while True:
        operation = input("Digite \"encode\" para criptografar, ou \"decode\" para decifrar:\n-> ")
        print(run_operation(operation))
