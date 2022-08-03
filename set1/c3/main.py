pts_bytes = []
num_letters = []
for i in range(0x00,0x100):

    ct = int('0x1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736',16)
    key = int('0x'+34*hex(i)[2:] if len(hex(i)[2:]) == 2 else '0x'+34*('0'+hex(i)[2:]),16)
    
    pt = ct^key

    pt_hex = hex(pt)[2:]
    pt_hex = (68-len(pt_hex))*'0'+pt_hex

    pt_bytes = bytes.fromhex(pt_hex)
    pts_bytes.append(pt_bytes)
    
    letters = 0 

    for pt_byte in pt_bytes:
        if 0x41 <= pt_byte <= 0x5a or 0x61 <= pt_byte <= 0x7a or pt_byte == 32:
            letters+=1

    num_letters.append(letters)

index = num_letters.index(max(num_letters))
print(pts_bytes[index])
