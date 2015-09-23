table={
' ':'11',
'e':'101',
't':'1001',
'o':'10001',
'n':'10000',
'a':'011',
's':'0101',
'i':'01001',
'r':'01000',
'h':'0011',
'd':'00101',
'l':'001001',
'!':'001000',
'u':'00011',
'c':'000101',
'f':'000100',
'm':'000011',
'p':'0000101',
'g':'0000100',
'w':'0000011',
'b':'0000010',
'y':'0000001',
'v':'00000001',
'j':'000000001',
'k':'0000000001',
'x':'00000000001',
'q':'000000000001',
'z':'000000000000'
}


message = input()
convertedBin = ''

for word in message:
    for letter in word:
        convertedBin += table[letter]
    
if len(convertedBin) % 8 != 0:
    convertedBin += '0'*(len(convertedBin) - (int(len(convertedBin)/8))*8)
    
binary = [ int(convertedBin[pos:pos+8], 2) for pos in range(0, len(convertedBin), 8) ]
hexa = [hex(bit) for bit in binary]
[ print((len(i[2:]) == 1 and '0' or '') + i[2:].upper(), end=' ') for i in hexa ]