import os
import hashlib
import time
import bz2
import md5

#Program only does MD5 but will be able to do more I will continue to add more

#To clear screen but not really needed
def cls():
	os.system( [ 'clear', 'cls' ][ os.name == 'nt' ] )

def start():
	word = raw_input("Word: ")
	md5word = hashlib.md5(word).hexdigest()
	print(md5word)
	stop = raw_input(" ")
start()