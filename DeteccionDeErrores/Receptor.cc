#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <iomanip>

// Función que calcula el checksum de Fletcher de un vector de bytes
uint16_t fletcher16(const std::vector<uint8_t>& data) {
    uint16_t sum1 = 0;
    uint16_t sum2 = 0;
    for (uint8_t byte : data) {
        sum1 = (sum1 + byte) % 255;
        sum2 = (sum2 + sum1) % 255;
    }
    return (sum2 << 8) | sum1;
}

// Función que añade padding a un vector de bytes para que su tamaño sea múltiplo de block_size
std::vector<uint8_t> pad_data(const std::vector<uint8_t>& data, size_t block_size) {
    size_t pad_length = (block_size - data.size() % block_size) % block_size;
    std::vector<uint8_t> padded_data = data;
    padded_data.insert(padded_data.end(), pad_length, 0);
    return padded_data;
}

// Función que convierte una cadena de bits en una secuencia de bytes
std::vector<uint8_t> binary_string_to_bytes(const std::string& binary_message) {
    std::vector<uint8_t> data((binary_message.size() + 7) / 8, 0);
    for (size_t i = 0; i < binary_message.size(); ++i) {
        if (binary_message[i] == '1') {
            data[i / 8] |= (1 << (7 - i % 8));
        }
    }
    return data;
}

// Función que recibe un mensaje en binario y verifica si hay
std::string fletcher_checksum_receptor(const std::string& binary_message) {
    std::string original_message = binary_message.substr(0, binary_message.size() - 16);
    std::string received_checksum_bits = binary_message.substr(binary_message.size() - 16);
    uint16_t received_checksum = std::stoi(received_checksum_bits, nullptr, 2);

    std::vector<uint8_t> data = binary_string_to_bytes(original_message);
    std::vector<uint8_t> padded_data = pad_data(data, 2);
    uint16_t calculated_checksum = fletcher16(padded_data);

    if (calculated_checksum == received_checksum) {
        return "No se detectaron errores: " + original_message;
    } else {
        return "Se detectaron errores: el mensaje se descarta.";
    }
}

int main() {
    std::string binary_message;
    std::cout << "Ingrese un mensaje en binario concatenado con la información generada por el emisor: ";
    std::cin >> binary_message;

    std::string result = fletcher_checksum_receptor(binary_message);
    std::cout << result << std::endl;

    return 0;
}