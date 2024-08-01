import socket
import random
from Hamming import encode

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ADRESS = "127.0.0.1"
PORT = 1111

def main():
    
    server.bind((ADRESS, PORT))

    while True:
        message = alg_menu()
        message = encode([int(bit) for bit in message])
        message = noise_layer(message)
        message = format_inforcer(message, 1)

        message = message.encode()
        server.sendto(message, (ADRESS, 1112))
        


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

def noise_layer(message: list)-> list:
    """We flip a bit in the message with a 1% probability

    Args:
        message (list): a list of 1s and 0s

    Returns:
        message (list): a list of 1s and 0s
    """
    for bit_idx in range(len(message)):
        if random.random() < 0.01:
            message[bit_idx] = not message[bit_idx]

    return message
            
            

def format_inforcer(message: list)-> str:
    formated_str = ""

    for i in message:
        formated_str += str(i) + ","
    formated_str = formated_str[:-1]

    return formated_str


def clean_message(user_message: str)-> tuple:
    identifier, message = user_message.split(";")
    identifier = int(identifier)
    message = message.split(",")
    message = [int(num) for num in message]
    return identifier, message
    


if __name__ == "__main__":
    main()