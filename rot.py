#coding=utf-8

import sys
import os

def shiftDigit(cipher):
	if cipher.isdigit():
		return str((int(cipher)+5)%10)
	else:
		return cipher

def shiftAlpha(cipher):
	if cipher.isalpha():
		if cipher.isupper():
			return chr((ord(cipher)-65+13)% 26 + 65)
		else:
			return chr((ord(cipher)-97+13)% 26 + 97)
	else:
		return cipher

def shiftAll(cipher):
	if ord(cipher) in range(33,127):
		return chr((ord(cipher)-33+47)% 94 + 33)
	else:
		return cipher

def shiftAlphaAndDigit(cipher):
	if cipher.isdigit():
		return str((int(cipher)+5)%10)
	elif cipher.isalpha():
		if cipher.isupper():
			return chr((ord(cipher)-65+13)% 26 + 65)
		else:
			return chr((ord(cipher)-97+13)% 26 + 97)
	else:
		return cipher

def decipher5(cipher):
	return ''.join(map(shiftDigit,list(cipher)))

def decipher13(cipher):
	return ''.join(map(shiftAlpha,list(cipher)))

def decipher18(cipher):
	return ''.join(map(shiftAlphaAndDigit,list(cipher)))

def decipher47(cipher):
	return ''.join(map(shiftAll,list(cipher)))

def printHelp():
	print('Usage:')
	print('Decode:rot.py -d "Encodedtext" [5/13/18/47]')

decipherMode={5:decipher5,13:decipher13,18:decipher18,47:decipher47}

def main():
	if len(sys.argv) not in (3,4):
		printHelp()
	elif sys.argv[1] not in ('-d'):
			printHelp()
	elif sys.argv[1] == '-d':
		cipher=sys.argv[2]
		if len(sys.argv) == 4:
			mode=int(sys.argv[3])
			if mode in (5,13,18,47):
				print('Cipher:'+os.linesep+cipher)
				print('Plain:'+os.linesep+decipherMode.get(mode)(cipher))
		
	else:
		printHelp()
	

if __name__ == "__main__":
	main()