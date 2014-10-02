import socket
import string
import time
import threading

__author__ = "Rohit"

# Dummy client code


ip = "192.168.2.2" # Connecting to IP address of MDPGrp2
port = 5143
# message = "Hello World!"
message = list(string.ascii_lowercase)


# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip, port))


# Send data
def write():
	print "Enter text to send: "
	msg = raw_input()
	while len(msg) != 0 or msg != q:
		client_socket.send(msg)
		print "sending: ", msg
		print "Enter text to send: "
		msg = raw_input()

# Receive data
def receive():
	data = client_socket.recv(1024)
	print "Data received: %s " % data
	while True:
		if (data == 'q' or len(data) == 0):
			break
	
	

# while True:

# 		time.sleep(0.5)

rt = threading.Thread(target = receive)
wt = threading.Thread(target = write)

rt.start()
wt.start()
print "start rt and wt"

rt.join()
wt.join()
print "stop rt and wt"

# Close connections
client_socket.close()
print "End of client program"