# Challenge
We have to transform the hex number `49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d` into its base64 representation `SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t`

# Solution
First we import the codecs package.
````Python 
    import codecs
````

Then we declare our hex integer.
````Python
b16 = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
````

Then we decode our hex integer to save it as bytes.
````Python
b2 = codecs.decode(b16, 'hex')
````

We then encode our hex integer in base 64. Now it is still in the form of bytes, so we decode it to a String. 
````Python
b64 = codecs.encode(b2, 'base64').decode()
````

Lastly, we print our solution to get `SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t`.
````Python
print(b64)
````