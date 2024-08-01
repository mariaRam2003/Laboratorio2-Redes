from client import Client
from Hamming import encode

# The identifier is 1 in this case because we are the hamming code sender
IDENTIFIER = 1

def main():
    client = Client("127.0.0.1", 1111, IDENTIFIER)
    
    while True:
        recv_data = client.recv()

        identifier, message = clean_message(recv_data)
        encoded_msg = encode(message)
        formated_msg = format_inforcer(encoded_msg, IDENTIFIER)

        client.send(formated_msg)
        print("Message sent")


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