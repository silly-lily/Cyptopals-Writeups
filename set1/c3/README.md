<h1>Challenge</h1>

We are given the hex ciphertext `1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736` that
has been encrypted with single character XOR. We need to find the plaintext.

<h1>Solution</h1>

First we intialize two empty arrays one for plaintext bytes `pts_bytes` and one for the corresponding amount of letters in these plaintexts `num_letters`.

````Python
pts = []
num_letters = []
````

Next we loop through ever possible key.

````Python
for i in range(0x00,0x100):
````

Then inside this loop, we transform our ciphertext string into an integer `ct`. We add `0x` as a prefix to the hex string so that the program knows our integer is represented by hexadecimal.

````Python
ct = int('0x1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736',16)
````

Then we make the key. Every key starts with the prefix `0x` so that the program knows our key string that we're building is represented by hexadecimal. Next we have 34 characters because our cipher text is 34 characters long of the same repeating two hexadecimal numbers or byte. We pad with a zero if the hexadecimal number is less than `0x10`.

````Python
key = int('0x'+34*(hex(i)[2:] if len(hex(i)[2:]) == 2 else ('0'+hex(i)[2:]))
````

Next we XOR the ciphertext and key to get a possible plaintext.

````Python
pt = ct^key
````

Then we save this integer as a hexadecimal string and pad it so that it is exactly 34 bytes long (the same length as the ciphertext). We conver the plaintext to a bytes object and append it to our array of plaintexts.

````Python
pt = hex(pt)[2:]
pt = (68-len(pt))*'0'+pt

pt = bytes.fromhex(pt)
pts.append(pt)
````

Then we count the number of letters and spaces in this possible plaintext. Looking at an ascii chart, lowercase letters are between `0x41` and `0x5a`, uppercase are between `0x61` and `0x7a`, and spaces are `0x20`. We add the number of letters to an array `num_letters` where each entry is corresponding to a possible plaintext.

````Python
    letters = 0 

    for b in pt:
        if 0x41 <= b <= 0x5a or 0x61 <= b <= 0x7a or b == 0x20:
            letters+=1

    num_letters.append(letters)
````

Lastly, we find the plaintext with the most number of letters and spaces and we print our solution `b"Cooking MC's like a pound of bacon"`.

````Python
index = num_letters.index(max(num_letters))
print(pts_bytes[index])
````
