# Challenge
We need to decrypt the base64 ciphertext which was encrypted under hex using the vigenere cipher. 

# Solution
We need to import the `base64` package with deals with base64 numbers.
````Python
import base64
````

We need to write a function that calculates hamming distance which is the bitwise difference of two integers. First we take two hex strings and transform them to integers. Then we XOR them to find the differennt bits and count the number of 1's (different bits).
````Python
def hamming_distance(b1,b2):
    
    n1 = int(b1.hex(),16)
    n2 = int(b2.hex(),16)
    
    n3 = n1^n2
    
    return bin(n3).count('1')
````

Next we openn the file, read the file, and decode the file into a bytes object from a base64 string.
````Python
fp = open('set1/c6/data6.txt','r')
ct = fp.read()
ct = base64.b64decode(ct)
````

Then we find the key length. We loop through every possible key length `2` to `40`. Then we break the ciphertext into blocks of `KEYLEN` length and find the hamming disance. We average the hamming distance of these blocks and normalize by dividing by the KEYLEN. The smallest normalized distance corresponds to the most likely key length which is `29`.
````Python
diffs = []

for KEYLEN in range(2,41):
    
    b1 = None
    diff = 0
    blocks = 0
    
    for i in range(0,len(ct)-KEYLEN,KEYLEN):
        
        b2 = ct[i:i+KEYLEN]
        
        if b1:
            
            diff+=(hamming_distance(b1,b2)/KEYLEN)
            blocks+=1
            
        b1 = b2
        
    diff/=blocks
    diffs.append((KEYLEN,diff))
    
diffs = sorted(diffs,key=lambda x: x[1])
KEYLEN = diffs[0][0]
````

Since the ciphertext was encrypted using the vigenere cipher, the `i` ciphertext character was XORed with the `i%KEYLEN` character of the key. So we need to do single character XOR on every `i%KEYLEN` value. In other words we need to build a number for every remainder `i%KEYLEN=0`, `i%KEYLEN=1`,...,`i%KEYLEN=28` and compute single character XOR on each individual string. We build this number by taking every `i%KEYLEN=n` hexadecimal number and concatting it with the next. So `0x010203040506` would make `0x010305` and `0x020406` for a KEYLEN of `2`.
````Python
ct_i = []

for i in range(0,len(ct)):

    if len(ct_i) < KEYLEN:
        ct_i.append(ct[i])
    else:
        ct_i[i%KEYLEN]*=0x100
        ct_i[i%KEYLEN]+=ct[i]
````

We intalize an empty array to store each byte of the key. Then we loop through each byte of the key:
````Python
key_i = []
for i in range(0,KEYLEN):
````

To find every byte of the key, we do single character XOR. First we intialize emtpy arrays for plaintexts stored in bytes format `pts_bytes` and the corresponding number of letters and spaces `num_letters`. Then we loop through every possible key. Get the `i-th` hex number found above for `n1`. Then for `n2` we build a key the repeats `j` exactly `50` times. We XOR `n1` and `n2` to get `n3` our possible cipher text. We transform the `n3` to a hex string, pad it, and then transform it to bytes. We count the number of letters and spaces in it. Lowercase letters are between `0x41` and `0x5a`, upercase letters are between `0x61` and `0x7a`, and spaces are equal to `0x20`. We append this number of letters and spaces to `num_letters`. Then we find which plaintext has the most letters and spaces and that is our plaintext and key pair for that position in the key.
````Python 
    pts_bytes = []
    num_letters = []

    for j in range(0x000,0x100):

        n1 = ct_i[i]
        n2 = int('0x'+(100*('0'+hex(j)[2:]) if j < 0x10 else 100*hex(j)[2:]),16)
        
        n3 = n1^n2

        n3 = hex(n3)[2:]
        n3 = (200-len(n3))*'0'+n3
        n3 = bytes.fromhex(n3)
        pts_bytes.append(n3)
        
        letters = 0
        for pt_byte in n3:
            if 0x41 <= pt_byte <= 0x5a or 0x61 <= pt_byte <= 0x7a or pt_byte == 32:
                letters+=1
                
        num_letters.append(letters)

    index = num_letters.index(max(num_letters))
    key_i.append(index)
````

Then we print the key `Terminator X: Bring the noise`. We look at every int in the key and find its ascii char value. We find all 29 of these characters and concat them to find key. 
````Python
key = ''

for i in key_i:
    key+=chr(i)

print('key')
print(key)
print()
````

Next we XOR the `i` character of the ciphertext with the `i%KEYLEN` character of the key to get the plaintext. Lastly we decode the plaintext to get it from a byte array into English. 
````Python
pt = bytearray()
for i in range(0,len(ct)):
    pt.append(ct[i]^key_i[i%KEYLEN])

print('plaintext')
print(pt.decode())
````

The plaintext is:
````
I'm back and I'm ringin' the bell 
A rockin' on the mike while the fly girls yell
In ecstasy in the back of me
Well that's my DJ Deshay cuttin' all them Z's
Hittin' hard and the girlies goin' crazy
Vanilla's on the mike, man I'm not lazy.

I'm lettin' my drug kick in
It controls my mouth and I begin
To just let it flow, let my concepts go
My posse's to the side yellin', Go Vanilla Go!

Smooth 'cause that's the way I will be
And if you don't give a damn, then
Why you starin' at me
So get off 'cause I control the stage
There's no dissin' allowed
I'm in my own phase
The girlies sa y they love me and that is ok
And I can dance better than any kid n' play

Stage 2 -- Yea the one ya' wanna listen to
It's off my head so let the beat play through
So I can funk it up and make it sound good
1-2-3 Yo -- Knock on some wood
For good luck, I like my rhymes atrocious
Supercalafragilisticexpialidocious
I'm an effect and that you can bet
I can take a fly girl and make her wet.

I'm like Samson -- Samson to Delilah
There's no denyin', You can try to hang
But you'll keep tryin' to get my style
Over and over, practice makes perfect
But not if you're a loafer.

You'll get nowhere, no place, no time, no girls
Soon -- Oh my God, homebody, you probably eat
Spaghetti with a spoon! Come on and say it!

VIP. Vanilla Ice yep, yep, I'm comin' hard like a rhino
Intoxicating so you stagger like a wino
So punks stop trying and girl stop cryin'
Vanilla Ice is sellin' and you people are buyin'
'Cause why the freaks are jockin' like Crazy Glue
Movin' and groovin' trying to sing along
All through the ghetto groovin' this here song
Now you're amazed by the VIP posse.

Steppin' so hard like a German Nazi
Startled by the bases hittin' ground
There's no trippin' on mine, I'm just gettin' down
Sparkamatic, I'm hangin' tight like a fanatic
You trapped me once and I thought that
You might have it
So step down and lend me your ear
'89 in my time! You, '90 is my year.

You're weakenin' fast, YO! and I can tell it
Your body's gettin' hot, so, so I can smell it
So don't be mad and don't be sad
'Cause the lyrics belong to ICE, You can call me Dad
You're pitchin' a fit, so step back and endure
Let the witch doctor, Ice, do the dance to cure
So come up close and don't be square
You wanna battle me -- Anytime, anywhere

You thought that I was weak, Boy, you're dead wrong
So come on, everybody and sing this song

Say -- Play that funky music Say, go white boy, go white boy go
play that funky music Go white boy, go white boy, go
Lay down and boogie and play that funky music till you die.

Play that funky music Come on, Come on, let me hear
Play that funky music white boy you say it, say it
Play that funky music A little louder now
Play that funky music, white boy Come on, Come on, Come on
Play that funky music
````