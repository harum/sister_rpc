'''
Created on Apr 2, 2014

@author: root
'''
import xmlrpclib

proxy = xmlrpclib.ServerProxy('http://syahdeini11%40mhs.if.its.ac.id:dinamo92@127.0.0.1:7002')
list_provinsi=['aceh','sumatera utara',"sumatera barat","bengkulu","jambi"]






while True:
    print "daftar provinsi"
    for i in range(len(list_provinsi)):
        print i+1,' ',list_provinsi[i]
    
        
    inp=raw_input("pilih provinsi: ")
    inp=int(inp)-1
    provinsi=[]
    print 'LOADING...........'
    provinsi=proxy.receive_provinsi(inp)
    
    
    print 'daftar kota'
    for i in range(len(provinsi)):
        print i+1,' ',provinsi[i]
    
        
    inp_kota=raw_input('pilih kota : ')
    inp_kota=int(inp_kota)-1
    
    
    #mulai,sampai,mulaiPukul,sampaiPukul
    print '=======================| PERKIRAAN CUACA |============================='
    cuaca,mulai,sampai,mulaiPukul,sampaiPukul,suhu_min,suhu_max=proxy.receive_kota(inp_kota)
    print 'cuaca : ',cuaca
    print 'suhu : ',suhu_min,' - ',suhu_max
    #print mulai,' ',sampai
    print 'pada jam ',mulaiPukul['text'],' pada tanggal ',mulai
    print 'sampai jam ',sampaiPukul['text'],' pada tanggal ',sampai
    print "======================================================================="
    last_inp=raw_input("apakah anda ingin melanjutkan lagi, (Y/N) : ")
    if last_inp=='N' or last_inp=='n':
        print 'terimakasih..'
        break