import base64
from Crypto.Cipher import AES

fp = open('set2/c10/data10.txt')
ct = base64.b64decode(fp.read())

key = b'YELLOW SUBMARINE'
iv = b'\x00' * AES.block_size

cipher = AES.new(key, AES.MODE_ECB)

pt = b''
prev = iv

for i in range(0,len(ct),AES.block_size):
    
    block = ct[i:i+AES.block_size]
    
    temp = cipher.decrypt(block)
    
    pt_block = bytes(a ^ b for a, b in zip(prev,temp))
    pt+=pt_block

    prev = block
    
print(pt.decode())
