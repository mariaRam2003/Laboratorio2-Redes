import random
import pytest
from Receptor import fletcher_checksum, binary_string_to_bytes

def generate_binary_message(length):
    return ''.join(random.choice('01') for _ in range(length))

def introduce_error(message, error_rate):
    message = list(message)
    num_errors = max(1, int(len(message) * error_rate))
    for _ in range(num_errors):
        pos = random.randint(0, len(message) - 1)
        message[pos] = '1' if message[pos] == '0' else '0'
    return ''.join(message)

# Genera una lista de combinaciones para 100 pruebas
message_lengths = [10, 50, 100, 200, 500, 1000]
error_rates = [0.01, 0.05, 0.1, 0.2, 0.3]

# Combina todas las longitudes y tasas de error para generar más de 100 combinaciones
test_params = [(length, rate) for length in message_lengths for rate in error_rates]

@pytest.mark.parametrize("message_length, error_rate", test_params)
def test_error_detection(message_length, error_rate):
    """Ejecuta pruebas de detección de errores con diferentes longitudes de mensaje y tasas de error."""
    original_message = generate_binary_message(message_length)
    original_data = binary_string_to_bytes(original_message, 8)
    original_checksum = fletcher_checksum(original_data, 8)

    # Genera un mensaje con errores
    erroneous_message = introduce_error(original_message, error_rate)
    erroneous_data = binary_string_to_bytes(erroneous_message, 8)
    erroneous_checksum = fletcher_checksum(erroneous_data, 8)

    # Imprime mensajes para diagnóstico
    print(f"Original message: {original_message}")
    print(f"Erroneous message: {erroneous_message}")
    print(f"Original checksum: {original_checksum}")
    print(f"Erroneous checksum: {erroneous_checksum}")

    # Verifica si el checksum calculado para el mensaje erróneo difiere del checksum original
    assert original_checksum != erroneous_checksum

# Ejecuta las pruebas
if __name__ == "__main__":
    pytest.main()
