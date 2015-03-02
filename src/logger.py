# -*- coding: utf-8 -*-

import sys

def enc( text ):
	return text.encode(sys.stdout.encoding, errors='replace')

def log( text ):
	print(enc(text), file = open("log.txt", "a"))

def clear():
	open("log.txt", "w+")
