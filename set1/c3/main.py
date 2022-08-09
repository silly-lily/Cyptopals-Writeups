pts = []
num_letters = []
for i in range(0x00,0x100):

    ct = int('0x1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736',16)
    key = int('0x'+34*(hex(i)[2:] if len(hex(i)[2:]) == 2 else ('0'+hex(i)[2:])),16)
    
    pt = ct^key

    pt = hex(pt)[2:]
    pt = (68-len(pt))*'0'+pt

    pt = bytes.fromhex(pt)
    pts.append(pt)
    
    letters = 0 

    for b in pt:
        if 0x41 <= b <= 0x5a or 0x61 <= b <= 0x7a or b == 0x20:
            letters+=1

    num_letters.append(letters)

index = num_letters.index(max(num_letters))
print(pts[index])
