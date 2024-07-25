from typing import List


def main():
    # TODO: add the corresponding test cases
    test_message = [1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1]
    encode(test_message)


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
        count = count + 1 % parity_bit_no

    return count_ones % 2


if __name__ == "__main__":
    main()
