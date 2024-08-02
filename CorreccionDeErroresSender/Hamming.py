from typing import List
from Client import Client
import random

ADRESS = '127.0.0.1'
PORT = 1111

def main():
    client = Client(ADRESS, PORT)
    message = alg_menu()
    message = [int(bit) for bit in message]
    message = encode(message)
    message = noise_layer(message)
    message = format_inforcer(message)    
    client.send(message)


def validate_message(user_message: str):
    for char in user_message:
        if char != "0" and char != "1":
            return False
    return True

def encode_to_binary(ascii_message):
    binary_message = ''.join(format(ord(c), '08b') for c in ascii_message)
    return binary_message

def alg_menu():
    print("Ingresa el mensaje que deseas enviar: ")

    try:
        message = input()

        if message == "":
            raise ValueError
        
        message = encode_to_binary(message)

        return message
    
    except ValueError:
        print("Por favor, introduce un mensaje valido")
        return alg_menu()
    
def noise_layer(message: list)-> list:
    """We flip a bit in the message with a 1% probability

    Args:
        message (list): a list of 1s and 0s

    Returns:
        message (list): a list of 1s and 0s
    """
    for bit_idx in range(len(message)):
        if random.random() < 0.01:
            if message[bit_idx] == 0:
                message[bit_idx] = 1
            else:
                message[bit_idx] = 0

    return message
            
            

def format_inforcer(message: list)-> str:
    formated_str = ""

    for i in message:
        formated_str += str(i) + ","
    formated_str = formated_str[:-1]

    return formated_str

def is_power_of_two(n):
    """
    We check if a number is a power of two
    :param n: any positive integer
    :return: true if n is a power of two, false otherwise
    """
    return (n & (n - 1)) == 0


def encode(message: List[int]):
    """
    :param message: a list of 1s and 0s
    :return: the encoded message with the parity bits
    """
    r = get_parity_bit_no(message)
    encoded_message = []

    j = 0
    for i in range(r + len(message)):
        if is_power_of_two(i + 1):
            # if the index is a power of 2 we add a 0 because it is a parity bit
            encoded_message.append(0)
        else:
            # if the index is not a power of 2 we add the message bit
            encoded_message.append(message[j])
            j += 1

    # We calculate the parity bits
    for i in range(r):
        parity_bit_index = 2 ** i
        parity_bit = calculate_parity_bits(encoded_message, parity_bit_index)
        encoded_message[parity_bit_index - 1] = parity_bit

    return encoded_message


def get_parity_bit_no(message: List[int]):
    """
    We calculate the number of parity bits needed for the message
    :param message: a list of 1s and 0s
    :return: parity bit number
    """
    r = 0  # r is the number of redundant bits
    while not 2 ** r >= len(message) + r + 1:
        r += 1

    return r


def calculate_parity_bits(encoded_message: list, parity_bit_no: int):
    """
    We get the parity bit for the given parity bit number
    :param encoded_message: a list of 1s, 0s and None
    :param parity_bit_no: the index in base one of the parity bit, this number should be a power of 2
    :return:
    """
    if not is_power_of_two(parity_bit_no):
        raise ValueError("The parity bit number should be a power of 2")

    index = parity_bit_no - 1
    to_check = False
    count = 0  # counter for the to_check variable
    count_ones = 0  # counter for the number of 1s in the parity bit

    # We iterate over each index of the encoded message from the position of the parity bit given
    while index < len(encoded_message):
        # to check begins in false and changes to true when the count is 0
        if count % parity_bit_no == 0:
            to_check = not to_check

        if to_check:
            if is_power_of_two(index + 1):
                pass

            elif encoded_message[index] == 1:
                count_ones += 1

        index += 1
        count = (count + 1) % parity_bit_no

    return count_ones % 2


if __name__ == "__main__":
    main()
