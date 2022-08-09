import base64



def hamming_distance(b1,b2):
    
    n1 = int(b1.hex(),16)
    n2 = int(b2.hex(),16)
    
    n3 = n1^n2
    
    return bin(n3).count('1')



fp = open('set1/c6/data6.txt','r')
ct = fp.read()
ct = base64.b64decode(ct)



diffs = []

for KEYLEN in range(2,41):
    
    b1 = None
    diff = 0
    blocks = 0
    
    for i in range(0,len(ct)-KEYLEN,KEYLEN):
        
        b2 = ct[i:i+KEYLEN]
        
        if b1:
            
            diff+=(hamming_distance(b1,b2)/KEYLEN)
            blocks+=1
            
        b1 = b2
        
    diff/=blocks
    diffs.append((KEYLEN,diff))
    
diffs = sorted(diffs,key=lambda x: x[1])
KEYLEN = diffs[0][0]




ct_i = []

for i in range(0,len(ct)):

    if len(ct_i) < KEYLEN:
        ct_i.append(ct[i])
    else:
        ct_i[i%KEYLEN]*=0x100
        ct_i[i%KEYLEN]+=ct[i]



key_i = []
for i in range(0,KEYLEN):

    pts_bytes = []
    num_letters = []

    for j in range(0x000,0x100):

        n1 = ct_i[i]
        n2 = int('0x'+(100*('0'+hex(j)[2:]) if j < 0x10 else 100*hex(j)[2:]),16)
        
        n3 = n1^n2

        n3 = hex(n3)[2:]
        n3 = (200-len(n3))*'0'+n3
        n3 = bytes.fromhex(n3)
        pts_bytes.append(n3)
        
        letters = 0
        for pt_byte in n3:
            if 0x41 <= pt_byte <= 0x5a or 0x61 <= pt_byte <= 0x7a or pt_byte == 32:
                letters+=1
                
        num_letters.append(letters)

    index = num_letters.index(max(num_letters))
    key_i.append(index)



key = ''

for i in key_i:
    key+=chr(i)

print('key')
print(key)
print()


pt = bytearray()
for i in range(0,len(ct)):
    pt.append(ct[i]^key_i[i%KEYLEN])

print('plaintext')
print(pt.decode())