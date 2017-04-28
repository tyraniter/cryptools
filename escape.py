#coding=utf-8

import os
import sys


def encode(plain):
	tmp=plain.encode('utf-16-be')
	encoded=''
	for i in range(0,int(len(tmp)/2)):
		encoded=encoded+'%u'+'%02x' % int(tmp[2*i])+'%02x' % int(tmp[2*i+1])
	return encoded

def decode(encoded):
	return ''.join(map(lambda x:bytes.fromhex(x).decode('utf-16-be'),encoded.split('%u')[1:]))

def printHelp():
	print('Usage:')
	print('Encode:escape.py -e "Plaintext"')
	print('Decode:escape.py -d "Encodedtext"')
	
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