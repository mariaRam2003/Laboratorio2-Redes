import socket
import random
from view import main_menu, alg_menu

adresses = {}
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ADRESS = '127.0.0.1'
IDENTIFIERS = {
    1: "HAMMING_SENDER",
    2: "HAMMING_RECEIVER",
    3: "FLETCHER_SENDER",
    4: "FLETCHER_RECEIVER"
}


def main():
    global adresses, server
    server.bind((ADRESS, 1111))

    alg = main_menu()
    message = alg_menu()

    sent = False 
    while True:

        if sent:
            data, addr = server.recvfrom(1024)        
            identifier, message = clean_message(data.decode())

            controller(identifier, message, addr)

        elif (1 in adresses and 2 in adresses) or (3 in adresses and 4 in adresses):            
            if alg == 1:
                server.sendto(format_inforcer(message, 0).encode(), adresses[1])
            elif alg == 2:
                server.sendto(format_inforcer(message, 0).encode(), adresses[3])

            sent = True
        else:
            data, addr = server.recvfrom(1024)        
            identifier, message = clean_message(data.decode())

            controller(identifier, message, addr)

       


def controller(identifier: int, message: list, addr: str)-> tuple:
    """_summary_

    Args:
        identifier (int): This is the identifier from the sender
        message (list): This is the message that the sender wants to send
        addr (str): This is the address of the sender

    Returns:
        str: _description_
    """
    global adresses, server

    # Hamming Code Sender
    if identifier == 1:        
        message = noise_layer(message)
        message = format_inforcer(message, 0)
        recv_address = adresses[2]

         # We send the message to the receiver
        server.sendto(message.encode(), recv_address)

        # We tell the sender the message was sent
        server.sendto("Message sent".encode(), addr)

    # Hamming Code Receiver
    elif identifier == 2:
        print("Mensaje recibido: ", message)

    # Fletcher Checksum Sender
    elif identifier == 3:
        pass

    # Fletcher Checksum Receiver
    elif identifier == 4:
        pass

    # Here we add the adresses to the dictionary
    elif identifier > 4 and identifier < 9:
        identifier = identifier - 4
        adresses[identifier] = addr

        
    
    else:
        print("Identificador no válido")
        

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
            
            
            
    pass

def format_inforcer(message: list, identifier: int)-> list:
    formated_str = ""

    formated_str += str(identifier) + ";"

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