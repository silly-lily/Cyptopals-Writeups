from Crypto.Cipher import AES
import base64


fp = open('set1/c7/data7.txt','r')
ct = base64.b64decode(fp.read())

key = b'YELLOW SUBMARINE'

cipher = AES.new(key, AES.MODE_ECB)
pt = cipher.decrypt(ct)

print(pt.decode())