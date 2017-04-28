#coding=utf-8

import os
import sys

index=[['A','B','C','D','E'],['F','G','H','I','J'],['L','M','N','O','P'],['Q','R','S','T','U'],['V','W','X','Y','Z']]

def encode(plain):
    pass
    
def decode(encoded):
    encoded=str(encoded)
    tmp=''
    for i in range(int(len(encoded)/2)):
        tmp=tmp+index[int(encoded[2*i])-1][int(encoded[2*i+1])-1]
    return tmp
    
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
