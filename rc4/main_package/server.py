'''
Created on Mar 24, 2014

@author: root
'''

import socket
from __builtin__ import str
import sys
import pickle
from thread import *
from main_package.client import after_decrypt
import encryptor_net

# create socket object
s= socket.socket()

# Get local hostname
#host = socket.gethostname() 

# reserver port 
port = 12345

# bind the port
s.bind(('',port))

# put socket to listening mode
s.listen()



#Thread to handle client
def clientthread(conn):
    
    while True:
        data_in=raw_input("## Enter Message :")
        conn.send(encryptor_net.encryption(data_in))
        print "## Waiting message from client"
        data_in=conn.recv(4096)
        print ">> "+encryptor_net.encryption(data_in)
    



# looping to accept connection
try:
    
    while True:
        print '## waiting for client....'
        c,addr = s.accept() # Establish connection with client
        print '## Got connection from ',addr
        start_new_thread(clientthread,(c,))
        
except KeyboardInterrupt:
    s.close()
    sys.exit(0)
    
