# Challenge
We need to pad `YELLOW SUBMARINE` using PKCS#7 padding. The blocksize is 20 bytes.

# Solution
First the blocksize should be  `20`.
````Python
BLOCKSIZE = 20
````

Then the text needs to represented by bytes.
````Python
txt = b'YELLOW SUBMARINE'
````

Then we need to calculate the number of bytes needed. We subtract blocksize from the number of bytes in text. 
````Python
len_padding = BLOCKSIZE-len(txt)
````

Then once we find the number of bytes we need to pad, we pad this number of bytes the number of bytes times.
````Python
padded_txt = txt+len_padding*bytes.fromhex('0'+str(len_padding))
````

Finally we print the solution.
````Python
print(padded_txt)
````