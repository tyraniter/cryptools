#coding=utf-8

import os
import sys

index={21:'A', 22:'B', 23:'C', 31:'D', 32:'E', 33:'F', 41:'G', 42:'H', 43:'I', 51:'J',52:'K', 53:'L', 61:'M', 62:'N', 63:'O', 71:'P', 72:'Q', 73:'R', 74:'S', 81:'T',82:'U', 83:'V', 91:'W', 92:'X', 93:'Y', 94:'Z'}

def encode(plain):
    return ' '.join(map(lambda x:str(index.keys()[ord(x.upper())-65]),list(plain)))
    
def decode(encoded):
    return ''.join(map(lambda x:index[int(x)],encoded.split(' ')))
    
def printHelp():
    print('Usage:')
    print('Encode:tap_code.py -e "Plaintext"')
    print('Decode:tap_code.py -d "Encodedtext"')
    
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
