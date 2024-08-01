import socket


class Client:
    def __init__(self, address: str, port: int, identifier: int):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.address = (address, port)

        # We stablish the connection
        self.send(str(identifier + 4) + ";0,0")


    def recv(self):
        data, addr = self.client.recvfrom(1024)
        data = data.decode()
        identifier, message = self.clean_message(data)
        return message
    
    def send(self, message: str):
        self.client.sendto(message.encode(), self.address)
        print("message sent")

