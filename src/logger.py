# -*- coding: utf-8 -*-

import sys

def enc( text ):
	return repr(text)

def log( text ):
	print(enc(text), file = open("log.txt", mode="a", encoding='utf-8'))

def clear():
	open("log.txt", "w+")
