from socket import *

msg = "Hello from Hamsika, William, Donie, and Gary\n😭😂😂😭\r\n"
endmsg = "\r\n.\r\n"


# TODO: Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ("mail.smtp2go.com", 2525)


# TODO: Create socket called clientSocket and establish a TCP connection with mail server
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')
   
    
# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')


# TODO: Send MAIL FROM command and print server response.
mailFrom = "MAIL FROM: <garychang9@gmail.com> \r\n"
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024).decode()
print("MAIL FROM response: " + recv2)
if recv1[:3] != '250':
    print('250 reply not received from server.')


# TODO: Send RCPT TO command and print server response. 
rcptTo = "RCPT TO: <gary.chang@sjsu.edu> \r\n"
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1024).decode()
print("RCPT TO response: " + recv3)
if recv1[:3] != '250':
    print('250 reply not received from server.')


# TODO: Send DATA command and print server response. 
data = "DATA\r\n"
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024).decode()
print("DATA response: " + recv4)
if recv1[:3] != '250':
    print('250 reply not received from server.')


# TODO: Send message data and a single period denoting message ending
subject = "Subject: SMTP lab test \r\n\r\n" 
clientSocket.send(subject.encode())
clientSocket.send(msg.encode())
clientSocket.send(endmsg.encode())
recv_msg = clientSocket.recv(1024)
print("Response after sending message body:" + recv_msg.decode())
if recv1[:3] != '250':
    print('250 reply not received from server.')

    
# TODO: Send QUIT command and get server response.
clientSocket.send("QUIT\r\n".encode())
message = clientSocket.recv(1024)
print(message)
clientSocket.close()