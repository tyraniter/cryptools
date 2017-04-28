#coding=utf-8

import sys
import os
import base64

b642xx={'A':'+','B':'-','C':'0','D':'1','E':'2','F':'3','G':'4','H':'5','I':'6','J':'7','K':'8','L':'9','M':'A','N':'B','O':'C','P':'D','Q':'E','R':'F','S':'G','T':'H','U':'I','V':'J','W':'K','X':'L','Y':'M','Z':'N','a':'O','b':'P','c':'Q','d':'R','e':'S','f':'T','g':'U','h':'V','i':'W','j':'X','k':'Y','l':'Z','m':'a','n':'b','o':'c','p':'d','q':'e','r':'f','s':'g','t':'h','u':'i','v':'j','w':'k','x':'l','y':'m','z':'n','0':'o','1':'p','2':'q','3':'r','4':'s','5':'t','6':'u','7':'v','8':'w','9':'x','+':'y','/':'z','=':'+'}

xx2b64={'+':'A','-':'B','0':'C','1':'D','2':'E','3':'F','4':'G','5':'H','6':'I','7':'J','8':'K','9':'L','A':'M','B':'N','C':'O','D':'P','E':'Q','F':'R','G':'S','H':'T','I':'U','J':'V','K':'W','L':'X','M':'Y','N':'Z','O':'a','P':'b','Q':'c','R':'d','S':'e','T':'f','U':'g','V':'h','W':'i','X':'j','Y':'k','Z':'l','a':'m','b':'n','c':'o','d':'p','e':'q','f':'r','g':'s','h':'t','i':'u','j':'v','k':'w','l':'x','m':'y','n':'z','o':'0','p':'1','q':'2','r':'3','s':'4','t':'5','u':'6','v':'7','w':'8','x':'9','y':'+','z':'/','+':'='}

index='+-0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


def encode(plain):
	b64encoded=base64.b64encode(plain.encode('utf-8')).decode('utf-8')
	tmp=''.join(map(lambda x:b642xx[x],list(b64encoded)))
	result=[]
	while (len(tmp)>60):
		result.append('h'+tmp[0:60])
		tmp=tmp[60:]
	result.append(index[int(len(tmp)/4*3)]+tmp)
	return os.linesep.join(result)

def decode(encoded):
	result=''
	tmp=encoded
	while (len(tmp)>61):
		result=result+tmp[1:61]
		tmp=tmp[61:]
	result=result+tmp[1:]
	b64decoded=''.join(map(lambda x:xx2b64[x],list(result)))
	return base64.b64decode(b64decoded).decode('utf-8')

def printHelp():
	print('Usage:')
	print('Encode:xx_encode.py -e "Plaintext"')
	print('Decode:xx_encode.py -d "Encodedtext"')

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

if __name__=="__main__":
    main()