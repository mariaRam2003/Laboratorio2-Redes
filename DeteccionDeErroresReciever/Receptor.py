def fletcher_checksum(data, block_size):
    sum1 = 0
    sum2 = 0
    for byte in data:
        sum1 = (sum1 + byte) % 255
        sum2 = (sum2 + sum1) % 255
    return [sum1, sum2]

def binary_string_to_bytes(binary_str, block_size):
    return [int(binary_str[i:i+block_size], 2) for i in range(0, len(binary_str), block_size)]

def main():
    original_message = input("Ingrese el mensaje original en binario (sin checksum): ")
    binary_message_with_checksum = input("Ingrese el mensaje en binario con el checksum: ")

    block_size = 8
    if len(binary_message_with_checksum) % 16 == 0: block_size = 16
    if len(binary_message_with_checksum) % 32 == 0: block_size = 32

    data = binary_string_to_bytes(binary_message_with_checksum[:-2*block_size], block_size)
    received_checksum = binary_string_to_bytes(binary_message_with_checksum[-2*block_size:], block_size)

    calculated_checksum = fletcher_checksum(data, block_size)

    if calculated_checksum == received_checksum:
        print("No se detectaron errores. Mensaje original:", original_message)
    else:
        print("Se detectaron errores en el mensaje. Mensaje descartado.")

if __name__ == "__main__":
    main()
