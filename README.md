


# Jafar Abdollahi

<h2> Discription </h2>
# Simple-Chat-Room-using-Python
We've made it through the basics of working with sockets, and now we're ready to try to actually build something with them, so, in this sockets with Python tutorial, we're going to build a console-based chat app.


Client:
A client is a computer that requests the service from the server through a network. In most cases, clients are normal computers, tablets, phones, etc. A client request to the server, and the server gives a response to the client.

Protocols:
The communication (sending and receiving of data packets) between clients and servers follows some rules called protocols. There are two types of protocols that we need in our application

TCP
UDP
TCP: Transmission Control Protocol (TCP) is reliable as it guarantees the delivery of data packets to the destination.

UDP: User diagram protocol (UDP) on other hand cannot guarantee the successful delivery of data packets.

You can also check more on TCP and UDP here.

Socket:
The socket is a method of communication between the client and the server in a network.

Analogy: If you need a mouth to talk and communicate, so you need a socket to communicate.

A server binds its socket with an address so that different clients can identify it. The socket is made up of two parts

IP Address
Port
A client needs an IP address and port number on which the server is listening to reach the server.

Create a Basic Server and Client in Python.



 The Server Side Code
import time, socket, sys
print('Setup Server...')
time.sleep(1)
#Get the hostname, IP Address from socket and set Port
soc = socket.socket()
host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)
port = 1234
soc.bind((host_name, port))
print(host_name, '({})'.format(ip))
name = input('Enter name: ')
soc.listen(1) #Try to locate using socket
print('Waiting for incoming connections...')
connection, addr = soc.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")
print('Connection Established. Connected From: {}, ({})'.format(addr[0], addr[0]))
#get a connection from client side
client_name = connection.recv(1024)
client_name = client_name.decode()
print(client_name + ' has connected.')
print('Press [bye] to leave the chat room')
connection.send(name.encode())
whileTrue:
message = input('Me > ')
if message == '[bye]':
message = 'Good Night...'
connection.send(message.encode())
print("\n")
break
connection.send(message.encode())
message = connection.recv(1024)
message = message.decode()
print(client_name, '>', message)


The Client Side Code
import time, socket, sys
print('Client Server...')
time.sleep(1)
#Get the hostname, IP Address from socket and set Port
soc = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
#get information to connect with the server
print(shost, '({})'.format(ip))
server_host = input('Enter server\'s IP address:')
name = input('Enter Client\'s name: ')
port = 1234
print('Trying to connect to the server: {}, ({})'.format(server_host, port))
time.sleep(1)
soc.connect((server_host, port))
print("Connected...\n")
soc.send(name.encode())
server_name = soc.recv(1024)
server_name = server_name.decode()
print('{} has joined...'.format(server_name))
print('Enter [bye] to exit.')
whileTrue:
message = soc.recv(1024)
message = message.decode()
print(server_name, ">", message)
message = input(str("Me > "))
if message == "[bye]":
message = "Leaving the Chat room"
soc.send(message.encode())
print("\n")
break
soc.send(message.encode())



<h2> Contact me </h2>
You can reach me at:

Email: ja.abdollahi77@gmail.com
<br>
LinkedIn: https://www.linkedin.com/in/jafar-abdollahi-7647971b3/
<br>
Google Scholar: https://scholar.google.com/citations?user=2dK8kPwAAAAJ&hl=en
<br>
researchgate: https://www.researchgate.net/profile/Jafar-Abdollahi?ev=hdr_xprf&_tp=eyJjb250ZXh0Ijp7ImZpcnN0UGFnZSI6ImxvZ2luIiwicGFnZSI6ImhvbWUiLCJwcmV2aW91c1BhZ2UiOiJsb2dpbiIsInBvc2l0aW9uIjoiZ2xvYmFsSGVhZGVyIn19
<br>
youtube: https://www.youtube.com/@jafarabdollahi/featured
<br>
<img src="https://github.com/Jafar-Abdollahi/cuffless-bp-master-in-python-jupyter-/blob/main/2024-07-07_19-45-22.png"> 
<br>
<img src=" "> 
