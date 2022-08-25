BLOCKSIZE = 20
txt = b'YELLOW SUBMARINE'

len_padding = BLOCKSIZE-len(txt)
padded_txt = txt+len_padding*bytes.fromhex('0'+str(len_padding))

print(padded_txt)