import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Emisor {
    // Función para calcular el checksum de Fletcher
    public static int[] fletcherChecksum(List<Byte> data, int blockSize) {
        int sum1 = 0;
        int sum2 = 0;
        for (byte b : data) {
            sum1 = (sum1 + (b & 0xFF)) % 255;
            sum2 = (sum2 + sum1) % 255;
        }
        return new int[]{sum1, sum2};
    }

    // Función para convertir una cadena binaria a una lista de bytes
    public static List<Byte> binaryStringToList(String binaryStr, int blockSize) {
        List<Byte> result = new ArrayList<>();
        for (int i = 0; i < binaryStr.length(); i += blockSize) {
            String byteStr = binaryStr.substring(i, Math.min(i + blockSize, binaryStr.length()));
            byte b = (byte) Integer.parseInt(byteStr, 2);
            result.add(b);
        }
        return result;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingrese un mensaje en binario: ");
        String binaryMessage = scanner.nextLine();

        // Guardamos el mensaje original antes del padding
        String originalMessage = binaryMessage;

        // Determinamos el tamaño del bloque (8, 16 o 32)
        int blockSize = 8;
        if (binaryMessage.length() % 16 == 0) blockSize = 16;
        if (binaryMessage.length() % 32 == 0) blockSize = 32;

        // Aseguramos que el mensaje tenga longitud adecuada usando padding
        while (binaryMessage.length() % blockSize != 0) {
            binaryMessage += "0";
        }

        List<Byte> data = binaryStringToList(binaryMessage, blockSize);
        int[] checksum = fletcherChecksum(data, blockSize);

        // Concatenamos el checksum al mensaje original
        StringBuilder messageWithChecksum = new StringBuilder(binaryMessage);
        for (int sum : checksum) {
            messageWithChecksum.append(String.format("%8s", Integer.toBinaryString(sum)).replace(' ', '0'));
        }

        System.out.println("Mensaje original: " + originalMessage);
        System.out.println("Mensaje con checksum: " + messageWithChecksum.toString());

        String payload = originalMessage + ";" + messageWithChecksum.toString();

        UDPClient client = new UDPClient("127.0.0.1");
        client.send(payload);
    }
}
