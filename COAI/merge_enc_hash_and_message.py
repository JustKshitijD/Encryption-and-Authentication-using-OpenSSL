
# Python program to
# demonstrate merging
# of two files

data = data2 = ""

# Reading data from file1
with open('rsa_encrypted_hash','rb') as fp:
    data = fp.read()

print("len(data): ",len(data))
print("rsa_encrypted_hash: ",data)

# Reading data from file2
with open("plaintext",'rb') as fp:
    data2 = fp.read()

print("len(data2): ",len(data2))
print("plaintext: ",data2)

# Merging 2 files
# To add the data of file2
# from next line
# data += "\n"
data += data2

print("len(data): ",len(data))
print("data: ",data)

with open ('merged_enc_hash_and_message', 'wb') as fp: 
    fp.write(data)
