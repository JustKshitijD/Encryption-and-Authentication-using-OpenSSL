
# Python program to 
# demonstrate merging 
# of two files 
  
data = data2 = "" 
  
# Reading data from file1 
with open('final_enc','rb') as fp: 
    data = fp.read() 
  

print("len(data): ",len(data))

d1=data[0:256]
d2=data[256:]
 
print("len(rsa_encrypted_session_key_RECV): ",len(d1))
print("len(session_key_encrypted_merged_enc_hash_and_message_RECV): ",len(d2))

with open ('rsa_encrypted_session_key_RECV', 'wb') as fp: 
    fp.write(d1)

with open ('session_key_encrypted_merged_enc_hash_and_message_RECV', 'wb') as fp: 
    fp.write(d2)    
