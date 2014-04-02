'''
Created on Apr 2, 2014

@author: Prana Pratistha
'''

import urllib   
from elementtree.ElementTree import parse
from SimpleXMLRPCServer import SimpleXMLRPCServer

provinsi=0
kota=0
list_url=['propinsi_01_1.xml','propinsi_02_1.xml','propinsi_03_1.xml','propinsi_04_1.xml','propinsi_05_1.xml']
kota=[]
cuaca=[]
suhumin=[]
suhumax=[]

def parsing_xml():
    global kota
    global cuaca
    global suhumin
    global suhumax
    url = 'http://data.bmkg.go.id/%s'%list_url[provinsi]    
    rss = parse(urllib.urlopen(url)).getroot()
    
    for element in rss.findall('Tanggal'):
        mulai = element.find('Mulai').text
        sampai = element.find('Sampai').text
    
    for element in rss.findall('Isi/Row'):
        kota.append(element.find('Kota').text)
        cuaca.append(element.find('Cuaca').text)
        suhumin.append(element.find('SuhuMin').text)
        suhumax.append(element.find('SuhuMax').text)

def receive_kota(value):
    return cuaca[value],suhumin[value],suhumax[value]
    


# ada list of kota
def receive_provinsi(key):
    global provinsi
    provinsi=key
    global kota
    parsing_xml()
    return kota

server = SimpleXMLRPCServer(('127.0.0.1',7001))
server.register_function(receive_provinsi)
server.register_function(receive_kota)
print 'server start'
server.serve_forever()