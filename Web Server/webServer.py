from socket import * # import socket module
import sys # In order to terminate the program

# Create TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# TODO: Prepare a sever socket
PORT = 80
serverSocket.bind(('', PORT))
serverSocket.listen(1)
print('web server is listening on port:', PORT)

while True:
    # TODO: connectionSocket, addr = ?
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    
    try:
        # TODO: message = ? and outputdata = ?
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        
        # TODO: Send one HTTP header line into socket
        connectionSocket.send(b'\nHTTP/1.1 200 OK\n\n')
        
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode('utf-8'))
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        # TODO: Send response message for file not found
        connectionSocket.send(b'Error 404: File not found')
        
        # TODO: Close client socket
        connectionSocket.close()
serverSocket.close()

#Terminate the program after sending the corresponding data
sys.exit()