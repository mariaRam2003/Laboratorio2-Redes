import java.util.ArrayList;

public class Main{
    public static void main(String[] args){
        UDPServer server = new UDPServer();

        while (true){         
            String receivedData = server.recv();
            int[] msg = cleanMessage(receivedData);
            Reciever reciever = new Reciever(msg);

        }
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