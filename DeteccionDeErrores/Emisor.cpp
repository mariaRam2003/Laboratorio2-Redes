#include <iostream>
#include <vector>
#include <bitset>

// Función para calcular el checksum de Fletcher
std::vector<uint16_t> fletcher_checksum(const std::vector<uint8_t>& data, size_t block_size) {
    uint16_t sum1 = 0;
    uint16_t sum2 = 0;
    for (size_t i = 0; i < data.size(); ++i) {
        sum1 = (sum1 + data[i]) % 255;
        sum2 = (sum2 + sum1) % 255;
    }
    return {sum1, sum2};
}

// Función para convertir una cadena binaria a un vector de enteros
std::vector<uint8_t> binary_string_to_vector(const std::string& binary_str, size_t block_size) {
    std::vector<uint8_t> result;
    for (size_t i = 0; i < binary_str.size(); i += block_size) {
        std::bitset<8> byte(binary_str.substr(i, block_size));
        result.push_back(byte.to_ulong());
    }
    return result;
}

int main() {
    std::string binary_message;
    std::cout << "Ingrese un mensaje en binario: ";
    std::cin >> binary_message;

    // Determinamos el tamaño del bloque (8, 16 o 32)
    size_t block_size = 8;
    if (binary_message.size() % 16 == 0) block_size = 16;
    if (binary_message.size() % 32 == 0) block_size = 32;

    // Aseguramos que el mensaje tenga longitud adecuada usando padding
    while (binary_message.size() % block_size != 0) {
        binary_message += "0";
    }

    std::vector<uint8_t> data = binary_string_to_vector(binary_message, block_size);
    std::vector<uint16_t> checksum = fletcher_checksum(data, block_size);

    // Concatenamos el checksum al mensaje original
    std::cout << "Mensaje con checksum: " << binary_message;
    for (const auto& sum : checksum) {
        std::bitset<8> bits(sum);
        std::cout << bits.to_string();
    }

    return 0;
}