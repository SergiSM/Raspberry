import time
import serial
import binascii

try:
    import urllib2 as urlreq # Python 2.x
    from urlparse import urlparse
except:
    import urllib.request as urlreq # Python 3.x

def startscanning(): #function that scan rfid
    size = ser.inWaiting()
    if size:
        x = ser.read(size)
        time.sleep(1)
        x = binascii.hexlify(x)
        q = x.decode("ascii")  #converting scanned data
        '''print(q[4:27]) #converting scanned data
        rfidvalue = q[4:27]
        view(rfidvalue)'''
        print(q)
    else:
 
        print('Scanning...')
 
rfidtag =[]

try:
    ser = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=.0001)
    print("ok")
except:
    try:
        ser = serial.Serial(port='/dev/ttyUSB1', baudrate=9600, timeout=.0001)
        print("ok")
    except:
        print("error")

#ser.write("A0036AF3".encode())
#ser.write(b'A0036AF3')
'''ser.write("A0036A00F3".decode("hex"))
time.sleep(0.5)
out = ser.read(500)
#print(out)
print(binascii.hexlify(out))

ser.write("A006630001006591".decode("hex"))
time.sleep(0.5)
out = ser.read(500)
#print(out)
print(binascii.hexlify(out))

ser.write("A0038200DB".decode("hex"))
time.sleep(0.5)
out = ser.read(500)
#print(out)
print(binascii.hexlify(out))'''

ANTERIOR = ""
TEL = True
timeout = time.time() + 5


def peticio(ser, trama):
    global ANTERIOR
    global TEL    
    global timeout
    check=checksum(trama)
    trama = trama + check
    #print(trama)
    ser.write(trama.decode("hex"))
    time.sleep(0.5)
    out = ser.read(500)
    resposta = binascii.hexlify(out)
    #print(resposta)
    if resposta[0:2] == "e0":
        print(resposta)
        print(resposta[-10:-2])        
        if ANTERIOR != resposta[-10:-2] and TEL==True:
            ANTERIOR = resposta[-10:-2]
            TEL = False
            timeout = time.time() + 5 
            print("*****")
            req = urlreq.Request("https://api.telegram.org/xxxxx/sendMessage?chat_id=502993037&text='"+resposta[-10:-2]+"'")
            urlreq.urlopen(req).read()        

def checksum(trama):
    n_bytes = len(trama)/2
    sum = 0
    for i in range(n_bytes):
        byte_ = trama[i*2:i*2+2]        
        sum += int(byte_, 16)
    sum = bit_not(sum) + 1        
    return hex(sum)[2:]

def bit_not(n):
    return (1 << n.bit_length()) - 1 - n

#12 bytes -> 6 words
#peticio(ser, "A0098100000102012222") #1 word
#peticio(ser, "A00b81000001020211112222") #1 word
words_a_escriure = "1111"+"2222"+"3333"+"4444"+"5555"+"6666"
#peticio(ser, "A0"+"13"+"8100000102"+"06"+words_a_escriure)  #length 9 per 1 word, length 19 per 6 words
#peticio(ser, "A013810000010206111122223333444455556666") 
#print(checksum("A0036A00")) 
#peticio(ser, "A0036A00")

#peticio(ser, "A0068000010201")

while True:
    #peticio(ser, "A0038200")  #EPC Tag Identification
    #peticio(ser, "A0068000010201")  #llegir 1 word EPC Tag Read
   
    if time.time() > timeout:
        TEL = True
        timeout = time.time() + 5 
    
    peticio(ser, "A0068000010202")  #llegir 2 words
    time.sleep(0.2)


ser.close()
#while True:
#    startscanning()

'''size = ser.inWaiting()
if size:
    x = ser.read(size)
    time.sleep(1)
    x = binascii.hexlify(x)
    print(x)'''
