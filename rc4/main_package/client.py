'''
Created on Mar 24, 2014

@author: root
'''
import socket
import sys
import encryptor_net

clientsocket=socket.socket()
host=socket.gethostname()
#host=socket.gethostname()
port=12345


print "## Connecting to server"
clientsocket.connect((host,port))
print "## Connection successfull"


try:
    while True:
        print "## Handsaking ....."
        print "## Waiting message from server"
        # Get data from network
        data_in=clientsocket.recv(4096)
        # decrypt data
        after_decrypt=encryptor_net.encryption(data_in)
        print ">> "+after_decrypt
        data_in=raw_input("## Enter Message :")
        clientsocket.send(encryptor_net.encryption(data_in))
        
        
except KeyboardInterrupt:
    clientsocket.close()
    sys.exit(0)
