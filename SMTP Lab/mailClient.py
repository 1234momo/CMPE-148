from socket import *
import base64

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# TODO: Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ("mail.smtp2go.com", 2525)

# TODO: Create socket called clientSocket and establish a TCP connection with mailserver
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
    
# Using TLS for requests
# tls = "STARTTLS\r\n"
# clientSocket.send(tls.encode())
# recv_tls = clientSocket.recv(1024).decode()
# print(recv_tls)
# if recv1[:3] != '250':
#    print('250 reply not received from server.')

# gmail authentication
# username = "email"
# pwd = "pwd"
# base64_str = ("\x00" + username + "\x00" + pwd).encode()
# base64_str = base64.b64encode(base64_str)
# authMsg = "AUTH PLAIN ".encode() + base64_str + "\r\n".encode()
# clientSocket.send(authMsg)
# recv_auth = clientSocket.recv(1024)
# print(recv_auth.decode())

# TODO: Send MAIL FROM command and print server response.
mailFrom = "MAIL FROM: <email> \r\n"
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024).decode()
print("MAIL FROM response: " + recv2)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# TODO: Send RCPT TO command and print server response. 
rcptTo = "RCPT TO: <email> \r\n"
clientSocket.send(rcptTo.encode()) # ERROR: 550 relay access denied - please authenticate. 
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

# # TODO: Send message data.
# clientSocket.send(msg.encode())
# recv_msg = clientSocket.recv(1024).decode()
# print("Response after sending message body: " + recv_msg)
# if recv1[:3] != '250':
#     print('250 reply not received from server.')

# # TODO: Message ends with a single period.
# clientSocket.send(endmsg.encode())
# recv_msg_end = clientSocket.recv(1024)
# print("msg end: " + recv_msg_end.decode())
# if recv1[:3] != '250':
#     print('250 reply not received from server.')
    
# TODO: Send QUIT command and get server response.
clientSocket.send("QUIT\r\n".encode())
message = clientSocket.recv(1024)
print(message)
clientSocket.close()