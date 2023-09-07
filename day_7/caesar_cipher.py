def run_operation(operation: str):
    if "encode" != operation and "decode" != operation:
        print("Operação invalida, tente novamente!\n")
        return None
    
    msg = input("Digite a menssagem: ")
    key = int(input("Digite o número chave: "))    

    if operation.lower() == "encode":
        return encrypt(msg, key)
    elif operation.lower() == "decode":
        msg = input("Digite a menssagem: ")
        key = int(input("Digite o número chave: "))
        return decript(msg, key)


def encrypt(msg: str, key: int):
    print(msg, key)


def decript(msg: str, key: int):
    print(msg, key)
    
if __name__ == "__main__":
    while True:
        operation = input("Digite \"encode\" para criptografar, ou \"decode\" para decifrar:\n-> ")
        run_operation(operation)