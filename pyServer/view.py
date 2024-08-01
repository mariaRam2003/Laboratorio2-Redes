def main_menu():
    print("~~~~~~~~~~~Bienvenido al Laboratorio 2 de Redes~~~~~~~~~~~")
    print("1. Hamming Codes")
    print("2. Fletcher Checksum")
    print("Elige tu algoritmo: ")
    
    try:
        choice = int(input())

        if choice > 2 or choice < 1:
            print("Por favor, introduce un número válido")
            raise ValueError

    except ValueError:
        print("Por favor, introduce un número")
        return main_menu()
    
    return choice
    
def alg_menu():
    print("Ingresa el mensaje que deseas enviar: ")

    try:
        message = input()

        if message == "":
            raise ValueError
        
        if not validate_message(message):            
            raise ValueError

        return message
    
    except ValueError:
        print("Por favor, introduce un mensaje valido")
        return alg_menu()
    
def validate_message(user_message: str):
    for char in user_message:
        if char != "0" and char != "1":
            return False
    return True
