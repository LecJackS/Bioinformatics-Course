def symbolToNumber(symbol):
    symDict = {"A":0,
	           "C":1,
			   "G":2,
			   "T":3}
    return symDict[symbol]

def patternToNumber(pattern):
    if pattern is "":
        #last recursion
        return 0
    prefix = pattern[:-1]
    symbol = pattern[-1]
    return 4*patternToNumber(prefix)+symbolToNumber(symbol)
	
print(patternToNumber("AGT"))
print(patternToNumber("TCTTCCCTGGGTTAAGAAC"))
