# Challenge
We need to encrypt `Burning 'em, if you ain't quick and nimble<br>I go crazy when I hear a cymbal` with the key `ICE` using key repeating XOR.

#S olution
First we save the string we are encrypted as bytes and do the same for the key. 
````Python
pt = b'Burning \'em, if you ain\'t quick and nimble\nI go crazy when I hear a cymbal'
key = b'ICE'
````

Then we loop through the bytes and and xor the `i-th` byte of the ciphertext with the `i%KEYLEN` byte of the key.
````Python
ct = bytearray()
for i in range(0,len(pt)):
    ct.append(pt[i]^key[i%len(key)])
````

Lastly we print the answer in hexadecimal `0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f`.
````Python
print(ct.hex())
````