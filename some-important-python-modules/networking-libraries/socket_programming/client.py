import socket

HOST= socket.gethostbyname(socket.gethostname()) # Host address here should be the address of the server as the client is trying to connect to the server
#if this did not all happen in the same Local Area Network and if the server is a part of a different LAN than the client,
# then we would mention the Public IP Address of the Network of which server is a part here
PORT = 5050 # Similar to the Host IP, the Host Port must also reflect the port of the server as that is what we are trying to connect to

socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#socket.connect() serves the opposite role of socket.bind()
#socket.bind() reserves an IP address and port on the local machine so that other computers can connect to it. It is used to wait for incoming connections
# socket.connect() on the other hand attempts to make a connection to a remote server at a given IP address and port.
socket.connect((HOST, PORT))

socket.send(f"Hello server, I am connecting :)".encode('utf-8'))
print(socket.recv(1024).decode('utf-8'))