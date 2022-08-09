# Challenge

We have to xor the hex number `1c0111001f010100061a024b53535009181c` with the hex number `686974207468652062756c6c277320657965` to get the hex number `746865206b696420646f6e277420706c6179`.

# Solution

First we declare our first integer as a string. 
````Python
n1 = '1c0111001f010100061a024b53535009181c'
````

Then we transform this string to an integer.
````Python
n1 = int('0x'+n1,16)
````

We do the same for the seccond string. So now we have two integers `n1` and `n2`. 
````Python
n2 = '686974207468652062756c6c277320657965'
n2 = int('0x'+n2,16)
````

Next we take the bitwise XOR of the two integers.
````Python
xor = n1^n2
````

Lastly we print our resulting XOR value `746865206b696420646f6e277420706c6179` in hexadecimal without the `0x` prefix. 
````Python
print(hex(xor)[2:])
````
