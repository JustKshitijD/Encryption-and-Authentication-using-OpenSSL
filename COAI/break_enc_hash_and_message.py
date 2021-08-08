
# Python program to 
# demonstrate merging 
# of two files 
  
data = data2 = "" 
  
# Reading data from file1 
with open('merged_enc_hash_and_message_RECV','rb') as fp: 
    data = fp.read() 
  
d1=data[0:256]
d2=data[256:]

print("len(rsa_encrypted_hash_RECV): ",len(d1))
#print("rsa_encrypted_hash: ",data)
print("len(plaintext_RECV): ",len(d2))
# Reading data from file2

with open("rsa_encrypted_hash_RECV",'wb') as fp: 
    fp.write(d1)

with open("plaintext_RECV",'wb') as fp: 
    fp.write(d2)
     

