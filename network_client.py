import socket

HOST = "127.0.0.1"
PORT = 12345

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((HOST,PORT))
print("Connected to server  via :",HOST,PORT)

while True:
    msg = input("Enter the msg to send or exit to kill the connection:")
    if msg == "exit":
        print("Connection closed")
        break
    client_socket.sendall(msg.encode())
    data = client_socket.recv(1024)
    print("Message received",data)