#coding=utf-8


index={}

def learn(plain,encoded):
	if len(plain) != len(encoded):
		return
	for i in range(len(plain)):
		 index[encoded[i]]=plain[i]

def decode(encoded):
	return ''.join(map(lambda x:index[x],list(encoded)))
	

def main():
	plain=input('Plain:')
	encoded=input('Encoded:')
	learn(plain,encoded)
	unknown_encoded=input('Question:')
	print(decode(unknown_plain))


if __name__ == "__main__":
	main()