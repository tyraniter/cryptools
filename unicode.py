#coding=utf-8

import sys
import os

def encode(plainText):
	return plainText.encode('unicode-escape').decode('utf-8')


def decode(encodedText):
	return bytes(encodedText,'utf-8').decode('unicode-escape')

def printHelp():
	print('Usage:')
	print('Encode:ASCII.py -e "Plaintext"')
	print('Decode:ASCII.py -d "Encodedtext"')
	
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