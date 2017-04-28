#coding=utf-8

import sys
import os
import base64

#dos下参数的转义尚未解决

b642uu={'A':'`','B':'!','C':'"','D':'#','E':'$','F':'%','G':'&','H':"'",'I':'(','J':')','K':'*','L':'+','M':',','N':'-','O':'.','P':'/','Q':'0','R':'1','S':'2','T':'3','U':'4','V':'5','W':'6','X':'7','Y':'8','Z':'9','a':':','b':';','c':'<','d':'=','e':'>','f':'?','g':'@','h':'A','i':'B','j':'C','k':'D','l':'E','m':'F','n':'G','o':'H','p':'I','q':'J','r':'K','s':'L','t':'M','u':'N','v':'O','w':'P','x':'Q','y':'R','z':'S','0':'T','1':'U','2':'V','3':'W','4':'X','5':'Y','6':'Z','7':'[','8':'\\','9':']','+':'^','/':'_','=':'`'}
	
uu2b64={'`':'A','!':'B','"':'C','#':'D','$':'E','%':'F','&':'G',"'":'H','(':'I',')':'J','*':'K','+':'L',',':'M','-':'N','.':'O','/':'P','0':'Q','1':'R','2':'S','3':'T','4':'U','5':'V','6':'W','7':'X','8':'Y','9':'Z',':':'a',';':'b','<':'c','=':'d','>':'e','?':'f','@':'g','A':'h','B':'i','C':'j','D':'k','E':'l','F':'m','G':'n','H':'o','I':'p','J':'q','K':'r','L':'s','M':'t','N':'u','O':'v','P':'w','Q':'x','R':'y','S':'z','T':'0','U':'1','V':'2','W':'3','X':'4','Y':'5','Z':'6','[':'7','\\':'8',']':'9','^':'+','_':'/','`':'='}

index=r'''`!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_'''


def encode(plain):
	b64encoded=base64.b64encode(plain.encode('utf-8')).decode('utf-8')
	tmp=''.join(map(lambda x:b642uu[x],list(b64encoded)))
	result=[]
	while (len(tmp)>60):
		result.append('M'+tmp[0:60])
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
	b64decoded=''.join(map(lambda x:uu2b64[x],list(result)))
	return base64.b64decode(b64decoded).decode('utf-8')

def printHelp():
	print('Usage:')
	print('Encode:uu_encode.py -e "Plaintext"')
	print('Decode:uu_encode.py -d "Encodedtext"')

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