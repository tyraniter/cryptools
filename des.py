from pyDes import *


def encode(plain,key,IV):
	  k = des("DESCRYPT", CBC, "\0\0\0\0\0\0\0\0")
	k=des(plain,CBC,IV)


def decode():