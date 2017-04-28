#coding=utf-8

import os
import sys

def encode(plain):
    return plain[::2]+plain[1::2]
    
def decode(encoded):
    l=len(encoded)/2
    front=encoded[:l]
    back=encoded[l:]
    return ''.join(map(lambda x:front[x]+back[x],range(l)))
    
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
