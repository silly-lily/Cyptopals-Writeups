fp = open('set1/c4/data4.txt','r')
lines = fp.readlines()

pts = []
num_letters = []

for line in lines:
    for i in range(0x00,0x100):

        ct = int('0x'+line[:-1],16)
        key = int('0x'+30*hex(i)[2:] if len(hex(i)[2:]) == 2 else '0x'+30*('0'+hex(i)[2:]),16)

        pt = ct^key

        pt = hex(pt)[2:]
        pt = (60-len(pt))*'0'+pt

        pt = bytes.fromhex(pt)
        pts.append((line,pt))

        letters = 0
        for b in pt:
            if 0x41 <= b <= 0x5a or 0x61 <= b <= 0x7a or b == 0x20:
                letters+=1

        num_letters.append(letters)

index = num_letters.index(max(num_letters))
print('ct:',pts[index][0])
print('pt:',pts[index][1])