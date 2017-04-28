#coding=utf-8

def encode(plain):
	return ''.join(map(lambda x:r'\x'+str(hex(ord(x)))[2:],list(plain)))
	
def decode(encoded):
	return ''.join(map(lambda x:chr(int(x,16)),str.split(encoded,r'\x')[1:]))

def main():
		plain='The quick brown fox jumps over the lazy dog'
		encoded=encode(plain)
		print(encoded)
		print(decode(encoded))
		
if __name__=="__main__":
    main()