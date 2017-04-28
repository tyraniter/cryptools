#coding=utf-8

import pycipher 
import sys
import os

def decipher(cipher,shift):
	return pycipher.Caesar(shift).decipher(cipher,True)

def printHelp():
	print('Usage:')
	print('Decode:caesar.py -d "Encodedtext" [shift]')

def main():
	if len(sys.argv) not in (3,4):
		printHelp()
	elif sys.argv[1] not in ('-d'):
			printHelp()
	elif sys.argv[1] == '-d':
		cipher=sys.argv[2]
		if len(sys.argv) == 4:
			shift=int(sys.argv[3])
			print('Cipher:'+os.linesep+cipher)
			print('Plain:'+os.linesep+decipher(cipher,shift))
		else:
			print('Cipher:'+os.linesep+cipher)
			print('Plain:')
			for shift in range(1,26):
				print("%02d" % shift+':'+decipher(cipher,shift))
	else:
		printHelp()
	

if __name__ == "__main__":
	main()