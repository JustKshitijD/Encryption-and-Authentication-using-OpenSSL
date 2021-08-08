
# Python program to 
# demonstrate merging 
# of two files 
  
data = data2 = "" 
  
# Reading data from file1 
with open('rsa_encrypted_session_key','rb') as fp: 
    data = fp.read() 
  
print("len(data): ",len(data))

# Reading data from file2 
with open("session_key_encrypted_message",'rb') as fp: 
    data2 = fp.read() 

print("len(data2): ",len(data2))    
  
# Merging 2 files 
# To add the data of file2 
# from next line 
# data += "\n"
data += data2 

  
with open ('final_enc', 'wb') as fp: 
    fp.write(data)