fp = open('set1/c8/data8.txt')
cts = fp.readlines()

num_matches = []
for ct in cts:

    matches = 0

    for i in range(0,len(ct),16):
        for j in range(0,len(ct),16):

            if ct[i:i+16] == ct[j:j+16] and i != j:
                matches+=1

    num_matches.append(matches)

index = num_matches.index(max(num_matches))
ct = cts[index]

print(ct)