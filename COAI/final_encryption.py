
# Python program to 
# demonstrate merging 
# of two files 
  
data = data2 = "" 
  
# Reading data from file1 
with open('rsa_encrypted_session_key','rb') as fp: 
    data = fp.read() 
  
print("len(rsa_encrypted_session_key): ",len(data))

# Reading data from file2 
with open("session_key_encrypted_merged_enc_hash_and_message",'rb') as fp: 
    data2 = fp.read() 

print("len(session_key_encrypted_merged_enc_hash_and_message): ",len(data2))   

# with open("plaintext",'rb') as fp: 
#     data3 = fp.read() 

# print("len(plaintext): ",len(data3))    

  
# Merging 2 files 
# To add the data of file2 
# from next line 
# data += "\n"
data += data2 
#data+=data3
  
with open ('final_enc', 'wb') as fp: 
    fp.write(data)