<h1>Challenge</h1>
We are given a list of possible ciphertexts and need to figure out which one has been encrypted using single character XOR.

<h1>Solution</h1>

First we load and read the data. 
````Python
fp = open('set1/c4/data4.txt','r')
lines = fp.readlines()
````

Then we initalize arrays for possible plaintexts and the corresponding number of letters and spaces in each of these plaintexts.
````Python
pts = []
num_letters = []
````

Next we loop through every possible ciphertext.
````Python
for line in lines:
````

Then in this loop of every possible ciphertext, we loop through every possible key to get every possible plaintext value.
````Python
for i in range(0x00,0x100):
````

Then we make the hex ciphertext string from the line we just read into an integer. We include the `0x` so python knows our string is a representation of a hex number and we don't include the last character of the line because it is a new line character.
````Python
ct = int('0x'+line[:-1],16)
````

Next we make the key. We construct a hexadecimal string that starts wtih `0x` to signify to the program that it is a hexadecimal number. Then it is followed by 30 repreating bytes.
````Python
key = int('0x'+30*hex(i)[2:] if len(hex(i)[2:]) == 2 else '0x'+30*('0'+hex(i)[2:]),16)
````

Next we XOR a possible ciphertext with a possible key to get a possible plaintext.
````Python
pt = ct^key
````

Then we transform this XORed integer into a hex string, pad the hex string, and transform this string into bytes. We make a tupple with the possible ciphertext and append this ciphertext plaintext pair to the list of possible plaintexts. 
````Python
pt = hex(pt)[2:]
pt = (60-len(pt))*'0'+pt

pt = bytes.fromhex(pt)
pts.append((line,pt))
````

Next we count the number of letters and spaces in this possible plaintext. Lowercase letters are between `0x41` and `0x5a`, uppercase letters are between `0x61` and `0x7a`, and spaces are `0x20`.
````Python
letters = 0
for b in pt:
    if 0x41 <= b <= 0x5a or 0x61 <= b <= 0x7a or b == 0x20:
        letters+=1
    num_letters.append(letters)
````

Lastly, we find which plaintext has the most letters and spaces and print the ciphertext `ct: 7b5a4215415d544115415d5015455447414c155c46155f4058455c5b523f` and the plaintext `pt: b'Now that the party is jumping\n`.
````Python
index = num_letters.index(max(num_letters))
print('ct:',pts[index][0])
print('pt:',pts[index][1])
````