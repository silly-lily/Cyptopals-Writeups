import codecs

b16 = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
b2 = codecs.decode(b16, 'hex')
b64 = codecs.encode(b2, 'base64').decode()

print(b64)