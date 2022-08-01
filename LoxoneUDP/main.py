import socket

UDP_IP = "192.168.100.228"
UDP_PORT = 1234
MESSAGE = "1"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "Message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
             socket.SOCK_DGRAM) # UDP

sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))