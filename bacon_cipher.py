#coding=utf-8

import sys
import os

index=['AAAAA','AAAAB','AAABA','AAABB','AABAA','AABAB','AABBA','AABBB','ABAAA','ABAAA','ABAAB','ABABA','ABABB','ABBAA','ABBAB','ABBBA','ABBBB','BAAAA','BAAAB','BAABA','BAABB','BAABB','BABAA','BABAB','BABBA','BABBB']

def encode(plainText):
	return ' '.join(map(lambda x:index[ord(x)-65],list(plainText.upper())))


def decode(encodedText):
	tmp=encodedText.upper().replace(' ','')
	tmplist=[]
	for i in range(int(len(tmp)/5)):
		tmplist.append(tmp[i*5:i*5+5])
	return ''.join(map(lambda x:chr(index.index(x)+65),tmplist))

def printHelp():
	print('Usage:')
	print('Encode:bacon_cipher.py -e "Plaintext"')
	print('Decode:bacon_cipher.py -d "Encodedtext"')
	
def main():
	if len(sys.argv) != 3:
		printHelp()
	elif sys.argv[1] not in ('-e','-d'):
			printHelp()
	elif sys.argv[1] == '-e':
		plainText=sys.argv[2]
		print('Plain:'+os.linesep+plainText)
		print('Encoded:'+os.linesep+encode(plainText))
	elif sys.argv[1] == '-d':
		encodedText=sys.argv[2]
		print('Encoded:'+os.linesep+encodedText)
		print('Plain:'+os.linesep+decode(encodedText))
	else:
		printHelp()


if __name__ == "__main__":
	main()