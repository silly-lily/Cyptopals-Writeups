fp = open('set1/c4/data4.txt','r')
lines = fp.readlines()

pts_bytes = []
num_letters = []

for line in lines:
    for i in range(0x00,0x100):

        ct = int('0x'+line[:-1],16)
        key = int('0x'+30*hex(i)[2:] if len(hex(i)[2:]) == 2 else '0x'+30*('0'+hex(i)[2:]),16)

        pt = ct^key

        pt_hex = hex(pt)[2:]
        pt_hex = (60-len(pt_hex))*'0'+pt_hex

        pt_bytes = bytes.fromhex(pt_hex)
        pts_bytes.append((line,pt_bytes))

        letters = 0
        for pt_byte in pt_bytes:
            if 0x41 <= pt_byte <= 0x5a or 0x61 <= pt_byte <= 0x7a or pt_byte == 32:
                letters+=1

        num_letters.append(letters)

index = num_letters.index(max(num_letters))
print('ct:',pts_bytes[index][0])
print('pt:',pts_bytes[index][1])