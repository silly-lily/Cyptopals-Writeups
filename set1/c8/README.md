# Challenge
We are given a list of possible ciphertexts one of which has been encrypedted with ECB. We need to find which ciphertext was encrypted using ECB.

# Solution
First we load and read the ciphertexts.
````Python
fp = open('set1/c8/data8.txt')
cts = fp.readlines()
````

Then we know that ECB is stateless and deterministic so any repeats in plaintext will cause a repeat in cipher text. So we look for the number of matches in the ciphertext. First we make an empty array for the number of matches with each corresponding cipher text. Then we loop through the ciphertext blocks twice and add `1` to matches whenever there is a match on two different blocks. 
````Python
num_matches = []
for ct in cts:

    matches = 0

    for i in range(0,len(ct),16):
        for j in range(0,len(ct),16):

            if ct[i:i+16] == ct[j:j+16] and i != j:
                matches+=1

    num_matches.append(matches)
````

Lastly, we find the ciphertext with the most matches and print the resulting ciphertext. 
````Python
index = num_matches.index(max(num_matches))
ct = cts[index]

print(ct)
````