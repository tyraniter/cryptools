#coding=utf-8

import os
import sys

index=['100000','110000','100100','100110','100010','110100','110110','110010','010100','010110','101000','111000','101100','101110','101010','111100','111110','111010','011100','011110','101001','111001','010111','101101','101111','101011']

def encode(plain):
    return ' '.join(map(lambda x:index[ord(x)-65],list(plain.upper())))
    
def decode(encoded):
    try:
        return ''.join(map(lambda x:chr(index.index(x)+65),encoded.split(' ')))
    except:
        return ''
    
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
