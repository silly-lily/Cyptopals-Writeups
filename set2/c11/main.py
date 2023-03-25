import Crypto.Random
import Crypto.Random.random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.strxor import strxor


def encryption_oracle(pt):

    key = Crypto.Random.get_random_bytes(16)

    pre = Crypto.Random.get_random_bytes(Crypto.Random.random.randrange(5,11))
    suf = Crypto.Random.get_random_bytes(Crypto.Random.random.randrange(5,11))
    pt = pre+pt+suf
    pt = pad(pt, AES.block_size)
    mode = Crypto.Random.random.randint(0,1)

    ct = None

    if mode == 0:

        cipher = AES.new(key, AES.MODE_ECB)
        ct = cipher.encrypt(pt)

    elif mode == 1:

        iv = Crypto.Random.get_random_bytes(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC,iv)

        ct = cipher.encrypt(pt)

    return ct, mode

def detect(ct):

    rep = 0

    for i in range(0,len(ct),AES.block_size):

        for j in range(0,len(ct),AES.block_size):

            if i != j and ct[i:i+AES.block_size] == ct[j:j+AES.block_size]:
                
                rep+=1

    return 'cbc' if rep == 0 else 'ecb'