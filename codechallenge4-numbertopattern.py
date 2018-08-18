def NumberToSymbol(number):
    numDict = {0:'A', 1:'C', 2:'G', 3:'T'}
    return numDict[number]

def NumberToPattern(index, k):
    if k==1:
        return NumberToSymbol(index)
    prefixIdx, remain = divmod(index, 4)
    symbol = NumberToSymbol(remain)
    print(prefixIdx, remain, symbol)
    prefixPatt = NumberToPattern(prefixIdx, k-1)
    return prefixPatt + symbol
    
print(NumberToPattern(6819,10))