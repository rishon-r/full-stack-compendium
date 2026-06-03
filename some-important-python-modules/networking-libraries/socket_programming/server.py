import socket 
import threading 

# WHAT IS THREADING? : Threading is essentially a way of creating multiple threads within the same program.
# Threading allows us to separate code out so that a piece of code is not waiting for another piece of code to finish before it starts running.

# First, we define a port. 
# WHAT IS A PORT?: When we want to run a server, we pick a port to run the server on. While doing so we also want to ensure that we pick a port 
# where nothing else is running. Port 5050 is usually a safe bet for this.
PORT= 5050

#Now, we define the IP address to run the server on. We can get the IP adress of the machine we want to run the server on using the socket module.
HOST= socket.gethostbyname(socket.gethostname()) 
# this line of code gets us the IP address
# socket.gethostname() gets us the hostname of our current machine
# socket.gethostbyname() resolves this hostname to an IP address
# print(HOST) will now give the name of the IP address of our local computer
# another way to do this is to directly plug in the IP address we want in quotes. You can find IP address of current computer by going into the terminal and typing ifconfig

# Now we need to make a socket. A socket opens up this device to other connections
# A socket is an endpoint for sending and receiving information over a network (A socket is a communication endpoint)
# It is an abstraction provided by the OS that encapsulates (bundles together) an IP address, a Port and a transport protocol (TCP or UDP)
# We now want to essentially bind the socket to the address we have defined above

# INITIALIZZING THE SOCKET
# The 2 parameters are the Address Family and the Socket type
# socket.AF_INET tells us that the adress family we want to use is IPv4. AF stands for address family anf INET means IPv4
# socket.SOCK_STREAM defines the socket type do be that of TCP type
server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Now, server, is a socket object. We need to bind this socket object to an address.
# bind() takes one argument: a two tuple with two elements being the ip address of host and port number respectively.
# It essentially tells the operating sysetem to reserve the following IP address and port number for our socket
addr=(HOST, PORT)
server.bind(addr)

# Now, we want to listen for possible connections to the server. listen() transitions the socket into listening mode where it is ready to listen for incoming connections
# It takes one optional argument, an integer, which represents the maximum number of pending conection requests that can wait before being accepted. 
# This number is known technically as a backlog queue.
# After this maximum backlog is reached, the OS rejects or drops connection requests. 
server.listen()

while True:
    # Above while True creates an infinite loop, indicating that the server will be running forever, always waiting for new clients.
    # We wait until a client tries to connect and then the below line of code is executed.
    # So, the original server socket just listens, does not communicate with clients directly.
    communication_socket, address= server.accept()
    # Here, communication socket is a new socket designated especially for communication with this new client. 
    # address holds the address (IP address, PORT) of the client who just connected
    # When a client connects, their connection request is removed from the backlog queue
    # KEY IDEA: Server socket- still listening for new clients. Communication socket- used for communicating with one specific client.
    # This design allows one server to talk to multiple clients by creating a new socket for each
    # We now print the address of client to which we are connected
    print(f"Connected to {address}")
    # Below code receives a message from the client that just connected. 1024 here serves as the integer argument provided to recv that indicates the
    # maximum number of bytes that a message from client can be. Output of recv() is a byte stream
    #  The .decode('utf-8') converts the byte stream into human readable format according to the utf-8 encoding scheme.
    # The message stated by the client is now stored in the messsage variable.
    message= communication_socket.recv(1024).decode('utf-8')
    print(f"The message received is {message}")
    # The .send() function sends data from the server to the client. It needs an argument passed in byte format. This is why we use encode().
    # The byte stream is now sent from the server to the client.
    communication_socket.send(f"Your message is received".encode('utf-8'))
    # After responding, the connection is closed. 
    communication_socket.close()
    print(f'Connection with address {address} closed')



