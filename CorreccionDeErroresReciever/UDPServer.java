import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;

public class UDPServer {
    public String recv() {
        DatagramSocket socket = null;
        String received = "";
        try {
            // Create a DatagramSocket to listen on port 1111
            socket = new DatagramSocket(1111, InetAddress.getByName("127.0.0.1"));
            System.out.println("Server is listening on 127.0.0.1:1111");

            // Buffer to hold incoming data
            byte[] buffer = new byte[1024];

            // Create a DatagramPacket to receive data
            DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
            socket.receive(packet); // Receive packet

            // Get the data from the packet
            received = new String(packet.getData(), 0, packet.getLength());
            System.out.println("Received: " + received);

            // Send a response back to the client
            String response = "Echo: " + received;
            byte[] responseData = response.getBytes();
            DatagramPacket responsePacket = new DatagramPacket(responseData, responseData.length, packet.getAddress(), packet.getPort());
            socket.send(responsePacket);

        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            if (socket != null && !socket.isClosed()) {
                socket.close();
            }
        }

        return received;
    }
}