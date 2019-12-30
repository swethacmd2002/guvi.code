import time, socket, sys
print("\n Welcome to chat room")
print("Initialising.....")
time.sleep(1)

#step 1
s=socket.socket() #creating a socket
host=socket.gethostname()
ip=socket.gethostbyname(host) #used to  the current IP address of the system
port=1234

#step 2
s.bind((host, port)) #binding the host and port

print(host, "(" ,ip, " )\n") #printing the host and ip address

name=input(str("enter your name..."))

#step 3
s.listen(1) #port should listen for connecting to the server
print("\n Waiting for incoming connection...")

conn, addr=s.accept() #when there is any connection, it will accept and get the address

print("\n Received connection from ", addr[0],  addr[1]) #should print which connection has been accepted

s_name=conn.recv(1024) #to get the name of the connector and this will be received in bytes format

s_name=s_name.decode() #decode the bytes into string

print(s_name," has connected to the chatroom")

conn.send(name.encode()) #sending your name to client

#chatting process

while True:
    message=input(str("Me:  "))
    conn.send(message.encode())
    message=conn.recv(1024)  #received message
    message=message.decode()
    print(s_name, ":", message)
    




#First of all we import socket which is necessary.
#Then we made a socket object and reserved a port on our pc.
#After that we binded our server to the specified port. 
#Passing an empty string means that the server can listen to incoming connections from other computers as well. 
#If we would have passed 127.0.0.1 then it would have listened to only those calls made within the local computer.
#After that we put the server into listen mode.
#At last we make a while loop and start to accept all incoming connections and close those connections after a thank you message to all connected sockets.



#Server :
#A server has a bind() method which binds it to a specific ip and port so that it can listen to incoming requests on that ip and port.
#A server has a listen() method which puts the server into listen mode. 
#This allows the server to listen to incoming connections. And last a server has an accept() and close() method. 
#The accept method initiates a connection with the client and the close method closes the connection with the client.