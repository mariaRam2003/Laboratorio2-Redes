import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;

public class UDPClient {
    private String adress;
    final int PORT = 1111;

    public UDPClient(String adress){
        this.adress = adress;        
        
    }


    public String recv(){
        String receivedData = "";
        DatagramSocket socket = null;

        try{
            socket = new DatagramSocket();

            // Prepare a buffer to receive the response from the server
            byte[] receiveBuffer = new byte[1024];

            // Create a DatagramPacket to receive the response
            DatagramPacket receivePacket = new DatagramPacket(receiveBuffer, receiveBuffer.length);

            // Receive the response from the server
            socket.receive(receivePacket);

            // Convert the received data to a string and print it
            receivedData = new String(receivePacket.getData(), 0, receivePacket.getLength());
            System.out.println("Received: " + receivedData);
            

        }catch(Exception e){
            e.printStackTrace();
        }finally{
            // Close the socket if it is not null and is still open
            if (socket != null && !socket.isClosed()) {
                socket.close();
            }
        }

        return receivedData;
    }

    public int send(String payload) {
        DatagramSocket socket = null;
        try {
            // Create a DatagramSocket for sending and receiving UDP packets
            socket = new DatagramSocket();

            // Get the IP address of the server
            InetAddress address = InetAddress.getByName(this.adress);

            // Convert the message to bytes
            byte[] sendBuffer = payload.getBytes();

            // Create a DatagramPacket to send the message to the server
            DatagramPacket sendPacket = new DatagramPacket(sendBuffer, sendBuffer.length, address, this.PORT);

            // Send the packet
            socket.send(sendPacket);
        } catch (Exception e) {
            // Print the stack trace if an exception occurs
            e.printStackTrace();
        } finally {
            // Close the socket if it is not null and is still open
            if (socket != null && !socket.isClosed()) {
                socket.close();
            }
        }

        return 0;
    }
}