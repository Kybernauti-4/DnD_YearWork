to_convert = 'HELLO'
max_len = max([ord(letter) for letter in to_convert])

div = 0
while max_len/pow(10, div) > 1 :
	div += 1

converted = str(hex(div))
for letter in to_convert:
	converted += str(hex(ord(letter))).replace('0x','')



print(converted)