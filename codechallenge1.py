import re

def occurrences(input, pattern):
    regexp = '(?='+pattern+')'
    return len(re.findall(regexp, input))

with open("dataset_2_7.txt", "r") as f:
    for cnt, line in enumerate(f):
        #print("Line {}: {}".format(cnt, line))
        if cnt == 0:
            input = line[:-1]
        if cnt == 1:
            kmer  = line[:-1]
f.close()


#print(kmer)
#print(input.count("AGCCTTTAG"))
regexp = '(?='+kmer+')'
#print(regexp)
#print(sum(1 for _ in re.finditer(regexp, input)))
print(occurrences(input, kmer))

