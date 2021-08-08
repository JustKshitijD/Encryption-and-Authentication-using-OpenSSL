f=open("private-key.pem","r")
c=0
for i in f:
	c+=1
print("c: ",c)	

f.close()
f=open("private-key.pem","r")

k=0
l=0

for i in f:
	print("k: ",k)
	print(i)
	if(k!=0 and k!=c-1):	
		r=len(i)-1
		print("r: ",r)
		l+=r
	k+=1	

print("l: ",l)
f.close()
