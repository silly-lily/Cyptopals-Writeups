pt = b'Burning \'em, if you ain\'t quick and nimble\nI go crazy when I hear a cymbal'
key = b'ICE'

ct = bytearray()
for i in range(0,len(pt)):
    ct.append(pt[i]^key[i%len(key)])

print(ct.hex())