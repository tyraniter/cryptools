#coding=utf-8
import sys
import os

# 摩斯密码表(自己可定义加密方式...)
CODE = {
        # 26 letter
        'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
 
        # 10 number
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.',
 
        # 16 punctuation
        ',': '--..--', '.': '.-.-.-', ':': '---...', ';': '-.-.-.',
        '?': '..--..', '=': '-...-',  "'": '.----.', '/': '-..-.',
        '!': '-.-.--', '-': '-....-', '_': '..--.-', '(': '-.--.',
        ')': '-.--.-', '$': '...-..-','&': '. . . .','@': '.--.-.' 
}
# print CODE
# 反转字典(作为解密摩斯密码的字典)
UNCODE = dict(map(lambda t:(t[1],t[0]),CODE.items()))
#print (CODE)
#print (UNCODE)
 
'''
将字符串转换成摩斯密码
params:需要转换的字符串
'''
def encode(msg):
	# message用于保存加密结果
	message = ''
    # msg = raw_input('Message:')
    # msg = 'this is test'
    #print ('Plaintext:'+msg)
	for c in msg:
		if c == ' ':
			message += ' '
		else:
		# upper():将所有小写字母转换成大写字母
			message += CODE[c.upper()] + ' '
	return message
 
'''
将摩斯密码还原成字符串
params:需要还原的摩斯码
'''
def decode(morseCode):
	# message用于保存解密结果
	message = ''
	list = morseCode.split(' ')
	# print list
	#print ('Encodedtext:'+morseCode)
	for s in list:
		if s == '':
			message += ' '
		else:
			message += UNCODE[s]
	return message
 
 
# Test
# print stringToMorseAlphabet('I love you')
# print (morseAlphabetToString(stringToMorseAlphabet('what the fuck!')))

def printHelp():
	print('Usage:')
	print('Encode:MorseCode.py -e "Plaintext"')
	print('Decode:MorseCode.py -d "Encodedtext"')

def main():
	if len(sys.argv) != 3:
		printHelp()
	elif sys.argv[1] not in ('-e','-d'):
			printHelp()
	elif sys.argv[1] == '-e':
		msg=sys.argv[2]
		print('Plain:'+os.linesep+msg)
		print('Encoded:'+os.linesep+encode(msg))
	elif sys.argv[1] == '-d':
		msg=sys.argv[2]
		print('Encoded:'+os.linesep+msg)
		print('Plain:'+os.linesep+decode(msg))
	else:
		printHelp()


if __name__ == "__main__":
	main()