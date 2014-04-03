'''
Created on Apr 2, 2014

@author: everyone
'''


# get all the xml file 

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
    global mulai
    global sampai
    global mulaiPukul
    global sampaiPukul
    url = 'http://data.bmkg.go.id/%s'%list_url[provinsi]    
    rss = parse(urllib.urlopen(url)).getroot()
    
    for element in rss.findall('Tanggal'):
        mulai = element.find('Mulai').text
        sampai = element.find('Sampai').text
        mulaiPukul= element.find('MulaiPukul')
        sampaiPukul=element.find('SampaiPukul')
    for element in rss.findall('Isi/Row'):
        kota.append(element.find('Kota').text)
        cuaca.append(element.find('Cuaca').text)
        suhumin.append(element.find('SuhuMin').text)
        suhumax.append(element.find('SuhuMax').text)

def receive_kota(value):
    return cuaca[value],mulai,sampai,mulaiPukul,sampaiPukul,suhumin[value],suhumax[value]
# mulai[value],sampai[value],mulaiPukul[value],sampaiPukul[value]
#     print cuaca
#     print mulai
#     print mulaiPukul
#     print sampai
#     print sampaiPukul
#     print suhumin
#     print suhumax


# ada list of kota
def receive_provinsi(key):
    global provinsi
    provinsi=key
    global kota
    parsing_xml()
    return kota
 #   parsing_xml()
    

#def substract(x,y):
#    return x-y

server = SimpleXMLRPCServer(('127.0.0.1',7002))
server.register_function(receive_provinsi)
server.register_function(receive_kota)
print 'server start'
server.serve_forever()