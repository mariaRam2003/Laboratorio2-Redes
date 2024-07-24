def fletcher16(data: bytes) -> int:
    sum1 = 0
    sum2 = 0
    for byte in data:
        sum1 = (sum1 + byte) % 255
        sum2 = (sum2 + sum1) % 255
    return (sum2 << 8) | sum1

def pad_data(data: bytes, block_size: int) -> bytes:
    pad_length = (block_size - len(data) % block_size) % block_size
    return data + b'\x00' * pad_length

def fletcher_checksum_emisor(binary_message: str) -> str:
    data = int(binary_message, 2).to_bytes((len(binary_message) + 7) // 8, byteorder='big')
    padded_data = pad_data(data, 2)  # 2 bytes for 16 bits
    checksum = fletcher16(padded_data)
    checksum_bits = bin(checksum)[2:].zfill(16)
    return binary_message + checksum_bits

binary_message = input("Ingrese un mensaje en binario: ")
encoded_message = fletcher_checksum_emisor(binary_message)
print("Mensaje codificado:", encoded_message)