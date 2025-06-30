import socket


HOST = "0.0.0.0"
PORT = 12345


server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_socket.bind((HOST,PORT))
server_socket.listen()
print("Listioning on",HOST,PORT)


conn , addr = server_socket.accept()
print("Connected to", addr)

while True:
    data = conn.recv(1024)
    if not data:
        print("Connection closed")
        break
    print("Received buffer",data)
    conn.sendall(data)
