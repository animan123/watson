class generate_fingerprint:
	def set_group_size(self,no):
		self.group_size = no
	def __init__(self):
		self.set_group_size(3)
#Hash function that returns hashed string of length 10
	def hash(self,t):
		h=0
		for index in range(len(t)):
			h = h *33 + ord(t[index])
		return str(h)[:10]
#Group Function that creates groups of the list l based on the group size and returns equivalent hashed list
	def group(self,l):
		self.x=[]
		for start in range(len(l)-self.group_size+1):
			t=""
			for size in range(self.group_size):
				t=t+l[size+start]
			self.x.append(self.hash(t).zfill(10))	#padding 0's if length less than 10
		self.x.sort()
'''
l = ["Name","is","Akshay","Hi","My"]
te=generate_fingerprint()
te.group(l)
print te.x
'''