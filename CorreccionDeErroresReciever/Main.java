import java.util.ArrayList;

public class Main{
    // The identifier is 2 because we are the hamming reciever
    static int IDENTIFIER = 2;

    public static void main(String[] args){
        UDPClient client = new UDPClient("127.0.0.1", 2); 

        while (true){
            String recvData = client.recv();

            int[] message = cleanMessage(recvData);
            Reciever reciever = new Reciever(message);
            String response = reciever.run();

            client.send(response);
            System.out.println("Response sent: " + response);
        }
    }

    public static int[] cleanMessage(String userMessage) {
        String[] parts = userMessage.split(";");
        int identifier = Integer.parseInt(parts[0]);
        String[] messageParts = parts[1].split(",");
        int[] message = new int[messageParts.length];

        for (int i = 0; i < messageParts.length; i++) {
            message[i] = Integer.parseInt(messageParts[i]);
        }
        return message;
    }
}