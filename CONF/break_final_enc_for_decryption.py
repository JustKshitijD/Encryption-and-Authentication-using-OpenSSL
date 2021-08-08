
# Python program to 
# demonstrate merging 
# of two files 
import sys
x=sys.argv[1]
  
data = data2 = "" 
  
# Reading data from file1 
with open('final_enc','rb') as fp: 
    data = fp.read() 
  

print("len(data): ",len(data))


if(str(x)=="2048"):
	d1=data[0:256]
	d2=data[256:]
if(str(x)=="1024"):
	d1=data[0:128]
	d2=data[128:]	
 
print("len(d1): ",len(d1))
print("len(d2): ",len(d2))

with open ('rsa_encrypted_session_key_RECV', 'wb') as fp: 
    fp.write(d1)

with open ('session_key_encrypted_message_RECV', 'wb') as fp: 
    fp.write(d2)    
