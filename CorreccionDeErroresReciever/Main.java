import java.util.ArrayList;

public class Main{
    public static void main(String[] args){
        UDPServer server = new UDPServer();

        while (true){         
            String receivedData = server.recv();
            int[] msg = cleanMessage(receivedData);
            Reciever reciever = new Reciever(msg);
            // int parityBits = reciever.getParityBitNumber(msg);
            // String message = extractNonParityBits(msg, parityBits);
            // String message2 = arrayToBinaryString(msg);
            // message = decodeFromBinary(message2);

            // System.out.println("Mensaje recibido: " + message);

        }
    }

    public static String decodeFromBinary(String binaryMessage) {
        StringBuilder asciiMessage = new StringBuilder();
        for (int i = 0; i < binaryMessage.length(); i += 8) {
            String byteString = binaryMessage.substring(i, i + 8);
            char asciiChar = (char) Integer.parseInt(byteString, 2);
            asciiMessage.append(asciiChar);
        }
        return asciiMessage.toString();
    }

    public static String extractNonParityBits(int[] hammingCode, int parityQuantity) {
        StringBuilder originalMessage = new StringBuilder();
        int length = hammingCode.length;

        for (int i = 0; i < length; i++) {
            // Check if the current index is a power of 2 (parity bit position)
            if ((i + 1 & i) != 0) {
                originalMessage.append(hammingCode[i]);
            }
        }
        return originalMessage.toString();
    }

    public static String arrayToBinaryString(int[] binaryArray) {
        StringBuilder binaryString = new StringBuilder();
        for (int bit : binaryArray) {
            binaryString.append(bit);
        }
        return binaryString.toString();
    }

    public static int[] cleanMessage(String userMessage) {
        String[] messageParts = userMessage.split(",");
        int[] message = new int[messageParts.length];

        for (int i = 0; i < messageParts.length; i++) {
            message[i] = Integer.parseInt(messageParts[i]);
        }
        return message;
    }
}