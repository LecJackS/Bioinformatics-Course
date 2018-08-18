import re

def occurrences(input, pattern):
    regexp = '(?='+pattern+')'
    return len(re.findall(regexp, input))

with open("dataset_2_10.txt", "r") as f:
    for cnt, line in enumerate(f):
        #print("Line {}: {}".format(cnt, line))
        if cnt == 0:
            input = line[:-1]
        if cnt == 1:
            k     = int(line[:-1])
f.close()


#print(kmer)
#print(input.count("AGCCTTTAG"))
#regexp = '(?='+kmer+')'
#print(regexp)
#print(sum(1 for _ in re.finditer(regexp, input)))
#print(occurrences(input, kmer))

kmerdict = {}
for c in range(len(input)-k):
    kmer = input[c:c+k]
    if kmer not in kmerdict:
        kmerdict[kmer] = occurrences(input, kmer) 

print(kmerdict)
print(max(kmerdict.values()))
max_kmers = [i for i, v in kmerdict.items() if v == max(kmerdict.values())]
print(max_kmers)