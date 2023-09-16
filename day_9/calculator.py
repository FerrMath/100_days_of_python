from art import logo
import os

def calculator():
    operations = {
        "+" : add,
        "-" : sub,
        "*" : multiply,
        "/" : divide
    }
    # TODO verify if input values are valid
    value_1 = float(input("Enter the first number: "))

    while True:
        value_2 = float(input("Enter the next value: "))
        print("\nPossible operations:")
        
        for k in operations:
            print("--> " + k)
        operation = input("\nEnter operation: ")
        final = operations[operation](value_1, value_2)
        clear_screen()
        print(f"Result -- > {value_1} {operation} {value_2} = {final:.2f}\n")
        
        # Verifies if user wants to use the final result for the next operation
        # TODO need to clean the code
        continue_with_previous_value = input("Continue operations with the previous result?\n[y] / [n]: ").lower() == "y"
        
        if continue_with_previous_value:
            value_1 = final
            clear_screen()
        else:
            clear_screen()
            return calculator()


def add(n:float, m:float):
    return n + m


def sub(n:float, m:float):
    return n - m


def multiply(n:float, m:float):
    return n * m


def divide(n:float, m:float):
    return n / m


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    print(logo + "\n")
    calculator()
