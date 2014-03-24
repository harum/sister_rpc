'''
Created on Mar 23, 2014

@author: root

'''
from PyQt4.Qt import endl

def initialization(key):
    # making a s-box
    j=0
    global S
    S=[]
    
    for i in range(256): #initialize element
        S.append(i)
        
    for i in range(256):
        j=(j+S[i]+ord(key[i % len(key)])) % 256
        S[i],S[j]=S[j],S[i] # swaping element


# xor each byte with the choosen S-box element
# d for byte of data, i & j is static
i_itr=0
j_itr=0
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
def byte_encrypt(path):
    # initialize i & j for opeartion
    # opening target file
    file_target=open("output.txt","wb")    
    #reading file byte by byte 
    file=open(path,"rb")
    byte=file.read(1)   # read each byte of file
    byte=unicode(byte)
    while byte!="":
        byte=operation(byte) # encrypt each byte of data
#        print byte
        file_target.write(format(byte,"02x"))
        byte=file.read(1)
    

# Main function
def encryption(path,key):
    initialization(key)
    byte_encrypt(path)


file_key=open("key.txt","r")
keys=file_key.read(300)
#print list(keys)
#print list(keys)
encryption("data.txt",list(keys))
