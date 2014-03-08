#Hash function that returns hashed string of length 10
def hash(t):
	h=0
	for index in range(len(t)):
		h = h *33 + ord(t[index])
	return str(h)[:10]
#Group Function that creates groups of the list l based on the group size and returns equivalent hashed list
def group(l,group_size):
	x=[]
	for start in range(len(l)-group_size+1):
		t=""
		for size in range(group_size):
			t=t+l[size+start]
		x.append(hash(t).zfill(10))	#padding 0's if length less than 10
	x.sort()
	return x
#l = ["Name","is","Akshay","Hi","My"]
#print group(l,3)