#coding=utf-8

import os
import sys

index={'Q':'A', 'W':'B', 'E':'C', 'R':'D', 'T':'E', 'Y':'F', 'U':'G', 'I':'H', 'O':'I', 'P':'J', 'A':'K', 'S':'L', 'D':'M', 'F':'N', 'G':'O', 'H':'P', 'J':'Q', 'K':'R', 'L':'S', 'Z':'T', 'X':'U', 'C':'V', 'V':'W', 'B':'X', 'N':'Y', 'M':'Z'}

def encode(plain):
    return ''.join(map(lambda x:str(index.keys()[ord(x.upper())-65]),list(plain)))
    
def decode(encoded):
    return ''.join(map(lambda x:index[x],list(encoded)))
    
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
