'''
Created on Mar 23, 2014

@author: root

'''
from PyQt4.Qt import endl

input_file="data.txt"
output_file="output.txt"


# making a s-box 
def initialization(key):
    j=0
    global S
    S=[]
    
    for i in range(256): #initialize element
        S.append(i)
        
    for i in range(256):
        j=(j+S[i]+ord(key[i % len(key)])) % 256
        S[i],S[j]=S[j],S[i] # swaping element

# initialize i & j for opeartion (global variable)
i_itr=0
j_itr=0

# xor each byte with the choosen S-box element
# d for byte of data, i & j is static
def operation(d):
    global i_itr
    global j_itr
    #print 'sebelum ',i_itr
    i_itr=(i_itr+1)%256
    #print i_itr
    j_itr=(j_itr+S[i_itr])%256
    S[i_itr],S[j_itr]=S[j_itr],S[i_itr]
    pr=S[(S[i_itr]+S[j_itr])% 256]
    return ord(d) ^ pr  # in python ^ is bitwise XOR operation

# encrypt all the data
def byte_encrypt(data):
    global output_file
    
    out=""
    for c in data:
        byte=operation(c)
        out+=chr(byte)
    return out

# Main function to encrypt data, using path input, and key (list)
def encryption(data):
    file_key=open("key.txt","r")
    keys=file_key.read(300)
    initialization(list(keys))
    return byte_encrypt(data)
    

