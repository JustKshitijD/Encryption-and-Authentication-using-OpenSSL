
import subprocess
  
data = data2 = "" 
  
# Reading data from file1 
with open('session_key_RECV.txt','r') as fp: 
    data = fp.read() 
  
print("len(data): ",len(data))

# Reading data from file2 
with open("iv.txt",'r') as fp: 
    data2 = fp.read() 

print("len(data2): ",len(data2))    
  
 
if(len(data)==21): 
	with open("decrypt_line","w") as fp:
		fp.write("openssl enc -des-ede3-cbc -d -in session_key_encrypted_merged_enc_hash_and_message_RECV -K "+ str(data) +" -iv " + str(data2) +" -out merged_enc_hash_and_message_RECV\n")

elif(len(data)==32):
	with open("decrypt_line","w") as fp:
		fp.write("openssl enc -aes-256-cbc -d -in session_key_encrypted_merged_enc_hash_and_message_RECV -K "+ str(data) +" -iv " + str(data2)+  " -out merged_enc_hash_and_message_RECV\n")


