'''
	Constructor takes filaname as parameter
	parse() method returns a list of all the tokens in the given file
	for some reason first(0) and last(len(L)) element of the list is a white space (?)
	so while using iterate from 1 to len(L)-1
'''

import re

class tokenizer:

	def __init__(self,file_name):
		self.file_name=file_name
	
	def parse(self):
		self.file_handle=open(self.file_name,"r")
		self.file_text=self.file_handle.read()
		self.list_to_be_returned=re.split('\W+',self.file_text)
		return self.list_to_be_returned


if __name__ == "__main__":
	t=tokenizer("test.txt")
	L=t.parse()
	for i in range(1,len(L)-1):
		print L[i]," ",i
		
