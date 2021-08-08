
# Python program to 
# demonstrate merging 
# of two files 
  
data = data2 = "" 
  
# Reading data from file1 
with open('hash_RECV','rb') as fp: 
    data = fp.read() 
  
#print("len(data): ",len(data))

# Reading data from file2 
with open("hash_from_rsa",'rb') as fp: 
    data2 = fp.read() 

print("hash_RECV: ",data)
print("hash_from_rsa: ",data2)

if(data==data2):
	print("==========================SUCCESS=================================")
