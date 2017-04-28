#coding=utf-8
import base64

alphabet={'A':'+','B':'-','C':'0','D':'1','E':'2','F':'3','G':'4','H':'5','I':'6','J':'7','K':'8','L':'9','M':'A','N':'B','O':'C','P':'D','Q':'E','R':'F','S':'G','T':'H','U':'I','V':'J','W':'K','X':'L','Y':'M','Z':'N','a':'O','b':'P','c':'Q','d':'R','e':'S','f':'T','g':'U','h':'V','i':'W','j':'X','k':'Y','l':'Z','m':'a','n':'b','o':'c','p':'d','q':'e','r':'f','s':'g','t':'h','u':'i','v':'j','w':'k','x':'l','y':'m','z':'n','0':'o','1':'p','2':'q','3':'r','4':'s','5':'t','6':'u','7':'v','8':'w','9':'x','+':'y','/':'z'}

def encode(plain):
	b64encoded=base64.b64encode(plain.encode('utf-8')).replace('=','')
	return ''.join(map(lambda x:alphabet[x],list(b64encoded.decode('utf-8'))))
	
def decode(encoded):
	return ''.join(map(lambda x:chr(int(x,16)),str.split(encoded,r'\x')[1:]))

def main():
		plain='The quick brown fox jumps over the lazy dog'
		encoded=encode(plain)
		print(encoded)
		print(decode(encoded))
		
if __name__=="__main__":
    main()